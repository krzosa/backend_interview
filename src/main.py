from flask import Flask, request, jsonify
import utilityFunctions as util
from dataStructure import dataStructure

app = Flask(__name__)
openapi = util.loadYAMLfile("openapi.yaml")
database = dataStructure()


@app.route("/schemas", methods = ["POST"])
def addSchema():
    if request.is_json:
        hashid = database.addSchema(request.get_json())
        return jsonify({"hash": hashid})
    else:
        return 404


@app.route("/schemas/<hashid>")
def getSchema(hashid):
    schema = database.retrieveSchema(hashid)
    return jsonify(schema.decode("utf-8"))


def main():
    app.run(port=9292)


if __name__ == "__main__":
    main()
