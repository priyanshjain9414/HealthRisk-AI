from flask import Blueprint, request, jsonify
from services.predictor import predict
from services.model_loader import models

kidney_bp = Blueprint("kidney",__name__)

@kidney_bp.route("/predict/kidney",methods=["POST"])
def predict_kidney():

    data = request.json

    result = predict(models["kidney"],data)

    return jsonify(result)