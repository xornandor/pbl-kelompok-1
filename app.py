from flask import Flask
pbl = Flask(__name__)

@pbl.route("/")
def page():
    return "Aplikasi berjalan!"

if __name__ == "__main__":
    pbl.run(debug=True)