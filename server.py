import json
from datetime import datetime
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html', club=club, competitions=competitions)
    except IndexError:
        return render_template('index.html', message="Unknown email, please indicate a registered email")


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    try:
        club[f"{competition['name']}_history"]
    except KeyError:
        club[f"{competition['name']}_history"] = 0
    placesRequired = int(request.form['places'])
    if datetime.now() > datetime.strptime(competition['date'], "%Y-%m-%d %H:%M:%S"):
        flash("ERROR : you can t purchase places, it's a past competition")
    else:
        if placesRequired + club[f"{competition['name']}_history"] < 13:
            if placesRequired > int(club['points']):
                flash('ERROR : your points balance is too low')
            else:
                if placesRequired > int(competition['numberOfPlaces']):
                    flash('ERROR : you can t book more places than the number available')
                else:
                    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
                    club[f"{competition['name']}_history"] += placesRequired
                    flash('Great-booking complete!')
        else:
            flash('ERROR : You can only reserve a maximum of 12 places')
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/displayBoard', methods=['GET'])
def display_board():
    return render_template('display_board.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
