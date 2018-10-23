from .cards import cards, shuffled_cards
from app import ask

from flask_ask import statement, question
from flask_ask import session as ask_session, request as ask_request, context
from flask import render_template


@ask.launch
def start_skill():
    output = render_template('welcome')
    ask_session.attributes['last_speech'] = output
    return question(output).reprompt(ask_session.attributes['last_speech'])




@ask.intent('AMAZON.HelpIntent')
def help():
    output = render_template('help')
    return question(output)