from flask import Flask, render_template, jsonify
from database import job_listing


app = Flask(__name__)
JOBS = job_listing()


@app.route("/")
def hello_world():
  return render_template("home.html",jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)