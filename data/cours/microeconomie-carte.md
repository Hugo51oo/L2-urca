# Microéconomie — L2 EG
## Carte d'apprentissage

Enseignant : Jean-Sébastien Gharbi · CM 24 h (8 séances) + TD 15 h (10 séances)

Établi à partir de l'introduction générale, des Définitions 1 et 2, des
diapositives Consommateur et Producteur et des synthèses couvrant tout le
chapitre 1. Les chapitres 2 et 3 restent annoncés par le plan seul.

---

## 1. L'évaluation, connue à l'avance

| Épreuve | Quand | Durée | Poids |
|---|---|---|---|
| Devoir sur table n° 1 | séance de TD n° 5 | 1 h | 25 % |
| Devoir sur table n° 2 | séance de TD n° 10 | 1 h | 25 % |
| Examen final | fin de semestre | 1 h 30 | 50 % |

**Barème identique aux trois : 8 points de questions de cours et de
compréhension, 12 points d'exercices.**

Deux conséquences directes :

- **60 % de chaque note est du calcul.** L'entraînement sur exercices n'est pas
  une option de révision, c'est la majorité du barème. Les TD sont d'ailleurs
  déclarés indissociables du CM.
- **Les 8 points restants sont dans l'introduction générale**, pas dans les
  chapitres techniques. Voir section 3 : c'est le gisement que tout le monde
  néglige.

---

## 2. La structure du cours : un seul appareil, deux applications

C'est l'économie d'apprentissage la plus importante du semestre. Le producteur
n'est pas un nouveau chapitre : c'est le consommateur, transposé terme à terme.
Le cours le dit explicitement — la fonction de production est l'analogue de la
fonction d'utilité.

| Consommateur | Producteur |
|---|---|
| Fonction d'utilité `U(x, y)` | Fonction de production `q(K, L)` |
| Courbe d'indifférence | Courbe d'isoquante |
| Carte d'indifférence | Carte d'isoquantes |
| Convexité = préférence pour la diversité | Convexité = préférence pour la mixité des facteurs |
| `TmSxy = −Δy/Δx = Umx/Umy` | `TmSTKL = −ΔL/ΔK = PmL/PmK` |
| Contrainte de budget `R = x·px + y·py` | Droite d'isocoût `C = wL + rK` |
| Pente `px/py` | Pente `w/r` |
| Panier optimal : tangence, `TmSxy = px/py` | Production optimale : tangence, `TmSTKL = w/r` |
| Surplus du consommateur : sous la demande, au-dessus du prix | Surplus du producteur : au-dessus de l'offre, sous le prix |

Les deux colonnes ont les mêmes propriétés : courbes décroissantes, convexes,
et deux courbes d'un même agent ne se croisent jamais.

**La seule différence de fond, énoncée par le cours :** les niveaux d'utilité
du consommateur sont strictement subjectifs, les niveaux de quantité produite
ne le sont pas.

Méthode qui en découle : maîtriser la colonne de gauche jusqu'à l'automatisme,
puis traduire. Un exercice sur le producteur est un exercice sur le
consommateur avec un autre vocabulaire. Réviser les deux comme deux chapitres
indépendants, c'est faire deux fois le même travail.

Les deux optimums sont des maximisations sous contrainte — c'est exactement
Lagrange. Le socle mathématique de `PROGRESSION.md` est l'outil de ce cours.

---

## 3. L'introduction générale — les 8 points que personne ne travaille

Elle a l'air d'un préambule. C'est en réalité la matière des questions de
compréhension, et elle est conceptuellement plus difficile que les exercices.

**Le statut des modèles.** Un modèle est une représentation simplifiée, conçue
pour répondre à une question précise, valable *ceteris paribus*. Reprocher à un
modèle d'être irréaliste, c'est souvent lui reprocher d'être un modèle — ce que
le cours qualifie d'absurde. La vraie question n'est pas la ressemblance des
hypothèses avec la réalité, mais leur **pertinence au regard de l'objectif du
modèle**. Formulation à retenir : la question du réalisme se juge à la
compréhension des mécanismes réels que le modèle permet, et c'est finalement
une question empirique.

**Les choix révèlent les préférences.** Toutes les objections spontanées
— « je préfère les poires mais elles étaient trop chères » — portent sur le
contexte. Or l'économiste **inclut le contexte dans la préférence**, contraintes
budgétaires comprises. D'où un sens technique du mot, différent du langage
courant, et surtout : la préférence devient **observable**. Corollaire que le
cours souligne : l'égoïsme prêté à l'*homo economicus* est discutable, puisque
les préférences peuvent inclure sollicitude et empathie.

**Ordinal contre cardinal.** Cardinal : le nombre mesure l'intensité de la
satisfaction, les écarts ont un sens. Ordinal : on ne retient que le classement.
L'économie retient l'ordinal — et c'est ce qui autorise la démarche empirique,
donc le test des théories.

**Non-comparabilité interpersonnelle**, abandonnée depuis les années 1930.
Conséquence lourde et très interrogeable : **il n'existe plus une solution
collective optimale unique déterminable par le calcul.** Exemple du cours :
ouvrir ou non la fenêtre dans une salle de classe.

**Les quatre axiomes** — complétude, réflexivité, transitivité, continuité.
Leur fonction est instrumentale : ils permettent de représenter les préférences
par une fonction, donc d'utiliser tout l'outillage mathématique. La question du
cours sur la transitivité de l'amitié est un test de compréhension typique :
« les amis de mes amis sont mes amis » est faux, donc l'amitié n'est pas
transitive.

**Révolution marginaliste.** Utilité marginale = variation d'utilité d'une unité
supplémentaire. L'utilité totale croît, mais de moins en moins vite : utilité
marginale décroissante. Elle reste toujours positive — c'est la **monotonie**
des préférences, ou non-satiété, qui découle des quatre axiomes.

---

## 4. Les points techniques à ne pas rater

**La double condition du producteur.** La maximisation du profit exige deux
conditions, chacune nécessaire, aucune suffisante isolément :

1. **Production optimale sous contrainte technique** : `TmSTKL = w/r`. C'est
   l'absence de gaspillage.
2. **Optimum économique** : `Cm = p`. Tant que le prix dépasse le coût
   marginal, produire une unité de plus accroît le profit.

Ensemble seulement, elles équivalent à la maximisation du profit. Donner une
seule des deux est l'erreur classique.

**Coût et productivité : une relation d'identité, pas de causalité.** Quand la
productivité moyenne monte, le coût moyen baisse ; quand la productivité
marginale monte, le coût marginal baisse. Formulation à retenir : la loi des
rendements marginaux décroissants **est**, de façon équivalente, une loi des
coûts marginaux croissants. Ce sont deux lectures du même phénomène.

**La condition de fermeture.** Maximiser le profit donne `p = Cm`, mais
produire n'est pas toujours la meilleure option : un arrêt de production coûte
`−CF`. L'entreprise sort du marché si **`CVM > p`** — la recette ne couvre même
plus les coûts variables. Conséquence : seule la portion de la courbe de coût
marginal **située au-dessus du coût variable moyen** constitue la courbe
d'offre. Deux corollaires très interrogeables : la courbe d'offre d'une
entreprise concurrentielle est toujours croissante, et deux entreprises d'un
même secteur qui maximisent leur profit ont nécessairement le **même coût
marginal**, puisqu'elles égalisent toutes deux leur Cm au même prix de marché.

**Décomposer une variation de surplus.** Quand le prix passe de `p₀` à `p₁`, la
perte de surplus du consommateur se décompose en deux morceaux : un
**rectangle**, la perte sur les quantités encore achetées, et un **triangle**,
la perte due à la baisse de la quantité consommée. C'est l'outil standard
d'évaluation des mesures publiques — hausse de TVA, droits de douane.

**La limite du surplus du consommateur.** Il ne mesure exactement l'utilité que
si la fonction d'utilité est **quasi-linéaire** (linéaire en y, concave en x),
condition sous laquelle le prix de réserve du bien x ne dépend pas du revenu
disponible pour les autres biens. Sinon c'est une approximation — mais une
approximation utile, les erreurs de mesure des fonctions de demande réelles
étant généralement plus grandes que cette approximation elle-même.

**De la demande individuelle à la demande de marché.** La demande totale est la
somme des demandes individuelles à chaque prix, sous deux hypothèses : tous les
consommateurs font face au **même prix**, et la demande des uns n'est pas
influencée par celle des autres (**absence de mimétisme**). Sous ces hypothèses,
tout ce qui vaut pour un individu — TmS, équilibre, surplus — reste valable au
niveau agrégé.

**Les fonctions Cobb-Douglas.** La forme fonctionnelle des exercices, découverte
empiriquement en 1928 par Charles Cobb et Paul Douglas : `q = c·K^α·L^β`. Elle
se transpose telle quelle côté consommateur : `U = c·x^α·y^β`. Les exemples
simples `U(x,y) = xy` et `q(K,L) = KL` en sont le cas particulier `c = 1`,
`α = β = 1`.

**Le surplus du consommateur ne peut pas être négatif.** Si le prix de marché
dépasse le prix de réserve, le consommateur n'achète pas — il n'y a donc pas de
surplus négatif. Question de compréhension évidente.

**Le surplus se mesure en utilité, pas en unités monétaires.** Le nombre
d'unités monétaires est objectif ; l'utilité qu'un gain monétaire procure est
subjective et varie d'un individu à l'autre.

**Revenu réel contre nominal.** Le revenu réel est le panier effectivement
accessible : graphiquement, la surface sous la droite de budget. Si elle
augmente, le revenu réel augmente.

---

## 5. Un point à faire préciser en TD

Le poly Définitions 2 énonce qu'à l'optimum du producteur, on a **égalité des
productivités marginales des facteurs, `PmL = PmK`**.

Or le cours pose lui-même `TmSTKL = PmL/PmK` et, à l'optimum,
`TmSTKL = w/r`. En combinant : `PmL/PmK = w/r`, c'est-à-dire
**`PmL/w = PmK/r`** — les productivités marginales par euro dépensé sont
égales, pas les productivités marginales elles-mêmes. Les deux énoncés ne
coïncident que si `w = r`.

Le même point vaut côté consommateur : la condition est `Umx/px = Umy/py`.

Ce n'est pas anodin, parce que c'est une formule qu'on applique en exercice.
Pose la question en TD plutôt que de trancher seul : c'est la formulation
attendue par l'enseignant qui rapporte les points, et il s'agit peut-être d'un
raccourci d'écriture propre au cours.

*Mise à jour :* les supports de synthèse couvrant tout le chapitre 1 posent bien
`TmST_KL = PmL/PmK` et ne reprennent nulle part l'égalité `PmL = PmK`. La
formule générale est donc confirmée, et l'énoncé du poly Définitions 2
ressemble à un raccourci. La question reste à poser, mais elle est moins
urgente.

---

## 6. Séquence de travail

1. **L'introduction générale, fichée sérieusement.** Huit points par épreuve,
   trois épreuves. C'est le meilleur rapport temps/points du semestre et
   personne ne le travaille.
2. **La colonne consommateur**, jusqu'à savoir tracer, dériver un TmS et poser
   l'optimum sans notes.
3. **La traduction vers le producteur** — en une séance, en construisant
   toi-même le tableau de correspondance de la section 2 de mémoire.
4. **Les exercices de TD, refaits sans le corrigé**, dans les 24 h. C'est
   12 points sur 20.
5. **Cartes de rappel actif** sur l'introduction générale et les définitions
   uniquement. Les mécanismes de calcul s'acquièrent par les exercices, pas par
   des cartes.
6. **Premier jalon ferme : le devoir sur table de la séance de TD n° 5.** À
   caler dans le cockpit dès que le calendrier des TD est connu.

---

## 7. Suite du programme

- Chapitre 1 : Consommateur et producteur — A) vers la courbe de demande,
  B) surplus du consommateur, C) vers la courbe d'offre, D) surplus du
  producteur. **Couvert intégralement par les supports disponibles.**
- Chapitre 2 : Concurrences parfaite et imparfaites
- Chapitre 3 : L'équilibre général et ses limites

Le chapitre 3 est le point de bascule signalé dans `PROGRESSION.md` : c'est là
que l'appareil du chapitre 1 se referme sur l'analyse du marché.
