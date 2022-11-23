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
Il est donc indispensable de laisser un délai minimum entre 2 réservations successives d'un même véhicule afin de palier au mieux à ces retards sans pour autant entamer le nombre de réservations et donc le chiffre d'affaires de la société (et des loueurs). 

---

# 3. Comment procéder ?

## Pré-requis

## Datasets 

- dataset_delay : Contient les informations relatives aux locations (statut, timing de retour, délai entre les locations)
- dataset_pricing : Contient les informations relatives aux véhicules 

## Fichiers

    Le notebook Part 1 - EDA.ipynb permet de visualiser les données brutes (images et annotations) ainsi qu'une première EDA.
    Le notebook Part 2 - Yolov5.ipynb formatte les données pour l'utilisation de YoloV5 et permet d'entrainer le modèle
    Le notebook Part 3 - Deployment.ipynb se base sur le meilleur modèle choisi par l'utilisateur et le déploie grâce à outil en ligne qui permet à l'utilisateur de charger une photo sur laquelle il souhaite détecter les défauts.

---

# 4. Outils développés 


---

# 5. Informations

## Outils

    Les notebooks ont été développés avec Visual Studio Code.
    Le déploiement a été réalisé avec Streamlit et Heroku.

## Auteurs & contributeurs

Auteurs :

    Helene alias @Bebock
    Jean alias @Chedeta

La dream team :

    Henri alias @HenriPuntous
    Nicolas alias @NBridelance



 
