
![Polylogo](https://lh3.googleusercontent.com/proxy/vrZOGWNKkffbTGgMZ-yypVpqS0VjGaZaaJOcgPThxeier5DFa2jFBOxwNnu3399B-QodQulHbkDcVuxVh1PCoYKgOTY)

# TP3

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise](https://www.timeanddate.com/countdown/generic?iso=20210131T2359&p0=165&msg=Remise&font=cursive&csz=1#)

[Voir le guide pour rédiger en Markdown](https://guides.github.com/features/mastering-markdown/)

## Partie 1: Introduction aux fonctions


## Partie 2: Dijskstra - Amusons-nous avec un classsique!

Passons aux choses sérieuses. Pour ce 2e exercice vous expérimenterez avec un des algorithmes les plus connus en informatique. Comme beaucoup d'algorithmes, son fonctionnement peu sembler obscur à première vue. Ce n'est qu'en l'implémentant que vous aurez une vue d'ensemble sur son fonctionnement et peut-être alors vous réaliserez que la logique est plutôt simple. C'est d'ailleurs ce qui en fait son efficacité.

![Disjktra_photo](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Edsger_Wybe_Dijkstra.jpg/180px-Edsger_Wybe_Dijkstra.jpg)

En 1959, [E. W. Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra) (1930-2002), encore à ce jour une des figures ayant le plus influencé les sciences informatiques, s'est attaqué à un problème classique en optimisation, le [problème du plus court chemin](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_plus_court_chemin). C'est un problème dont les applications sont très larges, répondant à des questions toujours actuelles comme:

* Quelles routes dois-je prendre pour arriver le plus vite possible à mon entrevue ce matin?
* Comment router le plus efficacement entre deux appareils une série de fichiers à travers internet?

Dijsktra a donc proposé un [algorithme](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) qui permet de trouver le plus court chemin entre deux point dans un graphe. Par exemple, il permet de trouver le chemin le plus court entre deux villes en considérant différentes
villes et le réseau routier qui les lient. On propose dans cet exercice d’implémenter cet algorithme.

![animation_dijkstra](https://upload.wikimedia.org/wikipedia/commons/2/23/Dijkstras_progress_animation.gif)
> Un exemple de dijsktra en action, dans un contexte ou les distances entre les points sont toujours de "1".

Explication de l’algorithme :
Soit le réseau routier donné par la Figure 1. Les villes sont données par les nœuds (A-G, E, S). Chaque route
est représentée par un arc orientée qui donne le sens de circulation et la distance entre les deux villes
connectés. On cherche à travers cet exemple de trouver le plus court chemin de la ville E à S.



Directives particulières
* Dans chaque programme vous pouvez ajouter d’autres fonctions à celles décrites dans l’énoncé, ainsi que
d’autres structures (et sous-structures), pour améliorer la lisibilité et suivre le principe DRY (Don’t Repeat
Yourself). À chaque endroit où vous remarquez une duplication de code (vous avez écrit les mêmes
opérations plus d’une fois) et qu’il n’est pas possible de l’éliminer avec ce qui a été vu en cours, indiquez-le
en commentaire.
* Il est interdit d’afficher directement ou indirectement dans les fonctions décrites si la description n’indique
pas d’affichage.
* Respecter le guide de codage, les points pertinents pour ce travail sont donnés en annexe à la fin.
* N’oubliez pas de mettre les entêtes de fichiers (guide point 33), et pour chaque fonction (guide point 89).
* Ne pas oublier de donner la description IN/OUT pour chacun des paramètres.


