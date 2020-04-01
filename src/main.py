from flask import Flask, request, jsonify
import utilityFunctions as util
from dataStructure import dataStructure
from jsonschema import validate


app = Flask(__name__)

openapi = util.loadYAMLfile("openapi.yaml")
database = dataStructure()

@app.route("/schemas", methods = ["POST"])
def addSchema():
    validationSchema = openapi['paths']['/schemas/']['post']['requestBody']

    try:
        if not request.is_json:
            raise Exception
        validate(
            instance=request.get_json(), 
            schema=validationSchema['content']['application/json']['schema']
        )
    except:
        return "invalid request", 400
    
    hashid = database.addSchema(request.get_json())
    return jsonify({"hashlink": hashid})


@app.route("/schemas/<hashid>")
def getSchema(hashid):
    schema = database.retrieveSchema(hashid)
    if schema != None:
        return jsonify(schema.decode("utf-8"))
    return "schema not found", 404


def main():
    app.run(port=9292)


if __name__ == "__main__":
    main()
