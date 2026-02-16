import cv2
import numpy as np
from ultralytics import YOLO


class TrafficAnalyzer:
    """
    Real-time traffic analyzer:
    - Detects vehicles and people
    - Identifies blue vehicles
    - Counts traffic
    """

    def __init__(self, model_path="yolov8n.pt"):
        # Load YOLO once (faster)
        self.model = YOLO(model_path)

        # Vehicle classes from COCO
        self.vehicle_classes = ["car", "bus", "truck"]

        # HSV blue ranges (robust for real-world lighting)
        self.BLUE_LOWER1 = np.array([100, 150, 0])
        self.BLUE_UPPER1 = np.array([120, 255, 255])

        self.BLUE_LOWER2 = np.array([120, 50, 50])
        self.BLUE_UPPER2 = np.array([140, 255, 255])

    def _is_blue_vehicle(self, crop):
        """Check whether a cropped vehicle region is blue."""
        if crop is None or crop.size == 0:
            return False

        hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)

        mask1 = cv2.inRange(hsv, self.BLUE_LOWER1, self.BLUE_UPPER1)
        mask2 = cv2.inRange(hsv, self.BLUE_LOWER2, self.BLUE_UPPER2)
        mask = mask1 + mask2

        # Ratio of blue pixels
        blue_ratio = np.count_nonzero(mask) / (mask.shape[0] * mask.shape[1])

        return blue_ratio > 0.03

    def analyze_frame(self, frame):
        """
        Process a single frame:
        - Detect objects
        - Apply color logic
        - Count vehicles and people
        """

        results = self.model(frame, stream=True)

        stats = {
            "total_vehicles": 0,
            "blue_vehicles": 0,
            "people_count": 0
        }

        annotated = frame.copy()

        for r in results:
            for box in r.boxes:

                # Confidence filter (reduces noise)
                if float(box.conf[0]) < 0.4:
                    continue

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cls_id = int(box.cls[0])
                label = self.model.names[cls_id]

                # -------- PERSON --------
                if label == "person":
                    stats["people_count"] += 1

                    cv2.rectangle(annotated, (x1, y1), (x2, y2),
                                  (0, 255, 0), 2)

                # -------- VEHICLES --------
                elif label in self.vehicle_classes:
                    stats["total_vehicles"] += 1

                    vehicle_crop = frame[y1:y2, x1:x2]

                    if self._is_blue_vehicle(vehicle_crop):
                        stats["blue_vehicles"] += 1
                        color = (0, 0, 255)  # red box
                    else:
                        color = (255, 0, 0)  # blue box

                    cv2.rectangle(annotated, (x1, y1), (x2, y2),
                                  color, 3)

        # Convert BGR → RGB
        return cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB), stats