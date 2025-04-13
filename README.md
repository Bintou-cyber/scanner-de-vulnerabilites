# scanner-de-vulnerabilites
Scanner de vulnérabilités web – Python
Ce projet est un outil d’analyse de sécurité réseau simple et léger, développé en Python. Il a pour objectif principal de:

-Scanner les ports ouverts sur une adresse IP,

-Effectuer une analyse HTTP de base sur une URL cible,

-Fournir une première vue d’ensemble du niveau d’exposition d’un service web.

Pourquoi ce projet ?
Dans le cadre de ma formation en cybersécurité, j’ai souhaité créer un outil qui me permettrait :

De mieux comprendre les couches réseau,

D’explorer les vulnérabilités web de base,

Et de me familiariser avec les bibliothèques Python couramment utilisées dans l’analyse de sécurité.

Fonctionnement de l’outil
Ce scanner repose sur deux grandes fonctionnalités :

1. Scan de ports
Utilisation de la bibliothèque socket de Python.

L’outil tente de se connecter à une liste de ports TCP courants sur une adresse IP (ex : 21, 22, 80, 443, 8080...).

En cas de connexion réussie, le port est considéré comme ouvert.

Cela permet d’avoir une première cartographie du réseau, en repérant les services potentiellement actifs.

2. Analyse des en-têtes HTTP
Utilisation de la bibliothèque requests.

Une fois l’URL saisie, l’outil effectue une requête GET.

Il affiche ensuite les en-têtes HTTP de la réponse.

L’analyse des headers peut révéler des informations sensibles telles que :

Le type de serveur (Server: Apache, Server: ESF…),

Le langage ou framework utilisé (X-Powered-By: PHP/7.3…),

Des politiques de sécurité (Content-Security-Policy, X-Frame-Options…).


