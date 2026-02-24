from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "My First python DevOps Project"}

app.run(host="0.0.0.0", port=5000)
if __name__ == "__main__":

