from flask import Flask, render_template, request, jsonify
from chat import get_response
import requests
import os
import logging
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")

metrics = PrometheusMetrics(app)

metrics.info("app_info", "App Info for the app", version="1.0.0")

@app.route("/",methods=["GET"])
def index_get():
    return render_template("base.html")


@app.route("/predict",methods=["POST"])
def predict():
    text= request.get_json().get("message")
    response = get_response(text)
    message = {"answer":response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)