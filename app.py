from pathlib import Path

import pandas as pd
from flask import Flask, request, render_template
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "breast-cancer-data.csv"

FEATURES = [
    "radius_mean",
    "texture_mean",
    "perimeter_mean",
    "smoothness_mean",
    "compactness_mean"
]


# -----------------------------
# Train Model Once
# -----------------------------

df = pd.read_csv(DATA_PATH)

df["diagnosis"] = df["diagnosis"].map({
    "M": 1,
    "B": 0
})

X = df[FEATURES]
y = df["diagnosis"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=500,
    n_jobs=-1,
    random_state=42
)

model.fit(X_train, y_train)

accuracy = accuracy_score(
    y_test,
    model.predict(X_test)
)


# -----------------------------
# Home Page
# -----------------------------

@app.route("/")
def home():
    return render_template(
        "index.html",
        query="",
        accuracy=accuracy * 100
    )


# -----------------------------
# Prediction
# -----------------------------

@app.route("/predict", methods=["POST"])
def cancerpredict():

    try:

        input_query1 = float(request.form["query1"])
        input_query2 = float(request.form["query2"])
        input_query3 = float(request.form["query3"])
        input_query4 = float(request.form["query4"])
        input_query5 = float(request.form["query5"])

        data = [[
            input_query1,
            input_query2,
            input_query3,
            input_query4,
            input_query5
        ]]

        new_df = pd.DataFrame(
            data,
            columns=FEATURES
        )

        prediction = model.predict(new_df)[0]

        probability = model.predict_proba(new_df)[0][1]

        if prediction == 1:

            output = "The model predicts a possible malignant result."

            output1 = "Confidence: {:.2f}%".format(
                probability * 100
            )

        else:

            output = "The model predicts a benign result."

            output1 = "Confidence: {:.2f}%".format(
                (1 - probability) * 100
            )

        return render_template(
            "index.html",
            query=output + "\n" + output1,
            query1=input_query1,
            query2=input_query2,
            query3=input_query3,
            query4=input_query4,
            query5=input_query5,
            accuracy=accuracy * 100
        )

    except (ValueError, KeyError):

        return render_template(
            "index.html",
            query="Please enter valid numerical values.",
            accuracy=accuracy * 100
        )


if __name__ == "__main__":
    app.run(debug=True)