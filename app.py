from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    operation = data["operation"]
    a = data.get("a", 0)
    b = data.get("b", 0)

    try:
        if operation == "add":
            result = a + b
        elif operation == "sub":
            result = a - b
        elif operation == "mul":
            result = a * b
        elif operation == "div":
            result = a / b if b != 0 else "Error"
        elif operation == "sqrt":
            result = math.sqrt(a)
        elif operation == "pow":
            result = math.pow(a, b)
        else:
            result = "Invalid Operation"

        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
