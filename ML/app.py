from flask import Flask

from routes.diabetes import diabetes_bp
from routes.heart import heart_bp
from routes.kidney import kidney_bp
from routes.liver import liver_bp
from routes.stroke import stroke_bp
from routes.anemia import anemia_bp
from routes.thyroid import thyroid_bp

app = Flask(__name__)

app.register_blueprint(diabetes_bp)
app.register_blueprint(heart_bp)
app.register_blueprint(kidney_bp)
app.register_blueprint(liver_bp)
app.register_blueprint(stroke_bp)
app.register_blueprint(anemia_bp)
app.register_blueprint(thyroid_bp)

@app.route("/")
def home():
    return {"message": "HealthRisk AI API Running"}

if __name__ == "__main__":
    app.run(debug=True)