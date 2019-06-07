from flask import Flask, request, Response
from chatterbot import ChatBot

from eli import eliza

app = Flask(__name__)
therapist = eliza.eliza()
chatter = ChatBot('Chatter')

@app.route('/eliza')
def eliza():
    response = therapist.respond(request.args.get('msg', ''))
    resp = Response(response)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
	
@app.route('/chatter')
def chatter():
    response = chatter.get_response(request.args.get('msg', ''))
    resp = Response(response)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == "__main__":
    app.run()
