# Gender Detection Using Machine Learning

## Overview

This project predicts gender (Male or Female) based on a person's name using Machine Learning and Flask.

The model is trained using a CSV dataset containing names and their corresponding genders. When a user enters a name through the web interface, the trained model predicts whether the name belongs to a Male or Female.

---

## Features

* Gender prediction using names
* Machine Learning Classification Model
* Flask Web Application
* Simple User Interface
* CSV Dataset Based Training
* Fast and Easy Prediction

---

## Technologies Used

* Python
* Flask
* Pandas
* Scikit-learn
* Pickle
* HTML/CSS

---

## Project Structure

Gender-Detection/

├── app.py

├── train_model.py

├── gender_data.csv

├── model.pkl

├── requirements.txt

└── templates/

  └── index.html

---

## Dataset

Sample Dataset:

| ID | Name   | Gender |
| -- | ------ | ------ |
| 1  | Karan  | Male   |
| 2  | Sneha  | Female |
| 3  | Rahul  | Male   |
| 4  | Priya  | Female |
| 5  | Arjun  | Male   |
| 6  | Kavya  | Female |
| 7  | Rohit  | Male   |
| 8  | Anjali | Female |
| 9  | Vijay  | Male   |
| 10 | Divya  | Female |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/navya131/Gender-Detection.git
cd Gender-Detection
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## Train the Model

Run:

```bash
python train_model.py
```

This creates:

```text
model.pkl
```

---

## Run Flask Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Working

1. User enters a name.
2. Flask sends the name to the trained ML model.
3. The model predicts the gender.
4. Result is displayed on the webpage.

Example:

Input:

```text
Sneha
```

Output:

```text
Predicted Gender: Female
```

Input:

```text
Rahul
```

Output:

```text
Predicted Gender: Male
```
<img width="1920" height="1008" alt="Screenshot 2026-06-11 222437" src="https://github.com/user-attachments/assets/774d9377-4b54-4c87-81a6-a0ba8d629b61" />

---

## Future Enhancements

* Larger Dataset
* Improved Accuracy
* Multiple Language Support
* API Integration
* Deployment on Render/Heroku

---

## Author

Navya Botla

Machine Learning Project – Gender Detection Using Names
