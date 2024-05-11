from flask import Flask, request
import json

from src import Core, PrBaseException


app = Flask(__name__)
core = Core()


@app.route("/register/write", methods=["POST"])
def write_to_register():
    data: dict[str, str] = json.loads(request.data)
    try:
        core.registers.write(data)
        response = "OK", 200

    except PrBaseException as e:
        response = e.message, e.status

    except Exception as e:
        response = "Internal Server Error", 500

    return response


@app.route("/register/read", methods=["GET"])
def read_register():
    data = core.registers.read
    return data


@app.route("/memory/write", methods=["POST"])
def write_to_memory():
    data = json.loads(request.data)
    try:
        core.memory.write(data["data"])
        response = "OK", 200

    except PrBaseException as e:
        response = e.message, e.status

    return response


@app.route("/memory/read", methods=["GET"])
def read_memory():
    data = core.memory.read
    res = {"data": data}
    return res


@app.route("/core/instruction", methods=["POST"])
def execute_instructions():
    try:
        core.execute_instruction()
        response = "OK", 200

    except PrBaseException as e:
        response = e.message, e.status

    return response


@app.route("/core/compile", methods=["POST"])
def compile_instructions():
    try:
        data: dict[str, list[str]] = json.loads(request.data)
        core.compile(data["instructions"])
        return "OK", 200
    
    except PrBaseException as e:
        return e.message, e.status
    
    except:
        return "Internal Server Error", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
