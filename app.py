from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
  {
    "ID":1,
    "Title":"Data Scientist",
    "location":"Remote",
    "Salary":"$120000"
  },
  {"ID":2,
   "Title":"Data Analyst",
   "location":"North Carolina,USA",
   "Salary":"$10000",
    
  },
  {
    "ID":3,
    "Title":"Frontend Developer",
    "location":"New York",
    # "Salary":"$40000"
  },
  {
    "ID":4,
    "Title":"Backend Developer",
    "location":"Accra",
    "Salary":"GHS 200000"
  }
]


@app.route("/")
def hello_world():
  return render_template("home.html",jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)