from flask import Blueprint, request, jsonify
from services.predictor import predict
from services.model_loader import models

diabetes_bp = Blueprint("diabetes",__name__)

@diabetes_bp.route("/predict/diabetes",methods=["POST"])
def predict_diabetes():

    data = request.json

    result = predict(models["diabetes"],data)

    return jsonify(result)