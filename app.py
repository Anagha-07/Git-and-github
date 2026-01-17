from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Atlas connection
MONGO_URI = "mongodb+srv://username:password@cluster0.gdebain.mongodb.net/flaskDB?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client["flaskDB"]
collection = db["users"]

# -------- API ROUTE --------
@app.route("/api")
def api():
    with open("data.json", "r") as file:
        data = json.load(file)
    return jsonify(data)

# -------- FORM PAGE --------
@app.route("/", methods=["GET", "POST"])
def form():
    error = None
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]

            collection.insert_one({
                "name": name,
                "email": email
            })

            return render_template("success.html")

        except Exception as e:
            error = str(e)

    return render_template("form.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)
