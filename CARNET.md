# 📒 Mon carnet de bord

**Nom :** BENTLEY

**Prénom :** Charlotte

**Adresse de mon site :** https://charlottebnty.pythonanywhere.com

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > sur GithHub

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > Parce que le site est hébergé sur un serveur accessible via Internet.

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > Google.com

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > il n'a pas trouvé la fonction, correspend à l'erreur HTTP 404, envoyé par le serveur

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > erreur log 

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > La mise en page

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > h1 pour la fonction du texte: titre, corps de texte, ...
   > p pour un paragraphe
   > ul pour créer une liste
   > li pour une ligne dans la liste

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > Car elle envoie une balise qui contient le lien de la photo qui se trouve sur le Web.

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > Pour ne pas embrouiller tout le monde et avoir une vision claire des choses, et chacun peut travailler sans gêner les autres.

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > C'est le serveur qui remplace 

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > Le HTML décrit le contenu et le CSS l'apparence de ce contenu 

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > 3 fichiers

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > Pour remettre à jour, il force le rechargement  

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > HyperText Transfer Protocol, le navigateur envoie la requête et le serveur envoie la réponse

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > 4 ou 5 requête

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > 404 signifie qu'il y a une erreur et que la requête n'a pas été trouvé et 200 ca veut dire ok, que la quête à été trouvée.

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > Il modifie seulement la copie de la page chargée.

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > Le paramètre est search_query et sa valeur est chat.

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > Le serveur attend probablement un nombre et n’arrive pas à convertir « bonjour ». Pour l’éviter, il faut vérifier l’entrée, par exemple avec un try/except.

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > L’utilisateur peut envoyer du code HTML ou JavaScript que le navigateur exécutera (faille XSS).

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   >  En GET, les données apparaissent dans l’URL. En POST, elles sont dans le corps de la requête.

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > J’utiliserais GET pour une recherche, parce qu’on peut partager l’URL. J’utiliserais POST pour une connexion, pour que le mot de passe n’apparaisse pas dans l’URL.

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > Non, elles sont visibles dans l’onglet Réseau. Seul HTTPS les chiffre.

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > 4xx : erreur du client (requête incorrecte, ex. 404). 5xx : erreur du serveur (ex. 500).

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > Le serveur répond 3xx avec la nouvelle adresse (Location). C’est le navigateur qui refait la requête. 

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > http://google.fr redirige vers https://www.google.fr. 

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > L’adresse IP, le navigateur et le système (User-Agent), la langue (Accept-Language). 

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > Afficher automatiquement Wikipédia dans votre langue.

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > Cherchez la ligne avec 404 dans votre log : la page demandée est le chemin après GET.

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > Elle n'est pas vraiment anonyme, on arrive à retrouver des informations sur nous et notre ordinateur. 

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > HTML : une page mise en forme, faite pour un humain qui la lit dans le navigateur. JSON : des données brutes, faites pour un programme.

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > Serveur : le code qui calcule l’heure et l’envoie en JSON (Python, PHP…). Navigateur : le JavaScript qui récupère ce JSON (fetch) et met l’heure à jour sur la page. Vérifiez dans votre code de /horloge, car je ne l’ai pas sous les yeux. 

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > Une application météo : elle envoie votre position et reçoit la température et les prévisions. 

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ 
