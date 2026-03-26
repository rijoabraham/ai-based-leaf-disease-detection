# Leaf Health Detector - Interim Presentation 2 (PPT Content)

## Slide 1: Title Slide
- Title: Leaf Health Detector
- Subtitle: Interim Presentation 2
- Dates: 16/03/2026, 23/03/2026, 24/03/2026
- Team/Presenter: [Add your name]
- Guide: Keep this slide minimal and clean.

## Slide 2: Problem Statement and Objective
- Plant diseases reduce crop yield and increase farmer losses.
- Manual disease diagnosis needs expert support and takes time.
- Objective: Build an AI-based web app to detect plant leaf diseases quickly.
- Expected benefit: Early intervention and better crop health decisions.

## Slide 3: Process Flow Diagram (Workflow)
- Use this flow in SmartArt/diagram format:
1. User opens web app
2. Upload leaf image
3. Flask backend receives image
4. Preprocess image (RGB, resize 224x224, tensor conversion)
5. CNN model inference (PyTorch)
6. Predicted class index (0 to 38)
7. Fetch disease data from disease_info.csv
8. Fetch supplement data from supplement_info.csv
9. Display result page (disease + prevention + supplement)
10. Optional market page for product links

## Slide 4: System Architecture and Modules
- Frontend module:
  - HTML templates: home, index, submit, market, contact
- Backend module:
  - Flask routes in app.py
  - Image upload and prediction trigger
- AI module:
  - CNN model in CNN.py
  - 39 output classes
- Knowledge module:
  - disease_info.csv
  - supplement_info.csv

## Slide 5: Dataset / Database Description
- Dataset classes: 39 (disease + healthy classes)
- disease_info.csv: 39 rows
- supplement_info.csv: 39 rows
- disease_info.csv fields:
  - index, disease_name, description, Possible Steps, image_url
- supplement_info.csv fields:
  - index, disease_name, supplement name, supplement image, buy link
- Mapping logic:
  - Predicted class index maps to both CSV files for final recommendation.

## Slide 6: Proposed Method (Algorithm)
- Algorithm: Convolutional Neural Network (CNN) image classification
- Input: leaf image resized to 224x224
- Prediction pipeline:
  - RGB conversion
  - Tensor conversion
  - Forward pass through CNN
  - Argmax to select class
- CNN architecture summary:
  - 4 Conv blocks with BatchNorm and MaxPool
  - Dense layer: 50176 -> 1024 -> 39
  - Dropout(0.4) for regularization

## Slide 7: Results and Screenshots
- Functional result achieved:
  - Upload image -> prediction -> disease details + prevention + supplement
- Insert screenshots from demo_images:
  - Home page: demo_images/Screenshot 2025-07-03 013624.png
  - Prediction input page: demo_images/Screenshot 2025-07-03 013854.png
  - Prediction result page: demo_images/Screenshot 2025-07-03 014910.png
  - Market page: demo_images/Screenshot 2025-07-03 015050.png
- Note:
  - Keep screenshot labels visible under each image.

## Slide 8: Conclusion
- The project successfully integrates deep learning with a web interface.
- Current prototype can classify 39 classes and provide practical guidance.
- CSV-based recommendation system enables fast integration of disease/supplement data.

## Slide 9: Future Enhancements
- Improve robustness with more real-field image data.
- Add confidence score and top-3 predictions.
- Support multilingual user interface.
- Add user feedback loop for wrong predictions.
- Move CSV data to database (SQLite/PostgreSQL).
- Add severity-stage prediction (early/mid/late).

## Slide 10: Demo Flow / Thank You
- Demo steps:
1. Open home page
2. Go to prediction page
3. Upload sample leaf image
4. Show result page output
5. Show market recommendation page
- Closing: Thank you
- Q and A

---

## Design Tips for Fast PPT Creation
- Use a clean template with green/agriculture theme.
- Use one visual per slide where possible.
- Keep text to 5-7 bullet lines per slide.
- Highlight keywords in bold (Objective, Dataset, Algorithm, Results).
