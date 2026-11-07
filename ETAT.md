# État du projet — reprise de session

Dernière mise à jour : 8 septembre 2026. À relire au début de chaque session
Claude Code, à mettre à jour à la fin.

## Ce qui est en place

**L'outil.** `index.html` — cockpit autonome : deux semestres, barème inverse,
ECTS et compensation, échéances datées, comparaison temps/enjeu, moteur SM-2
intégré, import/export. Schéma de données v3.

**Le pilotage.** Quatre skills Claude Code (`point-semestre`,
`fiche-revision`, `annales-blanches`, `revision-espacee`), testées sur jeu de
données et corrigées, plus la commande `/point`.

**La méthode.** `PROGRESSION.md` — chaînes de dépendance entre notions et
boucle d'acquisition. Document de fond, indépendant de tout enseignant.

**Les cours cartographiés.** Quatre UE traitées à partir des polys réels, dans
`data/cours/` :

| Carte | Enseignant | Évaluation réelle |
|---|---|---|
| `histoire-des-sciences-carte.md` | A. Laude-Depezay | partiel unique 1 h 30, cours + réflexion |
| `calcul-analyse-couts-carte.md` | B. Huet | CC 50 % + ET 50 % |
| `microeconomie-carte.md` | J.-S. Gharbi | DST TD5 + DST TD10 + ET 1 h 30 ; barème 8 cours / 12 exos |
| `techniques-enquete-carte.md` | C. Ledoux | fiches 25 % + **oral 25 %** + ET 50 % |

**Le transversal.** `synthese-epistemologie-transversale.md` — met en regard
Histoire des sciences et Techniques d'enquête. À travailler en dernier.

**Le plan.** `plan-de-travail-s3.md` — les cinq séquences fondues en un ordre
unique, en quatre phases. C'est le document à ouvrir en premier.

**Les cartes.** `cartes-rappel-actif-s3.md` — 51 cartes au format collable,
vérifiées contre le parseur de l'app.

## Le point bloquant, et il s'est déplacé

Ce n'est plus « il manque des coefficients ». C'est **la structure des UE
elle-même**.

La licence d'économie de l'URCA annonce 5 UE de 6 ECTS par semestre. Or sept
matières sont déjà identifiées : Histoire des sciences, Calcul et analyse des
coûts, Microéconomie, Techniques d'enquête, plus Statistiques, Mathématiques
appliquées et Macroéconomie annoncées par Hugo.

Quatre matières de tronc commun sont confirmées par leurs polys : Histoire des
sciences, Calcul et analyse des coûts, Microéconomie, Techniques d'enquête.
S'y ajoutent les options retenues — **inférence statistique** et histoire, plus
sport.

Cela ne tient pas dans cinq UE à raison d'une matière par UE. Donc **les UE
sont des blocs regroupant plusieurs matières**, et la trame
`data/trame-l2-urca.json` — qui pose une matière = une UE = 6 ECTS — est
structurellement fausse. Les intitulés « Macroéconomie » et « Mathématiques
appliquées » qu'elle contient venaient d'une trame générique, pas de la
maquette : ne pas les traiter comme des matières suivies.

Conséquence : tant que la maquette n'est pas connue, ne pas injecter de
coefficients dans le cockpit. Un barème inverse calculé sur un mauvais
regroupement d'UE donne de mauvaises priorités, ce qui est pire que pas de
cockpit du tout.

Ce qu'il faut de Hugo, par ordre d'utilité :
1. **La maquette de L2** — quelles matières dans quelles UE, et les ECTS.
2. Le règlement d'examens (plafonnement en session 2).
3. Les dates d'épreuves, dont les séances de TD 5 et 10 en micro.
4. Les supports d'inférence statistique (option) — aucune carte possible sans eux.

## Décisions arrêtées

Ne pas les rouvrir sans raison nouvelle.

1. **Le barème inverse arbitre**, pas le ressenti. Classement par `pointsEnJeu`.
2. **Un seul moteur de cartes** : le SM-2 intégré. Kuliko n'est qu'un
   générateur ponctuel, son planning n'est pas suivi.
3. **Cibles** : 15 sur les UE quantitatives, 14 ailleurs.
4. **Notion écarté** : le vault Obsidian CERVEAU-vezy reste le système de notes.
5. **Pas de carte de cours sans poly.** Une carte générique habillée comme si
   elle venait du cours de Hugo est pire qu'une carte manquante — elle fait
   apprendre la mauvaise version avec confiance.
6. Ce dépôt est hors du quota de deux projets actifs.

## En attente d'une action de Hugo

- **La copie du diagnostic quantitatif** (`data/cours/diagnostic-quanti-blanche.md`),
  jamais rendue. Elle dirait où placer les heures du socle.
- **Le sujet de l'oral de Techniques d'enquête**, seul livrable du semestre qui
  se construit sur plusieurs semaines. Dès qu'il tombe : problématique au
  modèle de la carte, puis jalons intermédiaires dans le cockpit.

## Prochaines actions

1. Récupérer la maquette. Tout le reste en dépend.
2. Corriger la trame en conséquence, puis injecter dans `_etat` et réimporter.
3. Travailler le socle de `PROGRESSION.md` : optimisation, algèbre linéaire,
   probabilités. Ne dépend d'aucun document manquant.
4. Cartes de rappel actif sur les quatre matières cartographiées.

## Ce qu'on ne fait pas

Retoucher le cockpit. Il est fonctionnel. Règle anti-dérive : une amélioration
d'outil par semaine, aucune en semaine de partiels. Si une session dérive vers
le code plutôt que vers la révision, le dire et proposer la séance de travail.
