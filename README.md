# Image Edge Detection & Subtraction App

A simple web app to detect edges in images and compare two images using subtraction, built with a Flask backend and OpenCV.

## Features
- Upload an image and detect edges using Canny edge detection
- Upload two images (template and test) and view their pixel-wise subtraction
- Live image preview before processing

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- Image Processing: OpenCV

## How to Run
1. Clone the repo
```bash
   git clone https://github.com/tejapulaparthi/Edge_Detection_and_Subtraction.git
   cd Edge_Detection_and_Subtraction
```
2. Install dependencies
```bash
   pip install flask flask-cors opencv-python numpy
```
3. Start the backend
```bash
   python app.py
```
4. Open `index.html` in your browser

## Future Improvements
- Add thresholding and ROI extraction
- Align images before subtraction (using feature matching)
- Better error handling on the frontend