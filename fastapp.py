from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output, MODEL_VERSION, model


app = FastAPI()
  
        
@app.get("/")
def home():
    return {"message": "Insurance Premium Prediction API"}


@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "model_version": MODEL_VERSION,
        "model_loaded": model is not None
    }


@app.post('/predict')
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    
    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code = 200, content = {'predicted_category': prediction})
    except Exception as e:
        return JSONResponse(status_code = 500, content = {'error': str(e)})









# python -m uvicorn fastapp:app --reload
# python -m uvicorn fastapp:app
'''# Create new environment with Python 3.11 (more stable package support)
conda create -n myapp python=3.11 -y

# Activate it
conda activate myapp

# Install packages via conda (better dependency resolution)
conda install numpy pandas scikit-learn numba uvicorn fastapi -c conda-forge

# Then run your app
python -m uvicorn fastapp:app'''
# pip freeze > requirements.txt
# python -m venv myenv
# myenv\Scripts\Activate
# pip install -r requirements.txt
