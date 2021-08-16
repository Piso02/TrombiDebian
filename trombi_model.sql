
CREATE TABLE `checklist_info` (
  `List_id` varchar(5) NOT NULL,
  `Machine_Ref` varchar(20) DEFAULT NULL,
  `VPNServer_Statut` varchar(3) DEFAULT NULL,
  `VPNBPOC_Statut` varchar(3) DEFAULT NULL,
  `VPNBPORH_Statut` int(3) DEFAULT NULL,
  `OCS_Statut` varchar(3) DEFAULT NULL,
  `Partage00AMI_Statut` varchar(3) DEFAULT NULL,
  `Partage01Propales_Statut` varchar(3) DEFAULT NULL,
  `Partage02ProjetMission_Statut` varchar(3) DEFAULT NULL,
  `Partage04OutilsInternes_Statut` varchar(3) DEFAULT NULL,
  `Partage05Biblio_Statut` varchar(3) DEFAULT NULL,
  `Partage06Qualite_Statut` varchar(3) DEFAULT NULL,
  `Badge_Statut` varchar(3) DEFAULT NULL,
  `Badge_Num` varchar(8) DEFAULT NULL,
  `Habilitation_Statut` varchar(10) DEFAULT NULL,
  `Matricule` varchar(10) NOT NULL
); 


CREATE TABLE `cursus` (
  `Cursus_id` varchar(10) NOT NULL,
  `Poste` varchar(100) DEFAULT NULL,
  `Cursus_DateDebut` date DEFAULT NULL,
  `Cursus_DateFin` date DEFAULT NULL,
  `Entreprise` varchar(100) DEFAULT NULL
); 


CREATE TABLE `cursus_personnel` (
  `Cursus_id` varchar(10) NOT NULL,
  `Matricule` varchar(10) NOT NULL
); 


CREATE TABLE `departement` (
  `Departement_id` varchar(4) NOT NULL,
  `Departement_Nom` varchar(25) DEFAULT NULL,
  `Departement_AdresseGroupE` varchar(40) DEFAULT NULL,
  `Departement_Partage` varchar(40) DEFAULT NULL
); 

CREATE TABLE `habilitation` (
  `Habilitation_num` varchar(5) NOT NULL,
  `Habilitation_Statut` varchar(12) DEFAULT NULL,
  `Habilitation_nom` varchar(100) DEFAULT NULL,
  `Habilitation_DateDemande` date DEFAULT NULL,
  `Demandeur_Nom` varchar(60) DEFAULT NULL,
  `Date_Arrivee` date DEFAULT NULL,
  `Date_Depart` date DEFAULT NULL,
  `Badge_StatutCS` varchar(12) DEFAULT NULL,
  `BesoinMateriel_Statut` varchar(3) DEFAULT NULL,
  `PCFixe_Statut` varchar(3) DEFAULT NULL,
  `Portable_Statut` varchar(3) DEFAULT NULL,
  `AutreMatériel` varchar(100) DEFAULT NULL,
  `AncienUtilisateur` varchar(100) DEFAULT NULL,
  `Note` varchar(100) DEFAULT NULL,
  `Mail_Statut` varchar(12) DEFAULT NULL,
  `Mail_Extension` varchar(20) DEFAULT NULL,
  `Personnel_AdresseGroupE` varchar(30) DEFAULT NULL,
  `AutreAdresse` varchar(40) DEFAULT NULL,
  `Mail_Routage` varchar(50) DEFAULT NULL,
  `Routage_DateDebut` date DEFAULT NULL,
  `Routage_DateFin` date DEFAULT NULL,
  `ReponseAuto_Statut` varchar(3) DEFAULT NULL,
  `ReponseAuto_Contenu` varchar(250) DEFAULT NULL,
  `ReponseAutoSuppr_Statut` varchar(3) DEFAULT NULL,
  `ReponseAutoSuppr_Date` date DEFAULT NULL,
  `Repertoire_Statut` varchar(3) DEFAULT NULL,
  `AutrePartage` varchar(40) DEFAULT NULL,
  `Repertoire_Detail` varchar(40) DEFAULT NULL,
  `Libertempo_Statut` varchar(3) DEFAULT NULL,
  `Demandeur_Libertempo` varchar(60) DEFAULT NULL,
  `GLPI_Statut` varchar(3) DEFAULT NULL,
  `Timesheet_Statut` varchar(3) DEFAULT NULL,
  `Demandeur_GT` varchar(60) DEFAULT NULL,
  `Quadra_Statut` varchar(3) DEFAULT NULL,
  `SageCompta_Statut` varchar(3) DEFAULT NULL,
  `SageRH_Statut` varchar(3) DEFAULT NULL,
  `Matricule` varchar(10) NOT NULL
);


CREATE TABLE `historique_habilitation` (
  `Historique_id` varchar(10) NOT NULL,
  `Historique_date` date DEFAULT NULL,
  `Habilitation_Motif` varchar(100) DEFAULT NULL,
  `Habilitation_num` varchar(5) NOT NULL
);


CREATE TABLE `personnel` (
  `Matricule` varchar(10) NOT NULL,
  `Personnel_Nom` varchar(30) DEFAULT NULL,
  `Personnel_Prenom` varchar(30) DEFAULT NULL,
  `Fonction` varchar(100) DEFAULT NULL,
  `Personnel_Statut` varchar(20) DEFAULT NULL,
  `Personnel_Mail` varchar(50) DEFAULT NULL,
  `Personnel_phone` varchar(20) DEFAULT NULL,
  `Departement_id` varchar(4) NOT NULL
);


CREATE TABLE `sauvegarde_mail` (
  `Sauvegarde_id` varchar(5) NOT NULL,
  `Sauvegarde_date` date DEFAULT NULL,
  `List_id` varchar(5) NOT NULL
);


CREATE TABLE `utilisateur` (
  `Utilisateur_Nom` varchar(30) DEFAULT NULL,
  `MotDePasse` varchar(20) DEFAULT NULL
);



