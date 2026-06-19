from flask import Blueprint, request, jsonify
from services.predictor import predict
from services.model_loader import models

stroke_bp = Blueprint("stroke",__name__)

@stroke_bp.route("/predict/stroke",methods=["POST"])
def predict_stroke():

    data = request.json

    result = predict(models["stroke"],data)

    return jsonify(result)