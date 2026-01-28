
from flask import Flask
from flask_cors import CORS

# Import blueprints
from routes.report import report_bp
from routes.upload import upload_bp

app = Flask(__name__)
CORS(app)

# Register routes
app.register_blueprint(report_bp)
app.register_blueprint(upload_bp)

@app.route("/")
def health_check():
    return {"status": "Backend running successfully"}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
