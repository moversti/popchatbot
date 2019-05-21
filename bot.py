from flask import Flask, request,jsonify
from eliza import eliza

app = Flask(__name__)
therapist = eliza.eliza()


@app.route('/eliza')
def eliza():
    response = therapist.respond(request.args.get('msg', ''))
    return jsonify(response=response)


if __name__ == "__main__":
    app.run()
