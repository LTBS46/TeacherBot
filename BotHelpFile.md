LGM est le chatbot (robot de dialogue) qui a été développé par les administrateurs du serveur afin de faciliter l'échange d'informations entre professeurs et élèves de la classe TS5. Ainsi le robot met à disposition des **commandes** permettant la gestion de devoirs ou de cours (la différence étant que dans un cours on peut rentrer des fichier et dans un devoirs on peut seulement mettre du texte). L'accès à ses fonctionnalités se présentent sous la forme:
```php
$commande "argument 1" "argument 2" ...
```
La partie "`$commande`" permet de faire à comprendre au robot que vous lui demandez quelques chose.
# Ensemble des commandes
## Pour les devoirs :books:
### `$get-dev "matière" "date"`:
va demander au bot le devoir _"date"_ de la matière _"matière"_.Si le nom n'est pas renseigné, le Bot renvoie tous les devoirs enregistré pour cette matière
### `$new-dev "matière" "date" "contenu"`:
va créer un devoir dans la base de données du bot, dans la matière _"matière"_, avec le nom _"date"_ et le contenu _"contenu"_
### `$change-dev "matière" "date" "contenu"`:
Change un devoir _déjà existant_ dans la base de données du bot, dans la matière _"matière"_, avec le nom _"date"_ et le contenu _"contenu"_
### `$del-dev "matière" "date"`:
Supprime un devoir de la base de données du bot
## `Pour les cours`:notebook:
### `$get-cours "matière" "nom" "fichier"`:
Le bot renvoie tout ce qui se trouve dans le dossier _"nom"_ de la matière _"matière"_ (c-à-d tous les fichiers qu'il y trouve). Si le champ _"fichier"_ est précisé (ne pas oublier de mettre l'extension du fichier) le bot ne vous renvoie que le fichier correspondant dans sa base de donnée
### `$new-cours "matière" "nom"`:
_Il est impératif de joindre un fichier à la commande_ , va créer un nouveau cours dans la matière dite avec le nom dit en y incluant le fichier transmis
### `$add-to-cours "matière" "nom"`:
_Il est impératif de joindre un fichier à la commande_ , va ajouter le fichier dans le cours correspondant, ainsi il sera disponible via la commande `get-cours`
### `$del-cours "matière" "nom" "fichier"`:
Supprime un fichier d'un cours (ne pas oublier de mettre l'extension du fichier). Si aucun nom de fichier n'est rentré, le bot détruit tout le cours en question
## Liste des cours
Les noms des matières sont les suivant (ils sont à rentrer avec rigueur si vous ne voulez pas que le robot vous renvoie une erreur, la casse, elle, n'importe pas) :
- anglaisg (pour mme gauthier)
- anglaisn (pour monsieur navizet)
- espagnol
- geo
- histoire
- isn
- maths
- philo
- si (sciences de l'ingénieur)
- spc (pour la physique-chimie)
- spemaths
- spespc
<!--stackedit_data:
eyJwcm9wZXJ0aWVzIjoidGl0bGU6IEJvdEhlbHBGaWxlXG5hdX
Rob3I6IExUQlM0NlxuY2F0ZWdvcmllczogJ0hlbHBGaWxlLCBI
ZWxwJ1xuZGF0ZTogJzIwMjAtMDQtMDMnXG4iLCJoaXN0b3J5Ij
pbLTEwOTMxMTExMDksOTMxODgyMTQ2XX0=
-->