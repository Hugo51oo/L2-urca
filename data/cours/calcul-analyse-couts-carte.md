# Calcul et Analyse des coûts
## Carte d'apprentissage

Enseignant : B. Huet · 9 séances de 2 h · **CC 50 % + ET 50 %**

Établi à partir du plan de cours et des polys des thèmes 1 et 2. Les thèmes 3
à 5 restent reconstruits depuis les intitulés du plan — à confronter aux polys
dès que tu les as.

---

## 1. Ce qui distingue ce cours du reste

C'est une matière **procédurale**. On ne la sait pas, on sait la faire. Une
définition parfaitement récitée ne rapporte rien si le tableau de répartition
est faux, et à l'inverse une chaîne de calculs correctement déroulée rapporte
même quand le vocabulaire hésite.

Conséquence directe : **les exercices d'abord, la fiche après.** Ficher les
définitions avant d'avoir buté sur un calcul est le meilleur moyen de perdre
trois semaines.

---

## 2. La thèse du cours, démontrée dès le thème 1

Detoeuf, *Le prix de revient n'existe pas* (1937) : trois façons également
raisonnables de répartir 3 francs d'autobus entre des choux et des carottes
donnent trois prix de revient différents. **C'est la méthode qui détermine le
coût.**

Le cas de la PMI agroalimentaire le démontre numériquement :

| | Clés du contrôleur | Clés alternatives |
|---|---|---|
| Résultat unitaire A | 97,50 | 72,34 |
| Résultat unitaire B | −82,50 | −57,34 |
| Écart entre A et B | 180 | 129,68 |
| **Résultat global** | **15 000** | **15 000** |

Seules deux clés ont changé : l'administratif passe de 50/50 au prorata du CA,
et l'approvisionnement passe des kilos achetés au **nombre de lots traités**.

Deux choses à retenir, et elles reviendront tout le semestre :

1. La répartition des charges indirectes **déplace la rentabilité entre
   produits sans jamais modifier le résultat global**. Toute décision fondée sur
   un coût de revient complet est donc suspendue à un choix de méthode.
2. L'imputation par lots, présentée ici comme une simple « autre hypothèse »,
   est déjà de la **méthode ABC** — on impute selon un inducteur de coût réel
   plutôt que selon un volume. Le thème 4 ne fera que formaliser ce qui est
   déjà là.

---

## 3. Le vocabulaire à verrouiller tout de suite

Quatre catégories de charges, et la confusion entre elles coûte des points en
cascade parce qu'elle fausse le point de départ de tous les calculs.

| | Définition | Exemple du poly |
|---|---|---|
| **Incorporables** | charges de la comptabilité générale retenues en analytique | salaires des agents de production |
| **Non incorporables** | écartées car hors exploitation courante | charges exceptionnelles, pénalités |
| **Supplétives** | charges en analytique mais pas en comptabilité générale | rémunération des capitaux propres, prélèvement de l'exploitant |
| **De substitution** | retenues des deux côtés, mais pour un montant différent | dotations aux amortissements |

Piège du poly : les **dividendes attendus par les actionnaires ne sont pas une
charge du tout**, et les charges exceptionnelles sont non incorporables. Les
deux figurent dans la liste des frais administratifs pour être écartés.

Deux axes de classification, à ne jamais croiser mécaniquement :

- **direct / indirect** — le lien avec le produit (causé sans ambiguïté par ce
  produit, ou engendré par l'environnement commun à plusieurs produits) ;
- **variable / fixe** — le lien avec le niveau d'activité.

Les quatre combinaisons existent. Le poly note d'ailleurs explicitement
l'absence, dans son cas, de charges indirectes variables et de charges directes
fixes : c'est une simplification, pas une règle.

---

## 4. Le squelette du cours : une méthode par défaut de la précédente

C'est ce qui rend les neuf séances cohérentes. Chaque méthode existe parce que
la précédente échoue sur un point précis. Apprends le défaut, la méthode suit.

```
Thème 1   Le coût dépend de la méthode
             │  il faut bien répartir les charges indirectes
             ▼
Thème 2   COÛTS COMPLETS
          tableau de répartition, unités d'œuvre, hiérarchie des coûts
             │  défaut : les clés sont arbitraires, et les charges fixes
             │  sont imputées quel que soit le niveau d'activité
             ▼
Thème 3   DIRECT COSTING
          on cesse de répartir : marge sur coût variable, seuil de rentabilité
             │  défaut : on ne sait plus si un produit couvre ses propres
             │  charges fixes
             ▼
          DIRECT COSTING ÉVOLUÉ (coûts spécifiques)
          on réintègre les seules charges fixes directement attribuables
             │
             ▼
Thème 4   Les correctifs
          • imputation rationnelle → neutralise l'effet du niveau d'activité,
            isole le coût de sous-activité
          • coût marginal → le seul coût pertinent pour décider d'une commande
            supplémentaire
          • ABC → remplace les unités d'œuvre volumiques par des inducteurs
            d'activité (le cas des lots du thème 1)
             │
             ▼
Thème 5   Optimisation des marges sous contraintes de production
```

---

## 5. La chaîne de calcul — le geste central du thème 2

C'est l'exercice type. Il se déroule dans cet ordre, sans jamais sauter
d'étape :

```
1  Coût d'achat des MP            achat + charges indirectes d'approvisionnement
2  → entrée en stock MP           valorisation des sorties : CMUP ou FIFO
3  Coût des MP consommées         = sorties de stock
4  Coût de production des         = MP consommées + MOD
   produits fabriqués               + charges indirectes des centres de production
5  → entrée en stock PF           valorisation des sorties
6  Coût de production des         ≠ étape 4 dès qu'il y a un stock
   produits vendus
7  Coût de revient                = étape 6 + charges de distribution
8  Résultat analytique            = CA − coût de revient
```

**Les deux pièges qui font perdre le plus de points :**

- Confondre les étapes 4 et 6. Le coût de production des produits *fabriqués*
  n'est pas celui des produits *vendus* dès qu'un stock existe. Toute la
  variation de stock passe par là.
- Oublier que la méthode de valorisation des stocks (CMUP contre FIFO) change
  le résultat. C'est une illustration supplémentaire de la thèse du thème 1, et
  une question de réflexion toute trouvée.

---

## 5 bis. Le thème 2 en détail

### Les centres d'analyse

En comptabilité financière les charges sont classées **par nature** (locations,
frais postaux). En comptabilité de gestion on les reclasse **selon leur rôle
vis-à-vis du produit**. Deux types de centres :

- **Centre auxiliaire** — ne travaille pas pour les produits mais pour d'autres
  centres (Administration, Maintenance).
- **Centre principal** — relié aux produits par une unité d'œuvre
  (Approvisionnement, Atelier, Commercial).

Trois étapes, toujours dans cet ordre :
`① répartition primaire` (charges indirectes → tous les centres) →
`② répartition secondaire` (auxiliaires → principaux) →
`③ coût de l'UO` (principal → produits).

Règle pratique : commencer la répartition secondaire par le centre auxiliaire
qui alimente l'autre centre auxiliaire.

### La valorisation des stocks — quatre méthodes

Les entrées de matières premières se valorisent au **coût d'achat** (prix *plus*
frais d'approvisionnement, jamais le simple prix payé) ; les entrées de produits
fabriqués, au coût de production. Pour les **sorties**, quatre méthodes, qui
divergent dès que les prix bougent dans la période :

| | |
|---|---|
| **CUMP fin de période** | un seul coût moyen calculé en fin de période |
| **CUMP après chaque entrée** | recalculé à chaque entrée |
| **FIFO (PEPS)** | épuise d'abord les lots les plus anciens |
| **LIFO (DEPS)** | épuise d'abord les lots les plus récents |

Si les prix montent : FIFO valorise le stock final aux prix récents, donc
élevés, et les sorties aux prix anciens, donc bas. LIFO fait l'inverse.

Identité à vérifier systématiquement : **`SI + Achats − SF = Consommations`**.

### Cas Technor — la hiérarchie des coûts, et l'effet amortisseur des stocks

Deux produits à partir d'une même matière : A passe par deux ateliers (MP →
semi-fini, puis SF → A), B est obtenu en une étape. Résultat global 183 200 €,
cohérent avec la comptabilité générale.

Le résultat contre-intuitif du cas, et la meilleure question de réflexion du
thème : une **hausse de 20 % du prix de la matière première (+60 000 €) ne fait
baisser le résultat que de 12 832 €**. Parce que la hausse se répartit entre ce
qui est consommé dans le mois et ce qui reste immobilisé en stock — MP, semi-finis
et produits finis non vendus. Les stocks jouent un rôle d'amortisseur : l'impact
n'est pas annulé, il est **différé**. Les semi-finis de juin deviennent les
stocks initiaux de juillet et alourdiront le mois suivant.

### Cas MARCO SA — le tableau des charges indirectes

Cinq services, trois unités d'œuvre : kilo acheté, heure de main-d'œuvre
directe, unité vendue.

| | Admin. | Maint. | Appro | Atelier | Commercial |
|---|---|---|---|---|---|
| Répartition primaire | 120 000 | 50 000 | 50 000 | 126 500 | 66 500 |
| Après répartition secondaire | 0 | 0 | 80 000 | 220 500 | 112 500 |
| Coût de l'UO | | | 20 €/kg | 50 €/h | 125 €/u |

**Les prestations réciproques** — le morceau technique du semestre. Si
Administration et Maintenance travaillent l'une pour l'autre, aucun total ne
peut être calculé sans l'autre. On pose un système :

```
A = 120 000 + 10 % × M
M =  50 000 + 25 % × A
```

d'où `A = 128 205,13` et `M = 82 051,28`. Le total général réparti (413 000) ne
change pas — seule sa ventilation finale entre les trois centres principaux
bouge. C'est encore la thèse du thème 1.

### Cas particuliers du coût de production

- **En-cours** — fabrications inachevées en fin de période :
  `coût de la production terminée = en-cours début + charges de la période − en-cours fin`
- **Produits résiduels** — distinguer le **déchet** (résidu, type sciure) du
  **rebut** (produit impropre à l'usage normal). Trois traitements : s'il est
  vendable, sa valeur vient en déduction du coût du produit principal ; s'il est
  réutilisable dans le process, il a son propre coût, sans impact ; s'il est
  inutilisable, le coût de son enlèvement **majore** le coût du produit
  principal.
- Effet du taux de rebut : 140 000 € de coût total réparti sur 9 000 unités
  conformes (1 000 rebutées sur 10 000 lancées) donne 15,56 € l'unité. À coût
  total identique, plus le taux de rebut monte, plus le coût unitaire des
  conformes monte.

---

## 6. Les formules du thème 3

Peu nombreuses, mais elles doivent être automatiques :

- Marge sur coût variable : `MCV = CA − charges variables`
- Taux de MCV : `MCV ÷ CA`
- Seuil de rentabilité : `charges fixes ÷ taux de MCV`
- Point mort : la date à laquelle le seuil est atteint
- Marge de sécurité : `CA − seuil de rentabilité`
- Direct costing évolué : `marge sur coût spécifique = MCV − charges fixes
  spécifiques au produit`

Pour le thème 4 : coefficient d'imputation rationnelle = activité réelle ÷
activité normale ; les charges fixes imputées sont les charges fixes multipliées
par ce coefficient, et l'écart constitue le coût de sous-activité ou le boni de
suractivité.

---

## 7. Séquence de travail

1. **Verrouiller le vocabulaire du thème 1** — les quatre catégories de
   charges, et les deux axes de classification. Une demi-heure, pas plus.
2. **Refaire intégralement le cas de la PMI** sans le poly, y compris la
   seconde hypothèse d'imputation. Si tu retombes sur 15 000 des deux côtés,
   tu as compris la thèse du cours.
3. **La chaîne de calcul du thème 2, avec stocks**, jusqu'à l'automatisme. Le
   passage produits fabriqués / produits vendus est à faire buter au moins
   trois fois.
4. **Le tableau de répartition avec prestations réciproques** — c'est le
   morceau technique du semestre.
5. **Les formules du thème 3** en cartes de rappel actif. Ce sont les seules
   du cours qui méritent des cartes.
6. **Une question de réflexion par thème**, à l'écrit : « le coût de revient
   d'un produit est-il une donnée objective ? » est la question centrale du
   cours et peut tomber sous dix formulations.

---

## 8. Dans le cockpit

Deux évaluations de poids égal, contrôle continu et examen terminal. Le CC
tombant en cours de semestre, c'est une UE où le barème inverse devient
informatif tôt — dès la première note, tu sauras ce qu'il te faut à l'ET.
