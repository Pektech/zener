from .cards import cards, shuffled_cards
from app import ask
from .mechanics import DECK, final_score

from flask_ask import statement, question
from flask_ask import session as ask_session, request as ask_request, context
from flask import render_template


@ask.launch
def start_skill():
    output = render_template('welcome')
    ask_session.attributes['GAME_RUNNING'] = 0
    ask_session.attributes['SCORE'] = 0
    ask_session.attributes['DECK'] = DECK
    ask_session.attributes['CARD_COUNT'] = 0
    ask_session.attributes['last_speech'] = output
    return question(output).reprompt(ask_session.attributes['last_speech'])



@ask.intent('ready')
def start_game():
    if ask_session.attributes['GAME_RUNNING'] == 1:
        output = render_template('playing')
        return question(output)
    else:
        output = render_template('ready')
        return question(output)





@ask.intent('zener')
def play_game(guess):
    ask_session.attributes['GAME_RUNNING'] = 1
    score = ask_session.attributes['SCORE']
    game_deck = ask_session.attributes['DECK']
    card_count = ask_session.attributes['CARD_COUNT']
    if guess is None or guess not in ['star', 'cross', 'square', 'waves', 'circle']:
        output = render_template('error')
        return question(output)
    while card_count < 24:
        if guess == 'ready':
            output = render_template('ready')
            return question(output)
        output = render_template('game')

        print(game_deck[card_count], guess, "score = ", score)
        if guess == game_deck[card_count]:
            score += 1
        card_count += 1
        ask_session.attributes['CARD_COUNT'] = card_count
        ask_session.attributes['SCORE'] = score
        return question(output)
    score = final_score(score)
    output = render_template('score', score=score)
    return statement(output)



@ask.intent('AMAZON.FallbackIntent')
def fallback():
    return question("whoop whoop fallback")



@ask.intent('AMAZON.HelpIntent')
def help():
    output = render_template('help')
    return question(output)

@ask.session_ended
def session_ended():
    return "{}", 200