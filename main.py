from flask import Flask, request, jsonify
import utilityFunctions as util

app = Flask(__name__)
openapi = util.loadYAMLfile("openapi.yaml")


@app.route("/")
def hello():
    return openapi


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
