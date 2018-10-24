from .cards import cards, shuffled_cards
from app import ask
from .mechanics import DECK, final_score, DECK_SIZE
from .dialogue import choose_a_card

from flask_ask import statement, question
from flask_ask import session as ask_session, request as ask_request, context
from flask import render_template


@ask.launch
def start_skill():
    output = render_template('welcome')
    ask_session.attributes['GAME_RUNNING'] = 0
    ask_session.attributes['SCORE'] = 0
    ask_session.attributes['DECK'] = DECK
    ask_session.attributes['DECK_SIZE'] = DECK_SIZE
    ask_session.attributes['CARD_COUNT'] = 0
    ask_session.attributes['last_speech'] = output
    return question(output).reprompt(ask_session.attributes['last_speech'])



@ask.intent('ready')
def start_game():
    if ask_session.attributes['GAME_RUNNING'] == 1:
        output = render_template('playing')
        ask_session.attributes['last_speech'] = output
        return question(output)
    else:
        output = render_template('ready')
        ask_session.attributes['last_speech'] = output
        return question(output)





@ask.intent('zener')
def play_game(guess):
    ask_session.attributes['GAME_RUNNING'] = 1
    score = ask_session.attributes['SCORE']
    game_deck = ask_session.attributes['DECK']
    deck_size = ask_session.attributes['DECK_SIZE']
    card_count = ask_session.attributes['CARD_COUNT']
    if guess is None or guess not in ['star', 'cross', 'square', 'waves', 'circle']:
        output = render_template('error')
        ask_session.attributes['last_speech'] = output
        return question(output)
    while card_count < (deck_size - 1):
        if guess == 'ready':
            output = render_template('ready')
            ask_session.attributes['last_speech'] = output
            return question(output)
        choose_card = choose_a_card()
        output = render_template('game', choose_card=choose_card)
        ask_session.attributes['last_speech'] = output
        #print(game_deck[card_count], guess, "score = ", score)
        if guess == game_deck[card_count]:
            score += 1
        card_count += 1
        ask_session.attributes['CARD_COUNT'] = card_count
        ask_session.attributes['SCORE'] = score
        ask_session.attributes['last_speech'] = output
        return question(output)
    score = final_score(score)
    output = render_template('score', score=score)
    return statement(output)


@ask.intent('testMode')
def testmode():
    ask_session.attributes['DECK_SIZE'] = 5
    output = render_template('ready')
    ask_session.attributes['last_speech'] = output
    return question(output)



@ask.intent('AMAZON.FallbackIntent')
def fallback():
    output = render_template('error')
    ask_session.attributes['last_speech'] = output
    return question(output)

@ask.intent('AMAZON.RepeatIntent')
def repeat():
    repeat_speech = ask_session.attributes['last_speech']
    return question(repeat_speech)

@ask.intent('AMAZON.HelpIntent')
def help():
    output = render_template('help')
    ask_session.attributes['last_speech'] = output
    return question(output)

@ask.intent('AMAZON.CancelIntent')
@ask.intent('AMAZON.StopIntent')
@ask.intent('AMAZON.NoIntent')
def goodbye():
    return statement('Good bye')



@ask.session_ended
def session_ended():
    return "{}", 200