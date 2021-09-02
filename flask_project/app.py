from flask import Flask, request, render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

# db = database.name

# db.drop_all()
@app.route('/')

@app.route('/games', methods=['GET', 'POST'])
def games():
    if request.method == 'POST':
        return 'Add a game here'
    else:
        return 'Look for a game?'

@app.route('/reviews', methods=['GET', 'POST'])
def games():
    if request.method == 'POST':
        return 'Add a review here'
    else:
        return 'Find the review'

if __name__=='__main__':
    app.run(debug=True, host=("0.0.0.0"))