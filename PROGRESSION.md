# Progression L2 — apprentissage construit

Ce document n'est pas un planning de révision. C'est l'ordre dans lequel les
notions se construisent les unes sur les autres, et la méthode pour acquérir un
chapitre plutôt que le relire.

Les listes de chapitres correspondent au tronc commun standard de L2 économie.
À aligner sur ta maquette dès que tu l'as — la structure de dépendances, elle,
ne bougera pas.

---

## 1. Le problème que ça résout

L'emploi du temps te présente les notions dans un ordre administratif, pas dans
un ordre logique. Deux exemples que tu vas rencontrer dès octobre :

- La micro te fera maximiser une utilité sous contrainte budgétaire **avant**
  que le cours de maths ait fini Lagrange.
- La macro construira la courbe LM à partir d'une demande de monnaie que le
  cours d'économie monétaire traitera plus tard dans le semestre.

Résultat classique : tu suis le CM sans le comprendre, tu notes sans
comprendre, et tu découvres en décembre que le trou était en octobre.

La parade n'est pas de travailler plus. C'est de **prendre de l'avance sur les
briques amont uniquement**, qui sont peu nombreuses.

---

## 2. Le socle — à tenir avant tout le reste

Trois blocs. Tant qu'ils ne sont pas solides, tout ce qui s'appuie dessus est
du bachotage.

**Optimisation** — dérivées partielles, différentielle totale, lagrangien,
conditions du second ordre, théorème de l'enveloppe.
→ commande toute la microéconomie, et le sens du multiplicateur.

**Algèbre linéaire** — matrices, déterminant, inverse, résolution de systèmes.
→ commande le calcul matriciel appliqué (Leontief, tableaux
entrées-sorties) et, plus tard, l'écriture matricielle des MCO.

**Probabilités** — variable aléatoire, lois usuelles, espérance et variance,
convergences, théorème central limite.
→ commande toute la statistique inférentielle, puis l'économétrie.

Test d'acquisition du socle : sur feuille blanche, sans le cours, tu poses un
lagrangien à deux variables et tu le résous ; tu inverses une matrice 2×2 et
tu interprètes le résultat ; tu énonces le TCL avec ses conditions.

---

## 3. Les quatre chaînes de dépendance

### Chaîne quantitative — strictement linéaire, aucun saut possible

```
Probabilités
   └─> Distributions d'échantillonnage
         └─> Estimation ponctuelle (biais, convergence, efficacité)
               └─> Estimation par intervalle
                     └─> Tests d'hypothèses
                           └─> MCO simple
                                 └─> MCO multiple, Gauss-Markov
```

C'est la chaîne où le décrochage est irréversible : un trou à l'étape *n* rend
l'étape *n+1* inapprenable, pas seulement difficile. C'est aussi celle qui
porte le plus de rang, parce que la promo y décroche massivement.

### Chaîne microéconomique

```
Optimisation sous contrainte
   └─> Préférences, utilité, programme du consommateur
         └─> Demandes marshalliennes
               └─> Dualité : demandes hicksiennes, équation de Slutsky
         └─> Producteur : fonction de coût, offre
               └─> Équilibre partiel
                     └─> Équilibre général, optimum de Pareto
                           └─> Défaillances : monopole, externalités, biens publics
```

Le point de bascule est la **dualité**. Tant que le passage
marshallien / hicksien n'est pas clair, la décomposition de Slutsky reste une
formule apprise par cœur, et tout ce qui suit s'effondre en examen.

### Chaîne macroéconomique

```
Comptabilité nationale, équilibre emplois-ressources
   └─> Marché des biens : multiplicateur, courbe IS
   └─> Monnaie, création monétaire, demande de monnaie
         └─> Courbe LM
               └─> Modèle IS-LM, policy mix
                     └─> Marché du travail, courbe de Phillips
                           └─> AS-AD
                                 └─> Économie ouverte : Mundell-Fleming
                     └─> Croissance : Solow
```

Noter la dépendance croisée : **LM vient du cours d'économie monétaire**. Si
les deux UE existent séparément dans ta maquette, la macro ira plus vite que la
monétaire. Prends l'avance sur création monétaire et demande de monnaie.

### Chaîne comptable et institutionnelle

Comptabilité et histoire de la pensée sont **faiblement dépendantes** : on peut
les attaquer à peu près dans n'importe quel ordre. Conséquence pratique : ce
sont les seules matières qu'on peut légitimement décaler quand une semaine
déborde. Les trois autres chaînes, non.

---

## 4. La boucle d'acquisition, chapitre par chapitre

C'est ici que se joue la différence entre suivre un cours et apprendre.

**Avant le CM — 20 minutes.** Lire le plan du chapitre et vérifier les
prérequis dans les chaînes ci-dessus. Si une brique amont manque, c'est le
moment de la reprendre, pas après.

**Pendant le CM.** Noter les **mécanismes et les conditions de validité**, pas
la prose. Format : choc → canal de transmission → effet → hypothèse sous
laquelle ça tient. Tout ce qui est recopiable depuis un poly n'a pas à être
recopié.

**Dans les 24 heures — le geste décisif.** Reprendre une démonstration ou un
calcul du CM et le refaire **sans le cours**. Pas le relire : le refaire. C'est
l'unique étape que presque personne ne fait, et c'est celle qui sépare les
notes.

**Le TD.** Chercher les exercices *avant* la séance. Un TD suivi sans avoir
buté ne sert à rien : on croit comprendre parce qu'on voit quelqu'un d'autre
faire.

**Fin de chapitre.** Dix à quinze cartes de rappel actif, portant sur les
mécanismes et les conditions — jamais sur du vocabulaire. Puis une annale sur
le chapitre.

**Test d'acquisition.** Le chapitre est acquis quand tu peux **redériver le
résultat central sur feuille blanche** et énoncer les hypothèses sous
lesquelles il tombe. Pas quand tu reconnais l'énoncé.

---

## 5. Où le kit se branche

| Étape de la boucle | Outil |
|---|---|
| Prérequis manquant repéré avant un CM | `point-semestre` pour arbitrer le temps |
| Mise au propre après le CM | `fiche-revision` |
| Cartes de fin de chapitre | `revision-espacee`, collées dans le cockpit |
| Annale de fin de chapitre | `annales-blanches` |
| Suivi de ce qui est acquis | cockpit, séances et barème inverse |

L'ordre compte : ficher **après** avoir buté, jamais avant.

---

## 6. Ce qu'il faut faire maintenant

Le socle, et rien d'autre. Optimisation, algèbre linéaire, probabilités.

Deux heures par jour, en faisant des exercices et non en lisant. C'est la seule
avance qui se transforme mécaniquement en rang, parce qu'elle porte sur les
briques dont tout le reste dépend.
