from flask import Flask, render_template, request, redirect
from queue_manager import ClinicQueue

app = Flask(__name__)

clinic = ClinicQueue()

@app.route("/")
def home():
    queue = clinic.get_queue()
    return render_template("index.html", queue=queue, served=clinic.served_today)

@app.route("/add", methods=["GET", "POST"])
def add_patient():
    if request.method == "POST":
        name = request.form["name"]
        clinic.add_patient(name)
        return redirect("/")
    return render_template("add_patient.html")

@app.route("/serve")
def serve():
    clinic.serve_patient()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5001)