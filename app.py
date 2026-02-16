import streamlit as st
import cv2
import numpy as np
import tempfile
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
from core_logic import TrafficAnalyzer

# Load analyzer once
analyzer = TrafficAnalyzer()

st.set_page_config(page_title="Smart Traffic Analyzer", layout="wide")

st.title("🚦 Smart Traffic Monitoring System")

# Sidebar
mode = st.sidebar.radio(
    "Select Input Source",
    ["Image", "Video", "Live Camera"]
)

# ================= IMAGE =================
if mode == "Image":
    file = st.file_uploader("Upload traffic image", type=["jpg", "png"])

    if file:
        img_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
        img = cv2.imdecode(img_bytes, 1)

        result, stats = analyzer.analyze_frame(img)

        col1, col2 = st.columns([3, 1])
        col1.image(result, use_column_width=True)

        col2.metric("Vehicles", stats["total_vehicles"])
        col2.metric("Blue Vehicles", stats["blue_vehicles"])
        col2.metric("People", stats["people_count"])


# ================= VIDEO =================
elif mode == "Video":
    video = st.file_uploader("Upload video", type=["mp4", "avi"])

    if video:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(video.read())

        cap = cv2.VideoCapture(tfile.name)

        frame_window = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            result, stats = analyzer.analyze_frame(frame)

            frame_window.image(result, channels="RGB")

        cap.release()


# ================= LIVE =================
elif mode == "Live Camera":

    class VideoProcessor(VideoTransformerBase):
        def transform(self, frame):
            img = frame.to_ndarray(format="bgr24")
            result, _ = analyzer.analyze_frame(img)
            return result

    webrtc_streamer(key="traffic-live",
                    video_processor_factory=VideoProcessor)