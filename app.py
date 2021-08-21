from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_appbuilder import SQLA, AppBuilder
from models import *
from functools import wraps
import models as dbHandler

#engine = create_engine('mysql+pymysql://rojo:1234@localhost/trombi_model')

app = Flask(__name__)
app.config['SECRET_KEY'] = "trombi"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://rojo:1234@localhost/trombi_model'

db = SQLAlchemy(app)



def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Vous devez vous connecter')
            return redirect(url_for('login'))
    return wrap 
 
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash ('Vous êtes déconnecté')
    return redirect(url_for('login'))



@app.route('/', methods=['POST', 'GET'])
def login():
    
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        entry = users(username=username, password=password)
        db.session.add(entry)
        db.session.commit()    
    return render_template('login.html')


@app.route('/index')
#@login_required
def index():
    return render_template('index.html')
