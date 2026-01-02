from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# --------------------------------------------------
# Load trained model (RandomForest with 7 features)
# --------------------------------------------------
with open("forest_model.pkl", "rb") as f:
    model = pickle.load(f)

print("✅ Model loaded successfully")

# --------------------------------------------------
# Home route
# --------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")

# --------------------------------------------------
# Prediction route
# --------------------------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        batting_team = data["batting_team"]
        bowling_team = data["bowling_team"]
        runs = int(data["runs"])
        wickets = int(data["wickets"])
        overs = float(data["overs"])
        runs_last_5 = int(data["runs_last_5"])
        wickets_last_5 = int(data["wickets_last_5"])

        # --------------------------------------------------
        # TEAM ENCODING (MUST MATCH TRAINING)
        # --------------------------------------------------
        teams = [
            "Chennai Super Kings",
            "Delhi Capitals",
            "Kings XI Punjab",
            "Kolkata Knight Riders",
            "Mumbai Indians",
            "Rajasthan Royals",
            "Royal Challengers Bangalore",
            "Sunrisers Hyderabad"
        ]

        batting_encoded = [1 if team == batting_team else 0 for team in teams]
        bowling_encoded = [1 if team == bowling_team else 0 for team in teams]

        # --------------------------------------------------
        # FINAL FEATURE VECTOR (EXACT ORDER)
        # --------------------------------------------------
        features = np.array(
            batting_encoded +
            bowling_encoded +
            [runs, wickets, overs, runs_last_5, wickets_last_5]
        ).reshape(1, -1)

        prediction = model.predict(features)[0]

        return jsonify({
            "predicted_score": int(round(prediction))
        })

    except Exception as e:
        return jsonify({"error": str(e)})

# --------------------------------------------------
# Run server
# --------------------------------------------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)



