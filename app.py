from flask import Flask, request, jsonify

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def index():
    return 'Main Page'


@app.route('/test', methods=['POST'])
def string_to_cut():
    req_json = request.get_json()
    if req_json is not None:
        if "string_to_cut" in req_json:
            return_string = string_cutter(req_json["string_to_cut"])
    return jsonify({"return_string": return_string})


def string_cutter(the_string):
    length = len(the_string)
    final_string = ""
    if the_string == "":
        return ""
    for cnt in range(2, length, 3):
        final_string += the_string[cnt]
    return final_string


if __name__ == '__main__':
    app.run(port=5000)
