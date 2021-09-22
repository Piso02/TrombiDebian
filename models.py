# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AutreAdresse(Base):
    __tablename__ = 'autre_adresse'

    adresse_id = Column(String(5), primary_key=True)
    adresse_nom = Column(String(100))


class AutreMateriel(Base):
    __tablename__ = 'autre_materiel'

    materiel_id = Column(String(5), primary_key=True)
    materiel_denomination = Column(String(100))


class AutrePartage(Base):
    __tablename__ = 'autre_partage'

    partage_id = Column(String(3), primary_key=True)
    partage_nom = Column(String(100))


class Departement(Base):
    __tablename__ = 'departement'

    departement_id = Column(String(4), primary_key=True)
    departement_nom = Column(String(25))
    departement_adresseGroup = Column(String(40))
    departement_partage = Column(String(40))

    personnel = relationship('Personnel', secondary='departement_personnel')


class ExtensionMail(Base):
    __tablename__ = 'extension_mail'

    extension_id = Column(String(5), primary_key=True)
    extension_nom = Column(String(20))


class Personnel(Base):
    __tablename__ = 'personnel'

    matricule = Column(String(10), primary_key=True)
    personnel_nom = Column(String(30))
    personnel_prenom = Column(String(30))
    fonction = Column(String(100))
    personnel_statut = Column(String(20))
    personnel_mail = Column(String(50))
    personnel_phone = Column(String(100))


class RoutageMail(Base):
    __tablename__ = 'routage_mail'

    routage_id = Column(String(5), primary_key=True)
    routage_mail = Column(String(50))


class User(Base):
    __tablename__ = 'users'

    username = Column(String(30), primary_key=True)
    password = Column(String(30))


class ChecklistInfo(Base):
    __tablename__ = 'checklist_info'

    list_id = Column(String(5), primary_key=True)
    machine_ref = Column(String(20))
    VPNServer_statut = Column(String(3))
    VPNBPOC_statut = Column(String(3))
    VPNBPORH_statut = Column(String(3))
    OCS_Statut = Column(String(3))
    partage00AMI_statut = Column(String(3))
    partage01Propales_statut = Column(String(3))
    partage02ProjetMission_statut = Column(String(3))
    partage04OutilsInternes_statut = Column(String(3))
    partage05Biblio_statut = Column(String(3))
    badge_statut = Column(String(3))
    badge_num = Column(String(8))
    habilitation_statut = Column(String(10))
    matricule = Column(ForeignKey('personnel.matricule'), nullable=False, index=True)

    personnel = relationship('Personnel')


class Cursu(Base):
    __tablename__ = 'cursus'

    cursus_id = Column(String(10), primary_key=True)
    poste = Column(String(100))
    cursus_datedebut = Column(Date)
    cursus_datefin = Column(Date)
    entreprise = Column(String(100))
    matricule = Column(ForeignKey('personnel.matricule'), nullable=False, index=True)

    personnel = relationship('Personnel')


t_departement_personnel = Table(
    'departement_personnel', metadata,
    Column('departement_id', ForeignKey('departement.departement_id'), primary_key=True, nullable=False),
    Column('matricule', ForeignKey('personnel.matricule'), primary_key=True, nullable=False, index=True)
)


class Habilitation(Base):
    __tablename__ = 'habilitation'

    habilitation_num = Column(String(5), primary_key=True)
    habilitation_categorie = Column(String(12))
    habilitation_nom = Column(String(100))
    habilitation_datedemande = Column(Date)
    demandeur_nom = Column(String(60))
    date_arrivee = Column(Date)
    date_depart = Column(Date)
    badge_statutCS = Column(String(12))
    besoinMateriel_statut = Column(String(3))
    pcFixe_statut = Column(String(3))
    portable_statut = Column(String(3))
    ancienUtilisateur = Column(String(100))
    note = Column(String(250))
    mail_statut = Column(String(3))
    personnel_adresseGroup = Column(String(30))
    routage_datedebut = Column(Date)
    routage_datefin = Column(Date)
    reponseAuto_statut = Column(String(3))
    reponseAuto_contenu = Column(String(250))
    reponseAutoSuppr_statut = Column(String(3))
    reponseAutoSuppr_date = Column(Date)
    repertoire_statut = Column(String(3))
    repertBPORH_detail = Column(String(100))
    libertempo_statut = Column(String(3))
    libertempo_rattachement = Column(String(60))
    glpi_statut = Column(String(3))
    timesheet_statut = Column(String(3))
    glpiTS_rattachement = Column(String(60))
    quadra_statut = Column(String(3))
    sageCompta_statut = Column(String(3))
    sageRH_statut = Column(String(3))
    matricule = Column(ForeignKey('personnel.matricule'), nullable=False, index=True)
    partage_id = Column(ForeignKey('autre_partage.partage_id'), nullable=False, index=True)
    adresse_id = Column(ForeignKey('autre_adresse.adresse_id'), nullable=False, index=True)
    materiel_id = Column(ForeignKey('autre_materiel.materiel_id'), nullable=False, index=True)
    extension_id = Column(ForeignKey('extension_mail.extension_id'), nullable=False, index=True)
    routage_id = Column(ForeignKey('routage_mail.routage_id'), nullable=False, index=True)

    adresse = relationship('AutreAdresse')
    extension = relationship('ExtensionMail')
    materiel = relationship('AutreMateriel')
    personnel = relationship('Personnel')
    partage = relationship('AutrePartage')
    routage = relationship('RoutageMail')


class HistoriqueHabilitation(Base):
    __tablename__ = 'historique_habilitation'

    historique_id = Column(String(10), primary_key=True)
    historique_date = Column(Date)
    habilitation_motif = Column(String(100))
    commentaire = Column(String(12))
    habilitation_num = Column(ForeignKey('habilitation.habilitation_num'), nullable=False, index=True)

    habilitation = relationship('Habilitation')
