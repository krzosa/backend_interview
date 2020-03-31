from flask import Flask, request, jsonify
import utilityFunctions as util

app = Flask(__name__)
openapi = util.loadYAMLfile("openapi.yaml")


@app.route("/")
def hello():
    return openapi


@app.route("/schemas", methods = ["POST"])
def addSchema():
    print(request.form)
    return "data has been added to repo"


@app.route("/schemas/<schemaHash>")
def getSchema(schemaHash):
    return "successful operation"


def main():
    app.run(port=9292)


if __name__ == "__main__":
    main()
