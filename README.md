# Sing-Stage-exercice
Dans le cadre de ma demande de stage, monsieur Orphée m'a chargé de réaliser l'exercice suivant:
Mettre au point un programme qui permettrait à lorsqu'on lui donne l'url d'un article dire s'il 
est positif (au sens élogieux) ou s'il est plûtot critique du sujet qu'il traite.
J'ai donc réaliser ce module Python, qui utilise un fichier txt dans lequel il y a 300 mots
relatif au champ lexical de la positivité.
Le principe est le suivant: 
 Lorsque l'on exécute le scrip une fenêtre s'ouvre dans laquelle
il est possible d'entrer une url. Si l'url est valide, le script télécharge le html de l'article 
dans un fichier txt, puis ouvre ce fichier txt et compare son contenu avec le contenu du fichier 
Qui sert de dictionnaire et lorsqu'il en trouve 20, le programme déduit que l'article est positif, 
entre 20 et 10 il déduit que l'article est plutot neutre et inférieur a 10 l'article est plutot négatif.
