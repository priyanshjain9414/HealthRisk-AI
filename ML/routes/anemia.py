from flask import Blueprint, request, jsonify
from services.predictor import predict
from services.model_loader import models

anemia_bp = Blueprint("anemia",__name__)

@anemia_bp.route("/predict/anemia",methods=["POST"])
def predict_anemia():

    data = request.json

    result = predict(models["anemia"],data)

    return jsonify(result)