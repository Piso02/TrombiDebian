from flask import *
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from models import User, Personnel

#sqlacodegen
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

#import models as dbHandler

#engine = create_engine('mysql+pymysql://rojo:1234@localhost/trombi_model')

app = Flask(__name__)
app.config['SECRET_KEY'] = "trombi"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://rojo:1234@localhost/trombi_model'

db = SQLAlchemy(app)



@app.route('/', methods=['POST', 'GET'])
def login():
    '''
    name = 'rrasoamahefa'
    user = db.session.query(User).filter_by(username=name).first_or_404()
    '''
    if request.method=='POST' and 'username' in request.form and 'password' in request.form:
        
        username = request.form['username']
        password = request.form['password']

        user = db.session.query(User).filter_by(username=username).first()

        return redirect(url_for('index')) 
    return render_template('login.html')



def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Vous devez vous connecter')
            return redirect(url_for('login'))
    return wrap 


@app.route('/index')
#@login_required
def index():
    id = 'personnel.Matricule'
    personnel = db.session.query(Personnel).filter_by(Matricule=id).first()
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')
 
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash ('Vous êtes déconnecté')
    return redirect(url_for('login'))


