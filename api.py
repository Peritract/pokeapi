from flask import Flask, request, jsonify

import pokefunctions

api = Flask(__name__)


@api.route("/", methods=["GET"])
def index():
    return jsonify({
        "message": "Welcome to the pokemon API!"
    })


@api.route('/pokemon', methods = ['GET', 'POST'])
def pokemon() -> list | dict:
    """Returns a list of pokemon, or adds a new one and returns it."""
    if (request.method == 'GET'):
        try:
            pokemon = pokefunctions.get_all()
            return pokemon
        except Exception as err:
            return jsonify({"error": True,
                            "Message": "Unable to retrieve pokemon"}), 500
    elif (request.method == 'POST'):
        data = request.json
        new_pokemon = pokefunctions.add_one(data)
        return jsonify(new_pokemon), 201


if __name__ == "__main__":
    api.run(debug=True, port=5050)