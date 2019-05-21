from flask import Flask, request, Response
from eli import eliza

app = Flask(__name__)
therapist = eliza.eliza()


@app.route('/eliza')
def eliza():
    response = therapist.respond(request.args.get('msg', ''))
    resp = Response(response)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == "__main__":
    app.run()
