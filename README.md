# L2 — Licence d'économie, URCA 2026-2027

Deux applications web autonomes et un jeu de documents de travail, pour piloter
l'année et réviser.

**En ligne :** https://hugo51oo.github.io/l2-urca/

## Ce que ça contient

| | |
|---|---|
| `index.html` | page d'accueil, deux entrées |
| `cours.html` | lecteur des cartes d'apprentissage — généré, ne pas éditer à la main |
| `cockpit.html` | suivi des notes : barème inverse, ECTS, échéances, rappel actif SM-2 |
| `data/cours/*.md` | les cartes d'apprentissage, **c'est la source** |
| `PROGRESSION.md` | chaînes de dépendance entre notions et boucle d'acquisition |
| `CLAUDE.md` · `ETAT.md` | instructions et reprise de session pour Claude Code |
| `.claude/skills/` | quatre skills de pilotage et de révision |

## Régénérer le lecteur

`cours.html` est produit à partir des fichiers markdown. Après toute
modification d'une carte :

```bash
python3 -m pip install markdown
python3 build.py
```

Le fichier obtenu est autonome : tout le contenu y est embarqué, aucune requête
réseau en dehors de Google Fonts.

## Publier sur GitHub Pages

```bash
git init
git add -A
git commit -m "L2 URCA — cockpit et cours"
git branch -M main
git remote add origin git@github.com:Hugo51oo/l2-urca.git
git push -u origin main
```

Puis dans **Settings → Pages**, choisir la branche `main` et le dossier
`/ (root)`. Le site est en ligne une minute plus tard. Aucune action de build
n'est nécessaire côté GitHub : tout est statique.

## Changer la palette

Chaque page porte un unique bloc `:root` en tête de sa feuille de style, et
aucune couleur n'est écrite en dur ailleurs. Remplacer ce bloc suffit à
reskinner l'ensemble.

Les cinq variables `--h-*` sont des **teintes** (au sens HSL), une par matière :
c'est le changement de couleur qui signale qu'on a changé de cours.

## Données

Le cockpit stocke tout dans le navigateur, sur l'appareil. Rien n'est envoyé à
un serveur, et les exports JSON sont exclus du dépôt par `.gitignore`. Les
supports de cours (PDF, PowerPoint, Word) sont également exclus : ils restent
en local.
