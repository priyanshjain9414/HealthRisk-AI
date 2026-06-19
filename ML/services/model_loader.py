import joblib

models = {
    "diabetes": joblib.load("trained_models/diabetes_model.pkl"),
    "heart": joblib.load("trained_models/heart_disease_model.pkl"),
    "kidney": joblib.load("trained_models/kidney_model.pkl"),
    "liver": joblib.load("trained_models/liver_model.pkl"),
    "stroke": joblib.load("trained_models/stroke_model.pkl"),
    "anemia": joblib.load("trained_models/anemia_model.pkl"),
    "thyroid": joblib.load("trained_models/thyroid_model.pkl")
}