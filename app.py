import random
from flask import Flask, render_template, request, jsonify
from wsgiref import simple_server
import gunicorn
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def play():
    cpu = cpuSetup()
    if request.method == 'POST':
        player = request.form['playerOption']
        #print(player)
        if player == cpu:
            return render_template('index.html', result="Tie", player="Same Choice", cpu="Same Choice")
        elif player == 'rock':
            if cpu == 'scissor':
                return render_template('index.html', result="Rock smashes Scissor", player="Wins", cpu="Loses")
            else:
                return render_template('index.html', result="Paper covers Rock", player="Loses", cpu="Wins")
        elif player == 'scissor':
            if cpu == 'paper':
                return render_template('index.html', result="Scissor cuts Paper", player="Wins", cpu="Loses")
            else:
                return render_template('index.html', result="Rock smashes Scissor", player="Loses", cpu="Wins")
        elif player == 'paper':
            if cpu == 'rock':
                return render_template('index.html', result="Paper covers Rock", player="Wins", cpu="Loses")
            else:
                return render_template('index.html', result="Scissor cuts Paper", player="Loses", cpu="Wins")
    else:
        return render_template('index.html', error="Something went wrong")


def cpuSetup():
    cpuChoice = ['rock', 'paper', 'scissor']
    randomChoice = random.choice(cpuChoice)
    return randomChoice


"""def playerSetup():
    playerChoice = input('Enter your selection:').lower()
    return playerChoice"""

if __name__ == '__main__':
    ###############Below line are used to remove flask warning of wsgi##################
    # host='0.0.0.0'
    # app.run(debug=True,port=port)
    # httpd=simple_server.make_server(host,port,app)
    # httpd.serve_forever
    ######################################
    app.run(debug=True)
