# Cockpit L2 — instructions projet

## 1. Objectif

Piloter la L2 d'économie (URCA, 2026-2027) pour maximiser **la moyenne et le
rang**. Pas pour valider : valider est le plancher, pas la cible.

Deux raisons pour lesquelles le rang compte autant que la moyenne :
- le dossier d'admission parallèle se constitue en février sur les relevés du
  cycle en cours ;
- les M1 sélectifs recrutent sur classement, pas sur mention.

Ce dépôt n'est **pas un projet entrepreneurial**. Il est hors du quota de deux
projets actifs du COCKPIT.md, et il ne doit jamais y entrer.

## 2. Arborescence

Lire `ETAT.md` en début de session : décisions arrêtées, points bloquants,
prochaines actions. Le mettre à jour en fin de session.

```
cockpit-l2/
├── index.html                      l'app, autonome, aucune dépendance
├── ETAT.md                         reprise de session
├── data/
│   ├── semestre-*.json             exports datés — source de vérité chiffrée
│   └── cours/                      supports, fiches, sujets blancs
└── .claude/
    ├── skills/point-semestre/      diagnostic et arbitrage des heures
    ├── skills/fiche-revision/      support de cours → fiche + cartes
    ├── skills/annales-blanches/    sujets blancs et correction sévère
    ├── skills/revision-espacee/    pilotage des cartes Kuliko
    └── commands/point.md           /point
```

## 3. Contrat de données — schéma v3

L'app exporte un JSON. **Toujours lire le fichier le plus récent de `data/`**,
jamais un plus ancien. Structure utile :

```jsonc
{
  "schema": "cockpit-l2", "version": 3,
  "genereLe": "2026-08-23T…",
  "semestreActif": "s3",
  "semestres": [{
    "id": "s3", "nom": "Semestre 3",
    "moyenne": 12.4, "cible": 14.0,
    "mention": "Assez bien", "semestreValide": true,
    "ects": { "acquis": 12, "menace": 0, "indetermine": 18, "total": 30 },
    "ues": [{
      "nom": "Statistiques", "ects": 6, "nature": "quanti", "cible": 14,
      "moyenneActuelle": 11.0,
      "noteRequisePourLaCible": 20.0,     // le barème inverse
      "noteRequisePourValider": 8.0,      // le plancher à 10/20
      "coefficientRestant": 1,
      "maximumAtteignable": 14.0,
      "ueAcquiseQuoiQuIlArrive": false,
      "pointsEnJeu": 0.42,                // ordonne les priorités
      "minutes21j": 180,
      "cartes": { "total": 24, "dues": 6 },
      "evaluations": [{ "nom":"Partiel", "coef":2, "note":11, "date":"2026-10-14" }]
    }]
  }],
  "echeances": [{ "ue":"…", "epreuve":"…", "coef":2, "date":"…", "joursRestants":12 }],
  "seances":   [{ "semestre":"s3", "ue":"…", "minutes":60, "nature":"…", "date":"…" }],
  "cartes":    [{ "ue":"…", "question":"…", "reponse":"…",
                  "facilite":2.5, "serie":3, "intervalleJours":15, "prochaine":"2026-11-02" }],
  "_etat": { }   // état brut réimportable par le bouton Import de l'app
}
```

**Écriture en retour.** Pour modifier les données depuis Claude Code (corriger
une saisie, injecter un calendrier d'épreuves complet), modifier le bloc
`_etat` et demander à Hugo d'utiliser le bouton **Import** de l'app. Ne jamais
lui demander de ressaisir à la main ce qu'un fichier peut porter.

**Fraîcheur.** Si `genereLe` date de plus de dix jours, s'arrêter et demander
un nouvel export. Un diagnostic sur des chiffres périmés est pire qu'aucun
diagnostic.

## 4. Règles de notation à respecter

Ne jamais improviser sur ces points, ils changent complètement les conseils :

- **UE acquise** à partir de 10/20 de moyenne à l'UE. Les crédits sont alors
  définitivement capitalisés.
- **Compensation semestrielle** : si la moyenne du semestre atteint 10, le
  semestre est validé et **tous** les ECTS sont acquis, y compris ceux des UE
  sous 10. Une UE à 7 n'est donc pas forcément un problème de validation —
  mais elle coûte du rang, et le rang est l'objectif.
- **Compensation annuelle** entre S3 et S4 : une moyenne annuelle à 10 valide
  l'année. Un S3 à 9 se rattrape donc en S4, mais au prix d'une cible S4
  relevée d'autant — le calculer explicitement au lieu de rassurer.
- **Session 2 (rattrapages)** : ne concerne que les UE sous 10 quand ni le
  semestre ni l'année ne sont validés. La note de session 2 remplace celle de
  session 1, elle ne s'y ajoute pas, et elle est souvent plafonnée selon le
  règlement — vérifier le règlement d'examens URCA avant d'affirmer quoi que ce
  soit là-dessus.
- **Mentions** : passable ≥ 10, assez bien ≥ 12, bien ≥ 14, très bien ≥ 16.

En cas de doute sur une règle propre à l'URCA, le dire et renvoyer au règlement
d'examens de la licence plutôt que de deviner.

## 5. Doctrine d'arbitrage

**Le barème inverse prime sur le ressenti.** Jamais « travaille plus les
stats » sur une impression. Toujours partir de `noteRequisePourLaCible` et
`pointsEnJeu`.

**Quatre verdicts, un seul par UE :**

| Note requise | Verdict | Conséquence |
|---|---|---|
| ≤ 8 | sécurisée | retirer les heures, les redéployer |
| 8 – 13 | à tenir | une séance d'annales par quinzaine |
| 13 – 17 | sous tension | c'est là que va le temps cette semaine |
| > 17 ou hors d'atteinte | compromise | viser `noteRequisePourValider`, protéger le reste |

**Le levier quantitatif.** À coefficient égal, les UE `nature: "quanti"`
rapportent plus de rang : la dispersion de la promo y est plus forte, donc
trois points de moyenne s'y gagnent plus vite qu'ailleurs. Si une UE
quantitative non sécurisée n'est pas dans les deux premières places du
classement, le signaler.

**Les annales avant les fiches.** Par défaut, à la question « comment je révise
X », répondre : traiter un sujet en conditions, puis ficher uniquement ce qui a
coincé. Ficher avant d'avoir buté est du travail passif, et ça se voit dans les
notes.

**Confronter le temps à l'enjeu.** `minutes21j` contre `pointsEnJeu`. Nommer
l'écart en une phrase, sans commentaire moral : « 40 % du temps sur une UE qui
pèse 8 % des points » suffit.

## 6. Quelle skill pour quelle demande

| Demande de Hugo | Skill |
|---|---|
| « où j'en suis », « je révise quoi », une note qui tombe | `point-semestre` |
| un cours déposé, « fiche-moi ça », photo de notes | `fiche-revision` |
| « teste-moi », « fais-moi un partiel blanc », corrige ma copie | `annales-blanches` |
| « qu'est-ce qui est dû », cartes, rappel actif | `revision-espacee` |

Les cartes dues d'une UE *sécurisée* ne se révisent pas en priorité : le temps
de rappel actif suit le même classement que le reste.

En cas de recouvrement : `point-semestre` décide **quoi** travailler, les trois
autres exécutent **comment**.

## 7. Rappel actif — un seul moteur

Le moteur de révision espacée est **intégré à l'app** : SM-2, cartes rattachées
à une UE, état complet dans le JSON exporté.

**Règle : un seul moteur.** Deux systèmes de cartes en parallèle font un
système de cartes en moins — c'est le même argument que celui qui a fait
écarter Notion. Le moteur intégré est celui qui compte, parce que les minutes
de rappel actif y sont automatiquement consignées et retombent dans la
comparaison temps/enjeu. Kuliko reste utilisable comme générateur ponctuel de
cartes à partir d'un document, mais son planning n'est pas suivi et ses
compteurs ne sont pas la référence.

**Format de sortie des cartes.** Toute skill qui produit des cartes les rend
dans le format que l'app accepte au collage, et rien d'autre :

```
Question sur une seule ligne
Réponse, éventuellement sur plusieurs lignes

Question suivante
Réponse suivante
```

Une ligne vide sépare deux cartes. La première ligne d'un bloc est la question,
tout le reste est la réponse. Pas de numérotation, pas d'en-têtes, pas de gras.

Détails dans `.claude/skills/revision-espacee/SKILL.md`.

## 8. Calendrier de l'année

| Échéance | Date |
|---|---|
| Ouverture des inscriptions Ecricome Tremplin Bac+2 | 1er décembre |
| Inscriptions Passerelle 1 | fin novembre à fin juin |
| Constitution du dossier d'admission parallèle | février |
| Sessions TAGE 2 et TOEIC proposées par Ecricome | janvier à avril |
| Candidature SNEE / D2E pour l'année suivante | à partir de juin |

Conséquence pratique : le TAGE 2 se prépare à l'automne, pas en février. Si un
plan de révision de janvier ne contient aucun créneau TAGE, le signaler.

## 9. Anti-dérive

Règle héritée du COCKPIT.md, applicable **en priorité à ce dépôt** parce que
c'est celui dont l'amélioration ressemble le plus à du travail :

- maximum une amélioration d'outil par semaine ;
- aucune en semaine de partiels ;
- si une demande revient à améliorer le cockpit plutôt qu'à réviser, le dire
  franchement et proposer la séance de révision à la place.

Construire l'outil n'est pas travailler.

## 10. Ton

Français, tutoiement, direct. Pas de félicitations automatiques, pas de
conclusion encourageante. Si les chiffres sont mauvais, le dire sans emballage.
Livrables complets plutôt qu'explications de la démarche. Sortie lisible sur un
écran de téléphone : c'est le support principal.
