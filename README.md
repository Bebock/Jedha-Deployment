# Deploiement - GetAround

---

# 1. Présentation du projet

GetAround est un service de AirBnB, spécialisé dans la location de véhicules allant de quelques heures à quelques jours. 

Lors de la location d'une voiture par GetAround, l'utilisateur doit compléter un checkin et un checkout au cours desquels les données suivantes sont enregistrées : 
- Etat de la voiture - dommages / anomalies pré-existants ou survenus au cours de la location
- Niveaux de carburants
- Nombre de kilomètres

Le service compte 3 flows différents permettant d'établir le contrat : 
- Via Mobile : Propriétaire et conducteur se rencontrent au checkin et au checkout pour signer les formulaires sur le smartphone du propriétaire
- Via Connect : Tout est dématérialisé, propriétaire et conducteur n'ont plus à se rencontrer et la voiture s'ouvre grâce au smartphone du conducteur
- Via Papier : La part des contrats papier est négligeable sur GetAround, mais cette solution existe si l'une des deux parties le souhaite

---

# 2. Objectif 

Le projet a pour objectif principal de s'intéresser aux retards lors du checkout, et à leurs conséquences sur les locations suivantes et donc sur les contrats perdus / non honorés, et donc sur la satisfaction des utilisateurs de GetAround. 
Il est en effet indispensable de laisser un délai minimum entre 2 réservations successives d'un même véhicule afin de palier au mieux à ces retards sans pour autant entamer le nombre de réservations et donc le chiffre d'affaires de la société (et des loueurs). 

**Objectif 1** : Déployer un dashboard permettant de visualiser l'impact du palier / seuil choisi sur les locations

**Objectif 2** : Déployer un modèle de Machine Learning permettant à l'utilisateur de cibler un prix de location en fonction des caractéristiques de son véhicule

---

# 3. Comment procéder ?

## Pré-requis

## Datasets 

- dataset_delay : Contient les informations relatives aux locations (statut, timing de retour, délai entre les locations)
- dataset_pricing : Contient les informations relatives aux véhicules 

## Fichiers

- Le notebook Part 1 - Getaround_EDA_Model.ipynb permet une première EDA et contient les modèles de prédiction du prix de location testés avant déploiement.
- Les fichiers finalized_model.sav et finalized_prepoc.sav contiennent le modèle de prédiction et le preprocessing des données nécessaire au fonctionnement du modèle
- Le fichier app.py contient le code pour déployer un dashboard et le modèle de prédiction via Streamlit
- Le dossier FastAPI contient les fichiers nécessaires au déploiement du modèle de prédiction via API 

---

# 4. Outils développés 

## Dashboard 

Le dashboard déployé est disponible [ici](https://getaround-ln.herokuapp.com/) aux sections Accueil et Dashboard. 
![image](https://user-images.githubusercontent.com/38078432/203615883-599081ef-1776-45f7-bf91-b4545832b4ec.png)
![image](https://user-images.githubusercontent.com/38078432/203615983-417a4bca-0b0d-437d-a5de-b6d344d2a7ae.png)

Le déploiement du modèle de prédiction du prix de location selon les caractéristiques du véhicule est disponible via Streamlit en section [Prediction](https://getaround-ln.herokuapp.com/)
![image](https://user-images.githubusercontent.com/38078432/203616113-63659286-1216-48dd-8c38-92b8cd94017e.png)

ou via FastAPI [ici](https://fastapi-ln.herokuapp.com/docs) et le fichier Request.py
![image](https://user-images.githubusercontent.com/38078432/203616211-06134dfd-7c6b-423c-b574-29084ee6aa77.png)


## Outil de prédiction

---

# 5. Informations

## Outils

Les notebooks ont été développés avec [Visual Studio Code](https://code.visualstudio.com/).

Le déploiement a été réalisé avec [Streamlit](https://streamlit.io/), [Heroku](https://www.heroku.com/platform) et [fastAPI](https://fastapi.tiangolo.com/). Le déploiement sur Heroku a été réalisé avec une connexion à Github. 

## Auteurs & contributeurs

Auteurs :

    Helene alias @Bebock
    Jean alias @Chedeta

La dream team :

    Henri alias @HenriPuntous
    Nicolas alias @NBridelance



 
