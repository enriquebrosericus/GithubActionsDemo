from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # slurp in .evn

app = Flask(__name__)

# added a comment
# another comment
# comments rule!


@app.route("/<random_string>")
def return_backwards_string(random_string):
    return "".join(reversed(random_string))


@app.route("/get-mode")
def get_mode():
    return os.environ.get("MODE")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
