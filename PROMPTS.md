# Mise en route et prompts à copier

## 1. Installation (une fois)

```bash
cd cockpit-l2
git init && git add -A && git commit -m "cockpit L2"
claude
```

Claude Code lit `CLAUDE.md` au démarrage et découvre les quatre skills dans
`.claude/skills/`. Rien d'autre à configurer.

Ouvre `index.html` dans le navigateur (double-clic). Sur mobile : pousse-le sur
GitHub Pages et ajoute la page à ton écran d'accueil. Les données restent sur
l'appareil.

## 2. La boucle de données

L'app **exporte** un JSON dans `data/`. Claude Code le lit pour arbitrer. Quand
Claude Code doit écrire en retour (injecter tout ton calendrier d'épreuves par
exemple), il modifie le bloc `_etat` du fichier et tu le recharges avec le
bouton **Import**. Aller-retour complet, aucune ressaisie manuelle.

## 3. Ce que tu fais aujourd'hui

Ouvre l'app, saisis pour le S3 : tes UE, leurs crédits, la nature de chacune,
la note que tu vises, et les épreuves connues **avec leurs dates**. Les dates
sont ce qui rend le compte à rebours et le plan de semaine utilisables.

Vingt minutes. Le reste attend.

## 4. Prompts à copier

### Le lundi — Claude Code
```
/point
```

### Tout le calendrier d'un coup — Claude Code
```
Voici mon calendrier d'examens du S3 (photo/copié-collé ci-dessous). Injecte
toutes les épreuves avec leurs coefficients et leurs dates dans le bloc _etat
du dernier export de data/, et redonne-moi le fichier à réimporter.
```

### Après une note — Claude Code
```
J'ai eu <note> en <UE> sur le <épreuve>. Mets à jour ma lecture du semestre :
ce que ça change sur le barème inverse des autres UE, sur les ECTS sécurisés,
et si je dois redéployer des heures cette semaine.
```

### Fiche de cours — Cowork
```
Prends le cours de <UE> chapitre <n> dans mon Drive et fais-en une fiche selon
la skill fiche-revision : noyau, mécanismes en choc → canal → effet →
condition, formules avec leurs hypothèses, erreurs classiques, questions de
rappel actif. Puis envoie les cartes dans Kuliko sous la matière <UE>.
```

### Fabriquer des cartes — Cowork ou Code
```
Sors-moi douze cartes de rappel actif sur <UE> chapitre <n>, au format collable
du cockpit : question sur une ligne, réponse en dessous, ligne vide entre deux
cartes, rien d'autre.
```
Puis dans l'app : ouvre l'UE, « Coller des cartes », colle le bloc tel quel.

### Réviser
Bouton **Réviser** dans l'app. Les minutes sont consignées toutes seules en fin
de session. Au clavier : espace pour retourner la carte, 1 à 4 pour noter.

Pour arbitrer :
```
D'après mon dernier export, sur quelle UE je dépense mes cartes dues, et est-ce
que ça correspond aux points en jeu ? Trois lignes.
```

### Entraînement — Cowork ou Code
```
Fais-moi une épreuve blanche de <UE> sur <chapitre>, format partiel, <durée>,
barème détaillé. Ne me donne pas le corrigé maintenant.
```
puis, la copie rendue :
```
Voici ma copie. Corrige au barème, sévèrement, et classe chaque point perdu en
erreur de connaissance, de méthode ou d'exécution.
```

### Poser les créneaux — Cowork
```
Prends le plan de semaine ci-dessus et pose les créneaux dans mon Google
Calendar, en évitant mes cours, séances quantitatives le matin, rappel quinze
minutes avant.
```

### Le dimanche soir — Cowork
```
Compare les créneaux de révision tenus cette semaine dans mon calendrier avec
le plan de lundi. Taux de tenue, UE sur laquelle j'ai décroché. Trois lignes.
```

## 5. Connecteurs

Déjà en place et utilisés ici : **Google Calendar** (créneaux et dates
d'épreuves), **Google Drive** (supports de cours). **Kuliko** reste
branché mais n'est plus le moteur : il ne sert que de générateur ponctuel de
cartes. Le planning qui fait foi est celui de l'app.

À ne pas ajouter : Notion. Tu as déjà le vault Obsidian CERVEAU-vezy, et deux
systèmes de notes en parallèle font un système de notes en moins.

## 6. Rappel

La règle anti-dérive du COCKPIT.md s'applique intégralement à ce dépôt : une
amélioration d'outil par semaine, aucune en semaine de partiels. Cette semaine,
ton quota est consommé par le cockpit lui-même.
