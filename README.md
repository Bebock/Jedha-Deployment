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

Le projet a pour objectif principal de s'intéresser aux retards lors du checkout, et à leurs conséquences sur les locations suivantes et donc sur les contrats perdus / non honorés, et donc sur la satisfaction des utilisateurs de GetAround. 
Il est donc indispensable de laisser un délai minimum entre 2 réservations successives d'un même véhicule afin de palier au mieux à ces retards sans pour autant entamer le nombre de réservations et donc le chiffre d'affaires de la société (et des loueurs). 



 
