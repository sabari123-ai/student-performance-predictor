# 🎓 Student Performance Predictor

A beginner-friendly Machine Learning web application that predicts a student's estimated final exam score based on daily study hours, attendance percentage, and previous exam score.

Built using Python, Scikit-learn, Pandas, and Streamlit.

## 📌 Project Overview

The Student Performance Predictor uses **Linear Regression**, a supervised Machine Learning algorithm, to learn relationships between student-related input features and final exam scores.

Users can enter student details through an interactive web interface and receive an estimated final score.

This project demonstrates the basic Machine Learning workflow, including data preparation, model training, evaluation, prediction, and web application development.

## ✨ Features

- 📊 **Student Dataset:** Uses a sample dataset containing 30 records.
- 🧹 **Data Preparation:** Separates input features and the target variable.
- 🤖 **Machine Learning:** Trains a Linear Regression model.
- 📈 **Model Evaluation:** Evaluates predictions using Mean Absolute Error (MAE) and R² score.
- 🎯 **Score Prediction:** Estimates final exam scores from user-provided inputs.
- 🌐 **Interactive Web App:** Provides an easy-to-use interface built with Streamlit.
- 💾 **Model Persistence:** Saves the trained model as a pickle file.
- 🔧 **Version Control:** Uses Git and GitHub to manage the source code.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Dataset loading and manipulation |
| Scikit-learn | Model training, prediction, and evaluation |
| Linear Regression | Score prediction algorithm |
| Streamlit | Interactive web interface |
| Matplotlib | Data visualization library |
| Git | Version control |
| GitHub | Source code hosting |

## 📂 Project Structure

```text
student-performance-ml/
│
├── app.py                 # Streamlit web application
├── train_model.py         # Model training and evaluation
├── students.csv           # Sample student dataset
├── student_model.pkl      # Saved trained model
├── requirements.txt       # Python dependencies
├── .gitignore             # Files excluded from Git
└── README.md              # Project documentation
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or later
- Git
- Visual Studio Code (recommended)

### 1. Clone the repository

```bash
git clone https://github.com/sabari123-ai/student-performance-predictor.git
cd student-performance-predictor
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Train the Machine Learning model

```bash
python train_model.py
```

This command trains the Linear Regression model, evaluates its performance, and generates `student_model.pkl`.

### 5. Launch the web application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

`http://localhost:8501`

## 🚀 How to Use

1. Launch the Streamlit application.
2. Enter the student's daily study hours.
3. Select the attendance percentage.
4. Enter the previous exam score.
5. Click **Predict Final Score**.
6. View the estimated score displayed by the application.
7. Change the inputs and compare the resulting predictions.

## 🧠 Machine Learning Workflow

1. **Load data:** Read student records from `students.csv` using Pandas.
2. **Select features:** Use study hours, attendance, and previous score as input variables.
3. **Select target:** Use final score as the prediction target.
4. **Split the dataset:** Allocate 80% of the records for training and 20% for testing.
5. **Train the model:** Fit a Linear Regression model using the training data.
6. **Generate predictions:** Predict scores for the test records.
7. **Evaluate performance:** Calculate MAE and R² score.
8. **Save the model:** Store the trained estimator using Python's pickle module.
9. **Deploy locally:** Use Streamlit to collect user inputs and display predictions.

## 📏 Model Evaluation

The initial model training run produced the following results:

| Metric | Observed result |
|---|---:|
| Total sample records | 30 |
| Training records | 24 |
| Testing records | 6 |
| Mean Absolute Error (MAE) | 0.70 |
| R² score (displayed to 2 decimal places) | 1.00 |

**MAE (Mean Absolute Error):** Measures the average absolute difference between actual and predicted scores. A lower value generally indicates smaller prediction errors on the evaluated data.

**R² score:** Indicates how well the model's predictions fit the observed target values on the test set. The displayed value of 1.00 is rounded to two decimal places.

These results are from a small, synthetic dataset and are intended for demonstration. They do not establish real-world predictive accuracy.

## ⚠️ Limitations

- The dataset contains only 30 artificially created sample records.
- The model may not generalize to real student populations.
- Predictions depend only on the three available input features.
- Factors such as exam difficulty, teaching quality, health, and study habits are not included.
- The predicted score is an estimate, not a guaranteed exam result.
- The displayed evaluation metrics may be overly optimistic because the sample data follows simple patterns.
- The application does not use a real-world student database.

Future improvements could include collecting a larger representative dataset, performing cross-validation, comparing different regression algorithms, adding visualizations, and improving input validation.

## 🔮 Future Enhancements

- Add exploratory data analysis and charts.
- Compare Linear Regression with Random Forest and other regression models.
- Introduce cross-validation and more robust evaluation.
- Improve the interface with prediction history.
- Add model comparison and feature importance analysis.
- Deploy the application to a public hosting platform.

## 🎓 Learning Outcomes

Through this project, I practiced:

- Python programming and data manipulation.
- Basic supervised Machine Learning.
- Training and testing data separation.
- Regression model evaluation.
- Building an interactive application with Streamlit.
- Saving and loading a trained model.
- Git version control and GitHub repository management.

## 👩‍💻 Author

**Sabari Durga**

GitHub: [@sabari123-ai](https://github.com/sabari123-ai)

## 📄 License

This project is intended for educational and learning purposes. A formal open-source license can be added if the project is to be distributed or reused by others.