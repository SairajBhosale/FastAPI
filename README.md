# 🏥 Insurance Premium Category Predictor

A machine learning-powered FastAPI application that predicts insurance premium categories based on user demographics and health information.

## 📋 Overview

This project uses a pre-trained machine learning model to classify users into insurance premium categories (Low, Medium, High) based on factors such as age, weight, height, income, smoking status, city, and occupation.

## ✨ Features

- **FastAPI Backend**: High-performance API with automatic documentation
- **ML-Powered Predictions**: Pre-trained scikit-learn model for accurate categorization
- **Input Validation**: Robust data validation using Pydantic models
- **Computed Fields**: Automatic calculation of BMI, lifestyle risk, age groups, and city tiers
- **Docker Support**: Containerized deployment for easy scaling
- **RESTful API**: Clean and intuitive endpoint design

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **ML Library**: scikit-learn
- **Data Processing**: pandas
- **Validation**: Pydantic
- **Server**: Uvicorn
- **Containerization**: Docker

## 📁 Project Structure

```
FastAPI/
├── fastapp.py           # Main FastAPI application
├── model.pkl            # Pre-trained ML model
├── user_input.py        # Pydantic input models
├── city_tier.py         # City tier classification
├── predict.py           # Prediction logic
├── requirements.txt     # Python dependencies
└── Dockerfile          # Docker configuration
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- pip or conda

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SairajBhosale/FastAPI.git
   cd FastAPI
   ```

2. **Create a virtual environment**
   ```bash
   # Using venv
   python -m venv myenv
   
   # Activate (Windows)
   myenv\Scripts\Activate
   
   # Activate (Linux/Mac)
   source myenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

**Local Development:**
```bash
python -m uvicorn fastapp:app --reload
```

The API will be available at `http://127.0.0.1:8000`

**Using Docker:**
```bash
# Build the image
docker build -t insurance-predictor .

# Run the container
docker run -p 8000:8000 insurance-predictor
```

## 📖 API Documentation

Once running, access the interactive API documentation at:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

### Endpoint

#### `POST /predict`

Predicts the insurance premium category for a user.

**Request Body:**
```json
{
  "age": 30,
  "weight": 70.0,
  "height": 1.75,
  "income_lpa": 10.0,
  "smoker": false,
  "city": "Pune",
  "occupation": "private_job"
}
```

**Response:**
```json
{
  "response": {
    "predicted_category": "Medium",
    "confidence": 0.95,
    "class_probabilities": {
      "Low": 0.1,
      "Medium": 0.85,
      "High": 0.05
    }
  }
}
```

**Occupation Options:**
- `retired`
- `freelancer`
- `student`
- `government_job`
- `business_owner`
- `unemployed`
- `private_job`

## 🧮 Feature Engineering

The model automatically computes:

1. **BMI (Body Mass Index)**: `weight / (height²)`
2. **Lifestyle Risk**: Based on smoking status and BMI
   - High: Smoker + BMI > 30
   - Medium: Smoker OR BMI > 27
   - Low: Neither condition
3. **Age Group**: 
   - Young: < 25
   - Adult: 25-44
   - Middle-aged: 45-59
   - Senior: 60+
4. **City Tier**: Classifies cities into Tier 1, 2, or 3

## 📊 Input Validation

All inputs are validated using Pydantic:
- Age: 1-119 years
- Weight: > 0 kg
- Height: 0.5-2.5 meters
- Income: > 0 LPA
- Smoker: Boolean
- City: String
- Occupation: Limited choices

## 🐛 Troubleshooting

### Common Issues

**ModuleNotFoundError: No module named 'pandas'**
```bash
pip install pandas scikit-learn fastapi uvicorn pydantic
```

**Port already in use**
```bash
# Use a different port
python -m uvicorn fastapp:app --port 8001
```

**Model file not found**
- Ensure `model.pkl` is in the same directory as `fastapp.py`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Sairaj Bhosale**
- GitHub: [@SairajBhosale](https://github.com/SairajBhosale)

## 🙏 Acknowledgments

- FastAPI for the amazing framework
- scikit-learn for ML capabilities
- The open-source community

---

This README is AI generated
