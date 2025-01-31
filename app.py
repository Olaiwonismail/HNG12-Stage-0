from flask import Flask,jsonify,Response,make_response
from flask_cors import CORS
from datetime import datetime,timezone

app = Flask(__name__)

CORS(app)


@app.route('/',methods = ['GET','POST'])
def home():
    email = "olaiwonismail@gmail.com"
    date = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    github_url = "https://github.com/Olaiwonismail/HNG12-Stage-0"
    data = {
        "email":email,
        "current_datetime":date,
        "github_url" : github_url
    }
  
    return data


if __name__ == '__main__':
    app.json.sort_keys = False
    app.run(debug=True)