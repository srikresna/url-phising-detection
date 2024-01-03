from feature import FeatureExtractor
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics
import warnings
import pickle
warnings.filterwarnings('ignore')

file = open("models/model_final.pkl", "rb")
gbc = pickle.load(file)
file.close()


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        obj = FeatureExtractor(url)
        x = np.array(obj.extract_features()).reshape(1, 8)

        pred = gbc.predict(x)[0]
        if pred == 0:
            prediction = "Save"
        else:
            prediction = "Not safe/Phising"
            
        return render_template("index.html", xx=prediction, url=url)

if __name__ == "__main__":
    app.run(debug=True)
