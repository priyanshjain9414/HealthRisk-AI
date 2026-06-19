from flask import Blueprint, request, jsonify
from services.predictor import predict
from services.model_loader import models

liver_bp = Blueprint("liver",__name__)

@liver_bp.route("/predict/liver",methods=["POST"])
def predict_liver():

    data = request.json

    result = predict(models["liver"],data)

    return jsonify(result)