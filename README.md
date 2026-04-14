# Système Bancaire en Microservices – Architecture Cloud-Native

## Description du projet

Ce projet présente une implémentation simple d'une architecture **cloud-native basée sur des microservices**.
L’objectif est de démontrer comment plusieurs services indépendants peuvent communiquer entre eux à l’aide de **Docker** et **Docker Compose**.

Le système simule une application bancaire simplifiée dans laquelle plusieurs microservices collaborent pour traiter une opération de paiement.

Chaque microservice possède une responsabilité précise, ce qui permet d'améliorer la **modularité, la maintenabilité et la scalabilité** du système.

---

## Architecture du système

L’application est composée de quatre microservices :

### Auth Service

Service responsable de l’authentification des utilisateurs.

Endpoint :

```
/auth
```

Retourne un utilisateur authentifié.

---

### Account Service

Service chargé de gérer les comptes bancaires.

Endpoint :

```
/balance
```

Retourne le solde du compte.

---

### Notification Service

Service responsable de l’envoi de notifications après une opération.

Endpoint :

```
/notify
```

Retourne un message de confirmation.

---

### Payment Service

Service principal qui orchestre l'opération de paiement.

Il communique avec :

* auth-service
* account-service
* notification-service

Endpoint :

```
/pay
```

Ce service agrège les réponses des autres microservices et retourne une réponse complète.

---

## Technologies utilisées

* Python
* Flask
* Docker
* Docker Compose

---

## Structure du projet

```
bank-system
│
├── auth-service
│   ├── app.py
│   └── Dockerfile
│
├── account-service
│   ├── app.py
│   └── Dockerfile
│
├── payment-service
│   ├── app.py
│   └── Dockerfile
│
├── notification-service
│   ├── app.py
│   └── Dockerfile
│
└── docker-compose.yml
```

---

## Lancement de l'application

Dans le dossier du projet, exécuter la commande suivante :

```bash
docker-compose up --build
```

Docker Compose va :

* construire les images Docker
* créer le réseau entre les conteneurs
* démarrer tous les microservices

---

## Test du système

Une fois les conteneurs démarrés, ouvrir un navigateur et accéder à :

```
http://localhost:5003/pay
```

---

## Exemple de réponse

```json
{
 "status": "Paiement traité avec succès",
 "auth": {
  "user": "estelle",
  "authenticated": true
 },
 "account": {
  "account_id": "ACC-1001",
  "balance": 1500
 },
 "notification": {
  "message": "Notification envoyée avec succès"
 }
}
```

Cette réponse montre que le microservice **payment-service** communique correctement avec les autres microservices.

---

## Objectif pédagogique

Ce projet démontre :

* le découpage d’une application en microservices
* la conteneurisation avec Docker
* l’orchestration locale avec Docker Compose
* la communication entre services via un réseau Docker interne

Cette architecture constitue une première étape vers un déploiement dans un environnement cloud utilisant des orchestrateurs comme **Kubernetes**.

---

## Auteur

Estelle Noukam

