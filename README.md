# 🚦 Smart Traffic Monitoring System  
### Real-Time Vehicle Detection, Colour Classification & Traffic Analytics  

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![YOLO](https://img.shields.io/badge/YOLOv8-Object%20Detection-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Computer Vision](https://img.shields.io/badge/Computer%20Vision-AI-orange)

---

## 📌 Overview  
The **Smart Traffic Monitoring System** is a real-time computer vision and deep learning application that detects vehicles and pedestrians, identifies blue vehicles, and provides traffic insights through an interactive web dashboard.

This project demonstrates how Artificial Intelligence and Computer Vision can be used to build intelligent transportation and smart city solutions.

The system supports:
- Image input  
- Video input  
- Live webcam monitoring  

---

## 🎯 Objectives  
- Detect vehicles and pedestrians in real time  
- Identify blue vehicles using colour segmentation  
- Count total traffic density  
- Provide analytics through an interactive dashboard  
- Enable smart traffic monitoring  

---

## 🧠 System Workflow  
Traffic Input (Image / Video / Live Camera) → YOLOv8 Object Detection → Vehicle Region Extraction → Colour Detection (HSV Model) → Bounding Box + Traffic Statistics → Real-Time Streamlit Dashboard

---

## 🚀 Features  

### 🔹 Real-Time Object Detection  
Detects:
- Cars  
- Buses  
- Trucks  
- Pedestrians  

### 🔹 Blue Vehicle Identification  
- Blue vehicles → Red bounding box  
- Other vehicles → Blue bounding box  

### 🔹 Traffic Analytics  
Displays:
- Total vehicles  
- Blue vehicles  
- People count  

### 🔹 Multi-Input Support  
- Upload traffic images  
- Upload video clips  
- Live camera monitoring  

### 🔹 Interactive GUI  
- Clean and responsive Streamlit dashboard  
- Real-time processing  
- Easy to use interface  

---

## ⚙️ Tech Stack  
- Python  
- OpenCV  
- YOLOv8  
- Streamlit  
- NumPy  
- Deep Learning  
- Computer Vision  

---

## 📊 Applications  
- Smart traffic monitoring  
- Traffic congestion analysis  
- Urban planning  
- Smart city infrastructure  
- Surveillance and security  
- Intelligent transportation systems  

---

## 📂 Project Structure  
```
smart-traffic-monitoring/
├── app.py
├── core_logic.py
├── requirements.txt
└── README.md
```

---

## 🛠 Installation  

### Step 1: Clone the Repository  

```bash
git clone https://github.com/UtkarstDawar/smart-traffic-monitoring.git
cd smart-traffic-monitoring
```

### Step 2: (Optional) Create and activate a virtual environment  
```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.\.venv\Scripts\activate
```

### Step 3: Install dependencies  
```bash
pip install -r requirements.txt
```

### Step 4: Run the app  
```bash
streamlit run app.py
```

---

## 🔮 Future Enhancements  
- Vehicle tracking and unique counting  
- Deep learning-based colour classification  
- Smart traffic signal automation  
- Number plate recognition  
- Cloud deployment  
- IoT integration  
- Real-time traffic analytics dashboard  

---

## 📈 Learning Outcomes  
This project helped in building skills in:
- Real-time AI system development  
- Deep learning deployment  
- Computer vision  
- Image processing  
- Full-stack AI applications  
- Software engineering  

---

## 🤝 Contribution  
Contributions are welcome! Feel free to fork this repository and improve the project.

---

## 📜 License  
This project is open-source and available under the MIT License.

---

## 👨‍💻 Author  
Utkarst Dawar