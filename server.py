from flask import Flask, render_template
import random
app = Flask(__name__)
app.secret_key = 'rocky'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['POST'])
def results():
    print(request.form)
    session['our_choice'] = request.form['our_choice']
    print(session)
    random_number = random.randint(0,2)
    choices = ['Rock', 'Paper', 'Scissors']
    opponent_choices = choices[random_number]
    #opponent_choices = random.choice(['Rock','Paper','Scissors'])
    print(opponent_choices)
    session['opponent_choices'] = opponent_choices

    if (our_choice == 'Paper' and opponent_choices == 'Scissors'):
        if 

    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)