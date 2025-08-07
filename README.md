# traffic-light-project
This project implements a smart traffic control system that dynamically sets the duration of a traffic light based on real-time vehicle counts from a camera. The workflow combines computer vision, machine learning, and automation for adaptive traffic management.

Key Components and Technologies Used:
Vehicle Detection (Computer Vision):

YOLOv3 (You Only Look Once): Used for real-time detection and counting of cars through webcam video feed.

OpenCV: Handles video capture, frame processing, and integration with YOLO for object detection.

Data Logging:

Detected car counts are accumulated over a configurable detection duration (set in config.py), with the results stored in a CSV file (car_count.csv).

Machine Learning Models:

scikit-learn: Several regression models (Linear Regression, Decision Tree, Random Forest, SVR, Gradient Boosting) are trained using historical traffic data (cleaned_data.csv).

The models predict the optimal traffic light timer (in seconds) based on the detected vehicle count.

Data Cleaning:

Outliers are detected and removed from raw data before model training for improved prediction accuracy.

Python Scripting and Notebooks:

Jupyter Notebooks: Used for model training, evaluation, and predictive analytics.

Python Scripts: Automate detection, counting, configuration management, data display, and model inference.

Configuration Management:

config.py: Stores parameters such as detection duration and file paths, allowing easy project configuration.

How It Works:
Vehicle Detection: The webcam captures live video; YOLOv3 detects and counts cars in real time.

Data Logging: After a set duration, the total count is saved.

Traffic Timer Prediction: The latest vehicle count is fed into the trained machine learning model, which predicts the optimal traffic light duration.

Automation: The system automatically logs data, updates configuration, and displays results
