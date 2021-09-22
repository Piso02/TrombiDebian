from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required
from functools import wraps
from werkzeug.utils import secure_filename
from models import User, Personnel, Departement, ChecklistInfo

#sqlacodegen
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

#import models as dbHandler

#for uploaded images
UPLOAD_FOLDER = '/static/img/'
ALLOWED_EXTENSIONS = {'png','jpg','jpeg','gif'}


#config for database
app = Flask(__name__)
app.config['SECRET_KEY'] = "trombi"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://rojo:1234@localhost/trombi_vf'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

#allowing extension
def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#config for login
@app.route('/', methods=['POST', 'GET'])
def login():
    
    if request.method=='POST' and 'username' in request.form and 'password' in request.form:
        
        username = request.form['username']
        password = request.form['password']

        user = db.session.query(User).filter_by(username=username).first()

        return redirect(url_for('index')) 
    return render_template('login.html')

'''
#config for login required
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Vous devez vous connecter')
            return redirect(url_for('login'))
    return wrap 

#login simple user
@app.route('/login', methods=['GET', 'POST'])
def loginS():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'simple' or request.form['password'] != 'coldonly':
            error = 'Veuillez réessayer.'
        else:
            return redirect(url_for('indexS'))
    return render_template('indexSu.html', error=error)
'''

#interface commune Simple user
@app.route('/indexS')
def indexS():
    personnel = db.session.query(Personnel).all()
    return render_template('indexSu.html', personnel = personnel)

#interface commune
@app.route('/index')
#@login_required
def index():
    personnel = db.session.query(Personnel).all()    
    return render_template('index.html', personnel = personnel)


#interface admin with add function
@app.route('/admin')
def admin():
    personnel = db.session.query(Personnel).all() 
    return render_template('admin.html', personnel = personnel)

@app.route("/search", methods=['GET'])
def search():
    query = request.args.get("search") # here query will be the search inputs name
    personnel = db.session.query(Personnel.personnel_prenom.like(search)).all()
    return render_template("index.html", search=search, personnel=personnel)

#routage des départements (index)

#département ADM
@app.route('/ADM')
def ADM():
    return render_template('ADM.html')

#département AMOA
@app.route('/AMOA')
def AMOA():
    return render_template('AMOA.html')

#département AUDIT
@app.route('/AUDIT')
def AUDIT():
    return render_template('AUDIT.html')

#département BPOC
@app.route('/BPOC')
def BPOC():
    return render_template('BPOC.html')

#département BPORH
@app.route('/BPORH')
def BPORH():
    return render_template('BPORH.html')

#département CCIAL
@app.route('/CCIAL')
def CCIAL():
    return render_template('CCIAL.html')

#département COMM
@app.route('/COMM')
def COMM():
    return render_template('COMM.html')

#département FIN
@app.route('/FIN')
def FIN():
    return render_template('FIN.html')

#département INFO
@app.route('/INFO')
def INFO():
    return render_template('INFO.html')

#département ORGA
@app.route('/ORGA')
def ORGA():
    return render_template('ORGA.html')

#département QUALITE
@app.route('/QUALITE')
def QUALITE():
    return render_template('QUALITE.html')

#département RHC
@app.route('/RHC')
def RHC():
    return render_template('RHC.html')

#département RHI
@app.route('/RHI')
def RHI():
    return render_template('RHI.html')

#département DAF
@app.route('/DAF')
def DAF():
    return render_template('DAF.html')


#routage des départements (admin)

#département ADM
@app.route('/ADMa')
def ADMa():
    return render_template('ADMa.html')

#département AMOA
@app.route('/AMOAa')
def AMOAa():
    return render_template('AMOAa.html')

#département AUDIT
@app.route('/AUDITa')
def AUDITa():
    return render_template('AUDITa.html')

#département BPOC
@app.route('/BPOCa')
def BPOCa():
    return render_template('BPOCa.html')

#département BPORH
@app.route('/BPORHa')
def BPORHa():
    return render_template('BPORHa.html')

#département CCIAL
@app.route('/CCIALa')
def CCIALa():
    return render_template('CCIALa.html')

#département COMM
@app.route('/COMMa')
def COMMa():
    return render_template('COMMa.html')

#département FIN
@app.route('/FINa')
def FINa():
    return render_template('FINa.html')

#département INFO
@app.route('/INFOa')
def INFOa():
    return render_template('INFOa.html')

#département ORGA
@app.route('/ORGAa')
def ORGAa():
    return render_template('ORGAa.html')

#département QUALITE
@app.route('/QUALITEa')
def QUALITEa():
    return render_template('QUALITEa.html')

#département RHC
@app.route('/RHCa')
def RHCa():
    return render_template('RHCa.html')

#département RHI
@app.route('/RHIa')
def RHIa():
    return render_template('RHIa.html')

#département DAF
@app.route('/DAFa')
def DAFa():
    return render_template('DAFa.html')



#return adding interface Associe
@app.route('/addStaffA')
def addStaffA():
    departement = db.session.query(Departement).all() 
    return render_template('addStaffAssocie.html', departement=departement)

#adding methods
@app.route('/addStaffA', methods=['GET','POST'])
def addStaffA_post():
    
    matricule = request.form.get('matricule')
    personnel_nom = request.form.get('personnel_nom')
    personnel_prenom = request.form.get('personnel_prenom')
    fonction = request.form.get('fonction')
    personnel_mail = request.form.get('personnel_mail')
    personnel_phone = request.form.get('personnel_phone')
    departement_id = request.form.get('departement_id')

    personnel = Personnel(matricule=matricule, personnel_nom=personnel_nom, personnel_prenom=personnel_prenom, fonction=fonction, personnel_mail=personnel_mail, personnel_phone=personnel_phone, departement_id=departement_id)
    db.session.add(personnel)
    db.session.commit()

    flash('Le personnel a été ajouté avec succès!')
    
    return redirect(url_for('admin'))

#return adding interface consultant
@app.route('/addStaffC')
def addStaffC():
    departement = db.session.query(Departement).all() 
    return render_template('addStaffConsultant.html', departement=departement) 

#adding methods
@app.route('/addStaffC', methods=['GET','POST'])
def addStaffC_post():
    
    matricule = request.form.get('matricule')
    personnel_nom = request.form.get('personnel_nom')
    personnel_prenom = request.form.get('personnel_prenom')
    fonction = request.form.get('fonction')
    personnel_mail = request.form.get('personnel_mail')
    personnel_phone = request.form.get('personnel_phone')
    departement_id = request.form.get('departement_id')

    personnel = Personnel(matricule=matricule, personnel_nom=personnel_nom, personnel_prenom=personnel_prenom, fonction=fonction, personnel_mail=personnel_mail, personnel_phone=personnel_phone)
    db.session.add(personnel)
    db.session.commit()
    
    return redirect(url_for('admin'))

#update personnel Associe
@app.route("/personnel/<string:matricule>/update", methods=['GET','POST'])
def updateStaff(matricule):
    personnel = Personnel.query.get_or_404(matricule)
    if request.method == 'POST':
        personnel.matricule = request.form['matricule']
        personnel.personnel_nom = request.form['personnel_nom']
        personnel.personnel_prenom = request.form['personnel_prenom']
        personnel.fonction = request.form['fonction']
        personnel.personnel_mail = request.form['personnel_mail']
        personnel.personnel_phone = request.form['personnel_phone']
        departement.departement_nom = request.form['departement_nom']

        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('updateStaffAssocie.html', personnel=personnel)

@app.route('/listStaff')
def listStaff():
    personnel = db.session.query(Personnel).all() 
    return render_template('listStaff.html', personnel = personnel) 

@app.route('/toDisable')
def toDisable():
    return render_template('toDisable.html') 

@app.route('/disabled')
def disabled():
    return render_template('disabled.html')  

@app.route('/sheets')
def sheets():
    return render_template('sheets.html')

#adding sheets view
@app.route('/addSheets')
def addSheets():
    return render_template('addSheets.html')

#adding sheets function
@app.route('/addSheets', methods=['GET', 'POST'])
def addSheets_post():
    return redirect(url_for('sheets', habilitation=habilitation)

@app.route('/histoInfo')
def histoInfo():
    checklist_info = db.session.query(ChecklistInfo).all() 
    return render_template('histoInfo.html')

@app.route('/addHistoInfo')
def addHistoInfo():
    return render_template('addHistoInfo.html')

#adding histoInfo
@app.route('/addHistoInfo', methods=['GET','POST'])
def addHistoInfo_post():
    
    list_id = request.form.get('list_id')
    matricule = request.form.get('matricule')
    machine_ref = request.form.get('machine_ref')
    VPNServer_statut = request.form.get('VPNServer_statut')
    VPNBPOC_statut = request.form.get('VPNBPOC_statut')
    VPNBPORH_statut = request.form.get('VPNBPORH_statut')
    OCS_Statut = request.form.get('OCS_Statut')
    partage00AMI_statut = request.form.get('partage00AMI_statut')
    partage01Propales_statut = request.form.get('partage01Propales_statut')
    partage02ProjetMission_statut = request.form.get('partage02ProjetMission_statut')
    partage04OutilsInternes_statut = request.form.get('partage04OutilsInternes_statut')
    partage05Biblio_statut = request.form.get('partage05Biblio_statut')
    badge_statut = request.form.get('badge_statut')
    badge_num = request.form.get('badge_num')
    habilitation_statut = request.form.get('habilitation_statut')

    checklist_info = ChecklistInfo(list_id=list_id, matricule=matricule, machine_ref=machine_ref, VPNServer_statut=VPNServer_statut, VPNBPOC_statut=VPNBPOC_statut, VPNBPORH_statut=VPNBPORH_statut, OCS_Statut=OCS_Statut,  partage00AMI_statut=partage00AMI_statut, partage01Propales_statut=partage01Propales_statut, partage02ProjetMission_statut=partage02ProjetMission_statut, partage04OutilsInternes_statut=partage04OutilsInternes_statut, partage05Biblio_statut=partage05Biblio_statut, badge_statut=badge_statut, badge_num=badge_num, habilitation_statut=habilitation_statut)
    
    db.session.add(checklist_info)
    db.session.commit()
    
    return redirect(url_for('histoInfo'))



@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash ('Vous êtes déconnecté')
    return redirect(url_for('login'))


