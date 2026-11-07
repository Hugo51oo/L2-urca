# Épreuve blanche de diagnostic — prérequis quantitatifs L2

**Durée : 1 h 30 · Barème sur 20 · Calculatrice autorisée · Documents interdits**

Conditions réelles : chrono lancé, téléphone hors de portée, rien d'ouvert.
Une question laissée blanche est une information utile — ne pas remplir pour
remplir.

Les résultats numériques sont attendus **avec leurs unités et une phrase
d'interprétation** quand la question porte sur une grandeur économique. Une
formule sans ses hypothèses ne vaut pas la totalité des points.

---

## Partie A — Questions de cours (6 points)

**A.1 (1,5 pt)** — Soit à maximiser `f(x, y)` sous la contrainte
`g(x, y) = c`. Écrire les conditions du premier ordre du lagrangien, puis dire
ce que représente économiquement le multiplicateur λ.

**A.2 (1,5 pt)** — Donner deux critères équivalents d'inversibilité d'une
matrice carrée. Expliquer en une phrase pourquoi l'inversibilité conditionne
l'existence d'une solution unique à un système linéaire.

**A.3 (1,5 pt)** — Distinguer estimateur sans biais et estimateur convergent.
Un estimateur peut-il être biaisé et convergent ? Justifier.

**A.4 (1,5 pt)** — Énoncer le théorème central limite. Préciser à quelles
conditions il est mobilisable sur un échantillon de taille 30, et ce qui se
passe si la distribution mère est fortement asymétrique.

---

## Partie B — Optimisation sous contrainte (6 points)

Un consommateur a pour fonction d'utilité :

`U(x, y) = x^(1/3) · y^(2/3)`

Les prix sont `p_x = 2` et `p_y = 4`, le revenu est `R = 60`.

**B.1 (1 pt)** — Écrire le lagrangien du programme du consommateur.

**B.2 (2 pts)** — Poser les conditions du premier ordre et résoudre. Donner
`x*` et `y*`.

**B.3 (1,5 pt)** — Calculer `λ*` et en donner l'interprétation économique
précise.

**B.4 (1,5 pt)** — Le revenu passe de 60 à 66. Estimer la variation d'utilité
à partir de `λ*`, puis calculer la variation exacte. Les deux valeurs
coïncident-elles ? Expliquer pourquoi, en une phrase, à partir d'une propriété
de cette fonction d'utilité.

---

## Partie C — Calcul matriciel (4 points)

Économie à deux branches. La matrice des coefficients techniques est :

```
A = | 0,2   0,3 |
    | 0,4   0,1 |
```

La demande finale est `D = (70 ; 40)`. La production `X` vérifie `X = A·X + D`.

**C.1 (1 pt)** — Réécrire la relation sous la forme `(I − A)·X = D` et donner
la matrice `I − A`.

**C.2 (1,5 pt)** — Calculer le déterminant puis l'inverse de `(I − A)`.

**C.3 (1 pt)** — En déduire les productions `X₁` et `X₂`.

**C.4 (0,5 pt)** — Interpréter économiquement le coefficient situé en ligne 1,
colonne 2 de `(I − A)⁻¹`.

---

## Partie D — Estimation (4 points)

Sur un échantillon aléatoire de `n = 100` ménages, le revenu mensuel moyen
observé est `x̄ = 1 450 €` avec un écart-type empirique `s = 300 €`.

**D.1 (1 pt)** — Construire l'intervalle de confiance à 95 % du revenu moyen
de la population. Détailler les hypothèses utilisées.

**D.2 (1 pt)** — L'échantillon passe à `n = 400`, `x̄` et `s` inchangés. Que
devient la demi-largeur de l'intervalle ? Quelle taille d'échantillon
faudrait-il pour la diviser par 3 par rapport au cas initial ?

**D.3 (1 pt)** — Une étude antérieure avançait un revenu moyen de 1 500 €.
Ce résultat est-il compatible avec l'échantillon, au seuil de 5 % ? Conclure
explicitement.

**D.4 (1 pt)** — Pourquoi a-t-on utilisé 1,96 plutôt qu'un quantile de Student
dans D.1 ? Qu'aurait-il fallu faire si `n = 15` ?

---

## Après l'épreuve

Rends ta copie telle quelle — y compris les questions ratées et les blancs.

La correction classera chaque point perdu en **erreur de connaissance**
(le cours n'est pas su), **erreur de méthode** (le cours est su mais mal
mobilisé) ou **erreur d'exécution** (calcul, étourderie). C'est cette
répartition qui dira quoi travailler dans les deux prochaines semaines, pas la
note.

Le corrigé n'est pas fourni avec le sujet.
