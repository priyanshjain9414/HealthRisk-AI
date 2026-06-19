import pandas as pd

def predict(model, data):

    df = pd.DataFrame([data])

    prediction = int(model.predict(df)[0])

    probability = round(model.predict_proba(df)[0][1] * 100,2)
    
    if probability >= 70:
        risk = "High"

    elif probability >= 40:
        risk = "Moderate"

    else:
        risk = "Low"

    return {
        "prediction": prediction,
        "probability": probability,
        "risk_level": risk
    }