from flask import Blueprint, request, jsonify
from services.predictor import predict
from services.model_loader import models

heart_bp = Blueprint("heart",__name__)

@heart_bp.route("/predict/heart",methods=["POST"])
def predict_heart():

    data = request.json

    result = predict(models["heart"],data)

    return jsonify(result)