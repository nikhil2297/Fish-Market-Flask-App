from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np 
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open("./fish_pred_model.pkl", 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict() :
    data = request.get_json()
    length1 = int(data.get("length1"))
    length2 = int(data.get("length2"))
    length3 = int(data.get("length3"))
    height = int(data.get("height"))
    width = int(data.get("width"))
    weight = int(data.get("weight"))

    scaler = StandardScaler()
    X_new = np.array([[weight ,length1, length2, length3, height, width]])

    print("X_new: ", X_new) 

    X_new_scaled = scaler.fit_transform(X_new)

    prediction = model.predict(X_new_scaled)[0]
    species_names = {0: "Bream", 1: "Roach", 2: "Whitefish", 3: "Parkki", 4: "Perch", 5: "Pike", 6: "Smelt"}

    return jsonify({"predicted_species": species_names[int(prediction)]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)