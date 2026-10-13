<div align="center">

# 🏋️ AI Fitness Intelligence Platform

### An End-to-End AI Powered Fitness Analytics Platform

<p>
A comprehensive fitness intelligence platform built using <b>SQL Server</b>, <b>Python</b>, <b>FastAPI</b>, <b>Machine Learning</b>, <b>Streamlit</b>, and <b>Power BI</b>.
</p>

<p>

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![SQL Server](https://img.shields.io/badge/SQL_Server-Database-red?logo=microsoftsqlserver)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit)
![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?logo=powerbi)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-Random_Forest-green)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black?logo=github)

</p>

</div>

---

# 📌 Project Overview

The **AI Fitness Intelligence Platform** is an end-to-end data analytics and machine learning project designed to analyze fitness data, generate AI-powered recommendations, and provide interactive dashboards for users.

The platform integrates:

- SQL Server Database
- ETL Pipeline
- Feature Engineering
- Machine Learning
- REST APIs (FastAPI)
- Interactive Streamlit Application
- Power BI Dashboards

This project demonstrates a complete data analytics workflow from raw data collection to visualization and AI prediction.

---

# 🚀 Key Features

## 👤 User Management

- User Profiles
- User Analytics
- Health Information
- Progress Tracking

---

## 🏋️ Workout Analytics

- Workout Tracking
- Exercise Recommendation
- Workout History
- Calories Burned Analysis

---

## 🥗 Nutrition Analytics

- Meal Tracking
- Food Database
- Daily Nutrition Summary
- Macro Recommendation

---

## 💧 Hydration Tracking

- Daily Water Intake
- Hydration Recommendation
- Water Goal Monitoring

---

## 😴 Sleep Analytics

- Sleep Tracking
- Sleep History
- Recovery Analysis

---

## 🤖 AI Modules

- Weight Prediction
- Calorie Recommendation
- Macro Recommendation
- Workout Recommendation

---

## 📊 Analytics Dashboard

- Executive Dashboard
- User Analytics
- Workout Analytics
- Nutrition Dashboard
- Sleep Dashboard
- AI Insights Dashboard

---

## 🌐 REST API

- FastAPI Backend
- JSON APIs
- Modular Architecture
- Clean Endpoint Design

---

# 🎯 Project Objectives

- Build a production-style fitness analytics platform.
- Demonstrate SQL, Python, Machine Learning, and Business Intelligence skills.
- Generate AI-powered health recommendations.
- Create interactive dashboards for data-driven decision making.
- Showcase an end-to-end Data Analytics workflow suitable for portfolio and internship applications.

---

# ⭐ Highlights

- End-to-End Data Analytics Project
- SQL Server Database
- ETL Pipeline
- Machine Learning Integration
- FastAPI Backend
- Streamlit Frontend
- Power BI Dashboards
- Modular Project Structure
- Git Version Control
- Portfolio Ready


---

# 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python 3.12 |
| Database | Microsoft SQL Server |
| Backend | FastAPI |
| Frontend | Streamlit |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Data Visualization | Plotly, Power BI |
| Version Control | Git & GitHub |

---

# 🏗️ System Architecture

```text
                         +----------------------+
                         |     SQL Server       |
                         |      Database        |
                         +----------+-----------+
                                    |
                                    |
                         ETL Pipeline (Python)
                                    |
                                    |
                         Feature Engineering
                                    |
                                    |
                    +---------------+---------------+
                    |                               |
                    |                               |
            Machine Learning                 FastAPI Backend
                    |                               |
                    +---------------+---------------+
                                    |
                              Streamlit UI
                                    |
                                    |
                           Power BI Dashboard
```

---

# 📂 Project Structure

```text
AI_Fitness_Intelligence_Platform/
│
├── app/                    # Streamlit Application
│
├── artifacts/
│   ├── eda_reports/
│   ├── processed_data/
│   ├── reports/
│   └── data_quality_report.csv
│
├── configs/                # Configuration Files
│
├── data/                   # Raw Dataset
│
├── scripts/                # Utility Scripts
│
├── sql/                    # SQL Scripts
│
├── src/
│   ├── api/
│   ├── auth/
│   ├── common/
│   ├── constants/
│   ├── database/
│   ├── etl/
│   ├── exceptions/
│   ├── models/
│   ├── recommendation/
│   ├── repository/
│   ├── services/
│   └── utils/
│
├── streamlit/              # Dashboard Pages
│
├── tests/                  # Unit Tests
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🗄️ Database Design

The project uses **Microsoft SQL Server** as the primary relational database.

### Main Tables

- Users
- Workouts
- Meals
- MealItems
- FoodItems
- Diet
- Sleep
- DailyProgress
- Goals

The database stores user fitness activities, nutrition records, sleep history, workout logs, and health progress for analytics and AI model training.

---

# ⚙️ ETL Pipeline

The ETL pipeline automates the complete data preparation workflow.

### Extract

- SQL Server
- CSV Files

### Transform

- Missing Value Handling
- Data Cleaning
- Feature Engineering
- Data Validation
- Outlier Processing

### Load

- Processed Dataset
- Feature Engineered Dataset
- ML Training Dataset

---

# 📊 Exploratory Data Analysis (EDA)

The project performs detailed Exploratory Data Analysis to understand user behavior and fitness trends.

### EDA Includes

- Missing Value Analysis
- Duplicate Detection
- Distribution Analysis
- Correlation Analysis
- Outlier Detection
- Summary Statistics
- Data Quality Report

Generated reports are stored inside the **artifacts** folder.

---

# 🤖 Machine Learning

The platform integrates Machine Learning to provide intelligent fitness recommendations and predictive analytics.

## Current Model

| Model | Random Forest Regressor |
|--------|--------------------------|
| Task | Weight Prediction |
| Framework | Scikit-learn |

### Input Features

- Age
- Gender
- Height (cm)
- Current Weight
- Calories Consumed
- Calories Burned
- Protein Intake
- Carbohydrate Intake
- Fat Intake
- Sleep Hours
- Workout Duration

### Model Performance

| Metric | Score |
|---------|-------|
| MAE | 1.26 |
| RMSE | 2.05 |
| R² Score | 0.9781 |

The trained model is serialized using **Joblib** and exposed through the FastAPI backend for real-time predictions.

---

# 🌐 FastAPI Backend

The backend is built using **FastAPI** and provides REST APIs for AI predictions and fitness recommendations.

## Features

- Modular API Architecture
- RESTful Endpoints
- JSON Responses
- Input Validation
- Error Handling
- Backend Health Check
- Easy Integration with Streamlit

---

## AI Endpoints

Current API modules include:

- Weight Prediction
- Calorie Recommendation
- Macro Recommendation
- Hydration Recommendation
- Workout Recommendation
- Health Score
- System Health Check

---

# 🎨 Streamlit Dashboard

The project includes a modern interactive dashboard developed using Streamlit.

## Dashboard Modules

- 🏠 Dashboard
- ⚖️ Weight Prediction
- 🔥 Calorie Recommendation
- 🥗 Macro Recommendation
- 💧 Hydration Recommendation
- 🏋️ Workout Recommendation
- 🍽️ Meal Recommendation
- ❤️ Health Score
- 👤 User Profile

---

## Dashboard Features

- Interactive Charts
- KPI Cards
- Progress Tracking
- AI Insights
- Responsive Layout
- Sidebar Navigation
- Real-Time API Integration

---

# ⚙️ Installation Guide

## Clone Repository

```bash
git clone https://github.com/MayankCodes2006/AI_Fitness_Intelligence_Platform.git

cd AI_Fitness_Intelligence_Platform
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

### Activate (Windows)

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root and configure the required database and application settings.

Example:

```env
DB_SERVER=YOUR_SERVER
DB_DATABASE=YOUR_DATABASE
DB_AUTH=windows
```

---

## Run FastAPI

```bash
uvicorn src.api.main:app --reload
```

---

## Run Streamlit

```bash
streamlit run app/main.py
```

> **Note:** Update the Streamlit entry point if your project uses a different startup file.

---

# 🧪 Testing

Run the project test suite using:

```bash
pytest
```

The `tests/` directory contains test cases for different modules of the application.

---

# 📈 Future Enhancements

- AI Chatbot for Fitness Assistance
- Personalized Meal Planning
- Exercise Form Analysis
- Wearable Device Integration
- Real-Time Notifications
- Authentication & User Accounts
- Cloud Deployment
- Docker Support
- CI/CD Pipeline
- Mobile Application

---

# 📊 Power BI Dashboards

The project includes interactive Power BI dashboards for business intelligence and fitness analytics.

## Dashboards

### 📈 Executive Dashboard

Provides an overview of the entire platform.

Features:

- Total Users
- Average Weight
- Average Sleep
- Total Goals
- Calories Burned
- Weight Trend
- Gender Distribution
- Workout Analytics

---

### 👤 User Analytics Dashboard

- User Distribution
- Gender Analysis
- Age Analysis
- Height & Weight Distribution
- User Activity

---

### 🏋️ Workout Analytics Dashboard

- Workout Frequency
- Exercise Distribution
- Calories Burned
- Workout Performance

---

### 🥗 Nutrition Analytics Dashboard

- Daily Calories
- Protein Intake
- Carbohydrates
- Fat Consumption
- Nutrition Trends

---

### 😴 Sleep & Health Dashboard

- Sleep Analysis
- Health Score
- Goal Progress
- Recovery Insights

---

# 📷 Project Screenshots

## Streamlit Dashboard

> Add screenshots here after completing the UI.

Example:

```
screenshots/
    dashboard.png
    weight_prediction.png
    workout.png
```

---

## Power BI Dashboard

> Add Power BI dashboard screenshots here.

Example:

```
screenshots/
    executive_dashboard.png
    user_dashboard.png
    workout_dashboard.png
```

---

# 📌 Project Roadmap

## Phase 1

- SQL Server Database
- Data Generation
- ETL Pipeline

✅ Completed

---

## Phase 2

- Exploratory Data Analysis
- Feature Engineering

✅ Completed

---

## Phase 3

- Machine Learning
- Weight Prediction

✅ Completed

---

## Phase 4

- FastAPI Backend

✅ Completed

---

## Phase 5

- Streamlit Dashboard

✅ Completed

---

## Phase 6

- Power BI Dashboard

🚧 In Progress

---

## Phase 7

- Deployment

⏳ Planned

---

# 🤝 Contributing

Contributions, suggestions, and improvements are always welcome.

If you find any bugs or have ideas to improve the project, feel free to open an issue or submit a pull request.

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## Harsh

**B.Tech (Data Science)**

Passionate about:

- Data Analytics
- Machine Learning
- SQL
- Python
- Power BI
- Artificial Intelligence

---

# 📬 Contact


Project Repository

https://github.com/Harsh/AI_Fitness_Intelligence_Platform

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star on GitHub!

Thank you for visiting this repository.

Made with ❤️ using Python, SQL Server, FastAPI, Streamlit, Machine Learning and Power BI.

</div>