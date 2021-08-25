# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Cursu(Base):
    __tablename__ = 'cursus'

    Cursus_id = Column(String(10), primary_key=True)
    Poste = Column(String(100))
    Cursus_DateDebut = Column(Date)
    Cursus_DateFin = Column(Date)
    Entreprise = Column(String(100))

    personnel = relationship('Personnel', secondary='cursus_personnel')


class Departement(Base):
    __tablename__ = 'departement'

    Departement_id = Column(String(4), primary_key=True)
    Departement_Nom = Column(String(25))
    Departement_AdresseGroupE = Column(String(40))
    Departement_Partage = Column(String(40))


class User(Base):
    __tablename__ = 'users'

    username = Column(String(30), primary_key=True)
    password = Column(String(30))


class Personnel(Base):
    __tablename__ = 'personnel'

    Matricule = Column(String(10), primary_key=True)
    Personnel_Nom = Column(String(30))
    Personnel_Prenom = Column(String(30))
    Fonction = Column(String(100))
    Personnel_Statut = Column(String(20))
    Personnel_Mail = Column(String(50))
    Personnel_phone = Column(String(20))
    Departement_id = Column(ForeignKey('departement.Departement_id'), nullable=False, index=True)

    Departement = relationship('Departement')


class ChecklistInfo(Base):
    __tablename__ = 'checklist_info'

    List_id = Column(String(5), primary_key=True)
    Machine_Ref = Column(String(20))
    VPNServer_Statut = Column(String(3))
    VPNBPOC_Statut = Column(String(3))
    VPNBPORH_Statut = Column(INTEGER(3))
    OCS_Statut = Column(String(3))
    Partage00AMI_Statut = Column(String(3))
    Partage01Propales_Statut = Column(String(3))
    Partage02ProjetMission_Statut = Column(String(3))
    Partage04OutilsInternes_Statut = Column(String(3))
    Partage05Biblio_Statut = Column(String(3))
    Partage06Qualite_Statut = Column(String(3))
    Badge_Statut = Column(String(3))
    Badge_Num = Column(String(8))
    Habilitation_Statut = Column(String(10))
    Matricule = Column(ForeignKey('personnel.Matricule'), nullable=False, index=True)

    personnel = relationship('Personnel')


t_cursus_personnel = Table(
    'cursus_personnel', metadata,
    Column('Cursus_id', ForeignKey('cursus.Cursus_id'), primary_key=True, nullable=False),
    Column('Matricule', ForeignKey('personnel.Matricule'), primary_key=True, nullable=False, index=True)
)


class Habilitation(Base):
    __tablename__ = 'habilitation'

    Habilitation_num = Column(String(5), primary_key=True)
    Habilitation_Statut = Column(String(12))
    Habilitation_nom = Column(String(100))
    Habilitation_DateDemande = Column(Date)
    Demandeur_Nom = Column(String(60))
    Date_Arrivee = Column(Date)
    Date_Depart = Column(Date)
    Badge_StatutCS = Column(String(12))
    BesoinMateriel_Statut = Column(String(3))
    PCFixe_Statut = Column(String(3))
    Portable_Statut = Column(String(3))
    AutreMatériel = Column(String(100))
    AncienUtilisateur = Column(String(100))
    Note = Column(String(100))
    Mail_Statut = Column(String(12))
    Mail_Extension = Column(String(20))
    Personnel_AdresseGroupE = Column(String(30))
    AutreAdresse = Column(String(40))
    Mail_Routage = Column(String(50))
    Routage_DateDebut = Column(Date)
    Routage_DateFin = Column(Date)
    ReponseAuto_Statut = Column(String(3))
    ReponseAuto_Contenu = Column(String(250))
    ReponseAutoSuppr_Statut = Column(String(3))
    ReponseAutoSuppr_Date = Column(Date)
    Repertoire_Statut = Column(String(3))
    AutrePartage = Column(String(40))
    Repertoire_Detail = Column(String(40))
    Libertempo_Statut = Column(String(3))
    Demandeur_Libertempo = Column(String(60))
    GLPI_Statut = Column(String(3))
    Timesheet_Statut = Column(String(3))
    Demandeur_GT = Column(String(60))
    Quadra_Statut = Column(String(3))
    SageCompta_Statut = Column(String(3))
    SageRH_Statut = Column(String(3))
    Matricule = Column(ForeignKey('personnel.Matricule'), nullable=False, index=True)

    personnel = relationship('Personnel')


class HistoriqueHabilitation(Base):
    __tablename__ = 'historique_habilitation'

    Historique_id = Column(String(10), primary_key=True)
    Historique_date = Column(Date)
    Habilitation_Motif = Column(String(100))
    Habilitation_num = Column(ForeignKey('habilitation.Habilitation_num'), nullable=False, index=True)

    habilitation = relationship('Habilitation')


class SauvegardeMail(Base):
    __tablename__ = 'sauvegarde_mail'

    Sauvegarde_id = Column(String(5), primary_key=True)
    Sauvegarde_date = Column(Date)
    List_id = Column(ForeignKey('checklist_info.List_id'), nullable=False, index=True)

    List = relationship('ChecklistInfo')
