from flask import Blueprint, request, jsonify
from services.predictor import predict
from services.model_loader import models

thyroid_bp = Blueprint("thyroid",__name__)

@thyroid_bp.route("/predict/thyroid",methods=["POST"])
def predict_thyroid():

    data = request.json

    result = predict(models["thyroid"],data)

    return jsonify(result)
