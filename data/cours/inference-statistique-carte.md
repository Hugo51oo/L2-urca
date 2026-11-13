# Introduction à l'inférence statistique

## Bachir Dadda — UE 3.5 EC2A — 2 ECTS — CC 50 % + écrit terminal 1 h 30, 50 %

Carte établie le 13 novembre 2026 à partir des seize supports déposés sur
Moodle : les deux diaporamas de cours (*Rappels de statistique descriptive et
initiation à l'inférence*, *Distinction entre statistique descriptive et
inférentielle*), le diaporama *Introduction à l'échantillonnage*, la fiche des
fonctions du tableur, l'énoncé et la correction du TD 1 (PDF, Word et Excel),
et les huit classeurs de simulation — dé cubique, dé tétraédrique, quiz,
surbooking, sondage.

---

## 1. Ce qu'est ce cours, et ce qu'il n'est pas

Douze heures de CM condensées sur deux week-ends de septembre, puis vingt-deux
heures de TD jusqu'à fin novembre. **La matière se joue en TD**, et elle se
joue **sur tableur** : la moitié des supports sont des classeurs Excel où l'on
simule des tirages au hasard pour voir les lois apparaître.

Ce n'est donc pas un cours de probabilités à formules. C'est un cours qui veut
te faire comprendre une seule idée, sous plusieurs angles : **un échantillon
fluctue, et cette fluctuation se mesure**. Tout le reste — intervalle de
confiance, taille d'échantillon, test d'hypothèse — en découle.

La progression du cours suit cet ordre, et elle est stricte :

| Étape | Contenu | Support |
|---|---|---|
| 1 | Rappels de statistique descriptive | TD 1, diaporama de rappels |
| 2 | Population, échantillon, types de tirage | diaporama Échantillonnage |
| 3 | Simulation et convergence des fréquences | classeurs dé, quiz, surbooking |
| 4 | Estimateur : biais et convergence | diaporama Distinction |
| 5 | Intervalle de confiance et taille d'échantillon | diaporama Échantillonnage |
| 6 | Test d'hypothèse : test Z, ANOVA | diaporama Distinction |

Une lacune à l'étape 3 rend l'étape 5 inapprenable — pas seulement difficile.
C'est la chaîne quantitative de `PROGRESSION.md`, appliquée telle quelle.

---

## 2. Étape 1 — les rappels qui servent vraiment

Le TD 1 reprend la statistique descriptive de L1. Quatre choses en sortent qui
resserviront partout.

**Les sommes et leurs formules fermées.**
$$\sum_{i=1}^n i = \frac{n(n+1)}{2} \qquad \sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6} \qquad \sum_{i=1}^n i^3 = \frac{n^2(n+1)^2}{4}$$
Et le changement d'indice : $\sum_{n=1}^5 (1+n)^2 = \sum_{k=2}^6 k^2 = \sum_{k=1}^6 k^2 - 1 = 91 - 1 = 90$.

**Variance : les deux écritures.**
$$V(X) = \frac{1}{N}\sum n_i (x_i - \bar x)^2 = \frac{1}{N}\sum n_i x_i^2 - \bar x^2$$
La seconde — *moyenne des carrés moins carré de la moyenne* — est celle qu'on
utilise dans un tableau. Écart-type $\sigma = \sqrt{V(X)}$.

**Transformation affine.** Si $Y = aX + b$ :
$$\bar y = a\bar x + b \qquad V(Y) = a^2 V(X) \qquad \sigma_Y = |a|\,\sigma_X$$
Le $b$ disparaît de la variance : décaler toutes les valeurs ne change pas
leur dispersion. C'est l'exercice 5 du TD 1 — une baisse de 25 % des ventes,
soit $Y = 0{,}75X$, divise l'écart-type par le même facteur.

**Moyenne géométrique, pour les taux.** Trois variations de +3 %, +7 % et −2 %
donnent un coefficient global $1{,}03 \times 1{,}07 \times 0{,}98 = 1{,}0801$,
et un taux moyen $\sqrt[3]{1{,}0801} - 1 = 2{,}6\ \%$. **Pas** la moyenne
arithmétique $(3+7-2)/3 = 2{,}67\ \%$ : des taux se composent, ils ne
s'additionnent pas. Une baisse de 10 % suivie d'une hausse de 10 % ne ramène
pas au point de départ — $0{,}9 \times 1{,}1 = 0{,}99$.

**Données groupées en classes.** On prend le **centre de classe** comme valeur
$x_i$. La médiane se lit sur les effectifs cumulés croissants, par
interpolation linéaire dans la classe qui franchit $N/2$.

---

## 3. Étape 2 — population, échantillon, tirages

La statistique **descriptive** résume des données qu'on a. La statistique
**inférentielle** part d'un échantillon pour dire quelque chose d'une
population qu'on n'a pas — *en fournissant une mesure de la certitude de la
prédiction : une probabilité d'erreur*. C'est la définition du cours, et
l'expression « probabilité d'erreur » est celle qui compte.

Les cinq types de tirage probabiliste, avec l'exemple du cours (1 000
étudiants du campus Croix-Rouge) :

| Tirage | Principe |
|---|---|
| **Simple** | liste complète, on tire au hasard |
| **Systématique** | liste complète, on prend un individu tous les $k$ |
| **Par grappes** | on tire des groupes entiers (10 filières), puis on y répartit l'échantillon |
| **À plusieurs degrés** | tirage de groupes, puis de sous-groupes dans ces groupes, puis d'individus |
| **Stratifié** | on respecte les proportions de la population sur des critères fixés (la part d'éco-gestion sur le campus) |

Piège : grappes et stratifié se confondent facilement. **Les strates
reproduisent la structure de la population ; les grappes la remplacent par
quelques groupes tirés.** Le stratifié réduit la variance de l'estimation, les
grappes la réduisent en coût.

---

## 4. Étape 3 — la simulation : voir la loi apparaître

C'est le cœur original du cours, et la raison des huit classeurs Excel.

**Les trois formules à savoir écrire de tête** (fiche *Fonctions tableur*) :

| Formule | Produit |
|---|---|
| `=ALEA()` | un réel uniforme dans $[0;1[$ |
| `=ENT(ALEA()+p)` | **1 avec probabilité $p$, 0 sinon** — une épreuve de Bernoulli |
| `=ALEA.ENTRE.BORNES(1;6)` ou `=ENT(ALEA()*6+1)` | un lancer de dé |

La deuxième est la plus importante et la moins évidente. `ALEA()+p` dépasse 1
exactement quand `ALEA()` dépasse $1-p$, ce qui arrive avec probabilité $p$ ;
`ENT` tronque à l'entier, donc renvoie 1 dans ce cas et 0 sinon. Le classeur
des boules rouges l'utilise avec $p = 0{,}6$, celui du surbooking avec
$p = 0{,}9$.

**Ce que montrent les simulations — la loi des grands nombres.** Le classeur
du dé cubique tire 100, puis 1 000, puis 5 000 lancers, et calcule à chaque
fois l'écart entre fréquence empirique et probabilité $1/6$. L'écart se
resserre quand $n$ augmente. Le graphique des boules rouges montre la fréquence
osciller fortement sur les premiers tirages puis se stabiliser autour de 0,6.
**La fréquence observée converge vers la probabilité, et la moyenne empirique
vers l'espérance** — c'est ce qui légitime d'estimer l'une par l'autre.

**Le cas du surbooking — à savoir refaire.** Une compagnie vend 107
réservations pour un avion de 100 places ; chaque passager se présente avec
probabilité 0,9. Quel est le risque que plus de 100 passagers se présentent ?

- Le nombre de présents suit une **loi binomiale** $\mathcal{B}(107\,;\,0{,}9)$.
- Espérance $np = 96{,}3$, écart-type $\sqrt{np(1-p)} = \sqrt{9{,}63} = 3{,}10$.
- Probabilité exacte de dépassement : $P(X \ge 101) \approx 8{,}1\ \%$.
- La simulation du classeur trouve 11 vols en surréservation sur l'ensemble
  simulé : du même ordre, et l'écart avec 8 % est lui-même une fluctuation
  d'échantillonnage.

C'est l'exemple parfait du cours : une question économique réelle (combien
survendre ?), un modèle probabiliste simple, une simulation qui le confirme, et
un écart entre les deux qui illustre précisément ce qu'on étudie.

**Le quiz au hasard.** Cinq questions à trois propositions, un étudiant qui
répond au hasard : le nombre de bonnes réponses suit $\mathcal{B}(5\,;\,1/3)$.
Probabilités théoriques de 0 à 5 bonnes réponses : 13 %, 33 %, 33 %, 16 %, 4 %,
0,4 %. La simulation du classeur sur une centaine d'étudiants donne 13, 36, 29,
16 et 4 — presque exactement la loi. Le coefficient binomial $\binom{5}{k}$
apparaît en tête du classeur (1, 5, 10, 10, 5, 1).

---

## 5. Étape 4 — l'estimateur : biais et convergence

La moyenne empirique $\bar X_n = \frac{1}{n}\sum X_i$ est l'estimateur naturel
de l'espérance $\mu$. Deux propriétés la justifient, et le cours les démontre :

**Sans biais.** $E(\bar X_n) = \frac{1}{n}\sum E(X_i) = \frac{1}{n} \cdot n\mu = \mu$.
En moyenne sur tous les échantillons possibles, elle tombe juste.

**Convergente.** Les $X_i$ étant indépendants et de même loi :
$$V(\bar X_n) = \frac{1}{n^2}\sum V(X_i) = \frac{\sigma^2}{n} \quad\Longrightarrow\quad \sigma_{\bar X} = \frac{\sigma}{\sqrt n}$$
Sa dispersion diminue quand l'échantillon grandit.

$\sigma/\sqrt n$ est **la** formule du cours. Elle dit deux choses à retenir :
la précision augmente avec la taille de l'échantillon, mais **seulement comme
la racine** — pour diviser l'erreur par deux, il faut quatre fois plus
d'observations. C'est ce qui rend les grands sondages coûteux.

Le biais se définit en général : $B = E(\hat\theta_n) - \theta$, l'estimateur
est sans biais si $B = 0$.

---

## 6. Étape 5 — l'intervalle de confiance et la taille d'échantillon

**La construction.** Si $\bar X$ suit une loi normale, la variable centrée
réduite $\dfrac{\bar X - m}{\sigma/\sqrt n}$ suit une $\mathcal{N}(0,1)$, et
tombe entre $-1{,}96$ et $1{,}96$ avec probabilité 95 %. On isole $m$ :

$$\boxed{\bar X - 1{,}96\,\frac{\sigma}{\sqrt n} \;\le\; m \;\le\; \bar X + 1{,}96\,\frac{\sigma}{\sqrt n}}$$

**La largeur** vaut $2 \times 1{,}96 \times \sigma/\sqrt n$. Elle ne dépend pas
de $\bar X$ — c'est ce qui permet de calculer la taille d'échantillon **avant**
de l'avoir.

**La taille d'échantillon.** On veut une largeur au plus égale à $L$ :
$$2 \times 1{,}96\,\frac{\sigma}{\sqrt n} \le L \quad\Longleftrightarrow\quad n \ge \left(\frac{2 \times 1{,}96 \times \sigma}{L}\right)^2$$
Exemple du cours : $\sigma = 4$, $L = 1$ donne $\sqrt n \ge 15{,}68$, soit
$n \ge 246$. **On arrondit toujours à l'entier supérieur** : 245,9 personnes
ne suffisent pas.

**L'exercice des poids, refait.** 72 observations, moyenne
$\bar x = 54{,}14$ g, écart-type $\sigma = 5{,}33$ g.

- IC à 95 % : $54{,}14 \pm 1{,}96 \times 5{,}33/\sqrt{72} = 54{,}14 \pm 1{,}23$,
  soit **[52,91 ; 55,37] g**.
- Largeur au plus 0,5 g : $n \ge (2 \times 1{,}96 \times 5{,}3 / 0{,}5)^2 = 1\,726{,}6$,
  soit **$n \ge 1\,727$**. Le diaporama écrit 1 723, écart d'arrondi : en copie,
  garder les décimales jusqu'au bout.
- Conclusion attendue : **la largeur de l'intervalle décroît quand $n$
  augmente**, en $1/\sqrt n$.

Le diaporama mentionne aussi la **formule de Slovin** pour la taille
d'échantillon d'une population finie, $n = N/(1 + Ne^2)$, et l'estimation
d'une fréquence ; ces deux sections sont annoncées mais peu développées dans
le support. Les surveiller dans les TD restants.

---

## 7. Étape 6 — le test d'hypothèse

### Le test Z : le cas des sprinters

Sans produit, un sprinter réagit en moyenne en 0,25 s. Cent sprinters ayant
pris le produit réagissent en 0,175 s, écart-type 0,025 s. Le produit a-t-il
un effet ?

1. **Hypothèses.** $H_0 : \mu = 0{,}25$ (aucun effet) contre
   $H_1 : \mu \ne 0{,}25$ (un effet). Test bilatéral.
2. **Statistique de test.** $Z = \dfrac{\bar x - \mu_0}{\sigma/\sqrt n}$.
3. **Règle de décision** au seuil de 5 % : rejet de $H_0$ si $|Z| > 1{,}96$.
4. **Conclusion** : on rejette $H_0$, le produit a un effet significatif.

**Attention à une incohérence du support.** Le diaporama calcule bien
$\sigma_{\bar x} = 0{,}025/\sqrt{100} = 0{,}0025$ s, mais divise ensuite par
0,025 et obtient $Z = 3$. Avec l'erreur-type qu'il vient de calculer,
$Z = -0{,}075/0{,}0025 = -30$. La conclusion ne change pas — on rejette $H_0$
dans les deux cas, et encore plus nettement — mais **en copie, divise par
$\sigma/\sqrt n$**. C'est tout l'objet de l'étape 4.

Vocabulaire à maîtriser : hypothèse nulle, hypothèse alternative, seuil
$\alpha$, valeur critique, zone de rejet, **p-value** (probabilité d'observer
un écart au moins aussi grand si $H_0$ est vraie — on rejette quand elle est
inférieure à $\alpha$).

### L'ANOVA à un facteur

Trois examinateurs notent chacun cinq étudiants. Les moyennes diffèrent-elles ?

$H_0 : \mu_1 = \mu_2 = \mu_3$ contre $H_1$ : au moins une moyenne diffère.

| Étape | Calcul |
|---|---|
| Moyennes de groupe | $\bar X_1 = 3$, $\bar X_2 = 5{,}2$, $\bar X_3 = 6{,}4$ ; moyenne générale $\bar{\bar X} = 4{,}867$ |
| Somme des carrés **intra** | $S_{intra} = \sum (x - \bar X_g)^2 = 10 + 14{,}8 + 11{,}2 = 36$ |
| Somme des carrés **inter** | $S_{inter} = \sum n_g (\bar X_g - \bar{\bar X})^2 = 29{,}73$ |
| Statistique | $F = \dfrac{S_{inter}/(k-1)}{S_{intra}/(n-k)} \sim \mathcal{F}(k-1,\, n-k)$ sous $H_0$ |
| Ici | $k = 3$, $n = 15$ : $F = \dfrac{29{,}73/2}{36/12} = 4{,}96$ |
| Décision | valeur critique $F_{0{,}95}(2,12) = 3{,}885$ ; $4{,}96 > 3{,}885$, **rejet de $H_0$** |

**Seconde incohérence du support** : après avoir calculé $S_{inter} = 29{,}73$
et $S_{intra} = 36$, le diaporama pose $F = (36{,}4/2)/(38{,}4/12) = 5{,}69$.
Les chiffres injectés ne sont pas ceux qu'il vient d'obtenir. Avec les siens,
$F = 4{,}96$. La conclusion est la même — rejet — mais si le calcul tombe à
l'examen, refais-le avec tes propres sommes.

L'intuition à retenir : **l'ANOVA compare la dispersion entre les groupes à la
dispersion à l'intérieur des groupes.** Si les groupes s'écartent beaucoup plus
les uns des autres que leurs membres ne s'écartent entre eux, c'est que les
moyennes diffèrent vraiment.

---

## 8. Les pièges du programme

**Diviser par $\sigma$ au lieu de $\sigma/\sqrt n$.** L'erreur la plus grave du
cours — et le support la commet lui-même une fois. Dès qu'on parle de la
moyenne d'un échantillon, c'est l'erreur-type $\sigma/\sqrt n$.

**Arrondir une taille d'échantillon vers le bas.** Toujours à l'entier
supérieur.

**Moyenne arithmétique de taux.** Les taux se composent : moyenne
géométrique.

**Oublier que $b$ disparaît de la variance** dans une transformation affine,
et que $a$ y entre au carré.

**Confondre grappes et strates.**

**Lire « on accepte $H_0$ ».** On ne prouve jamais $H_0$ : on la rejette ou on
ne la rejette pas, faute de preuve suffisante.

**Formule Excel de Bernoulli.** `=ENT(ALEA()+p)` donne 1 avec probabilité $p$,
pas $1-p$.

---

## 9. Comment travailler cette matière

Le cours est construit sur Excel ; la révision doit l'être aussi. Ouvrir le
classeur du surbooking, effacer les formules, et les réécrire : une colonne de
107 `=ENT(ALEA()+0,9)`, une somme en bas, une ligne de 100 vols, un `NB.SI` des
vols au-dessus de 100. Si tu y arrives sans regarder, les étapes 3 et 4 sont
acquises.

Ensuite, à la main et sans calculatrice graphique : l'exercice des poids, puis
le test des sprinters avec la bonne erreur-type, puis l'ANOVA. Trois calculs,
une heure.

Le format exact du contrôle continu et de l'écrit terminal n'est donné nulle
part dans les supports. Le demander en TD : si l'écrit est sur machine, la
maîtrise du tableur vaut des points directs.

---

## 10. Rappel actif

**Quelle est la différence entre statistique descriptive et inférentielle ?**
La descriptive résume les données dont on dispose. L'inférentielle part d'un
échantillon pour tirer des conclusions sur une population qu'on n'observe pas
entièrement, en fournissant une probabilité d'erreur.

**Que renvoie la formule Excel =ENT(ALEA()+0,9), et pourquoi ?**
1 avec probabilité 0,9, 0 sinon. ALEA()+0,9 dépasse 1 exactement quand ALEA()
dépasse 0,1, ce qui arrive 9 fois sur 10 ; ENT tronque alors à 1. C'est une
épreuve de Bernoulli de paramètre 0,9.

**Une compagnie vend 107 places pour 100 sièges, chaque passager vient avec
probabilité 0,9. Quel modèle, quelle espérance, quel écart-type ?**
Loi binomiale B(107 ; 0,9). Espérance 96,3, écart-type racine de 9,63, soit
3,10. Le risque de surréservation, P(X ≥ 101), vaut environ 8 %.

**Pourquoi la moyenne empirique est-elle un bon estimateur de l'espérance ?**
Elle est sans biais, E(X̄) = μ, et convergente, V(X̄) = σ²/n tend vers 0 quand
n grandit.

**Que vaut l'écart-type de la moyenne d'un échantillon de taille n, et qu'en
déduit-on ?**
σ/√n. La précision n'augmente qu'en racine de la taille : diviser l'erreur par
deux demande quatre fois plus d'observations.

**Écris l'intervalle de confiance à 95 % de la moyenne, σ connu.**
X̄ − 1,96 σ/√n ≤ m ≤ X̄ + 1,96 σ/√n. Sa largeur, 2 × 1,96 × σ/√n, ne dépend pas
de X̄, ce qui permet de calculer la taille d'échantillon avant l'enquête.

**Quelle taille d'échantillon faut-il pour un intervalle de largeur 1, avec
σ = 4 ?**
n ≥ (2 × 1,96 × 4 / 1)² = 245,9, donc n = 246. On arrondit toujours à l'entier
supérieur.

**Trois hausses successives de 3 %, 7 % et −2 % : quel taux moyen ?**
La moyenne géométrique : racine cubique de 1,03 × 1,07 × 0,98, soit 1,026,
donc 2,6 % par période. Pas la moyenne arithmétique, parce que les taux se
composent.

**Si Y = aX + b, que deviennent la moyenne, la variance et l'écart-type ?**
Ȳ = aX̄ + b, V(Y) = a²V(X), σY = |a|σX. Le décalage b n'affecte pas la
dispersion.

**Quelle différence entre un tirage stratifié et un tirage par grappes ?**
Le stratifié reproduit les proportions de la population sur des critères
choisis. Les grappes tirent quelques groupes entiers et y prennent
l'échantillon. Le premier gagne en précision, le second en coût.

**Que compare une ANOVA à un facteur ?**
La dispersion entre les groupes à la dispersion à l'intérieur des groupes,
via F = (S_inter / (k−1)) / (S_intra / (n−k)), qui suit une loi de Fisher sous
H0. Si F dépasse la valeur critique, au moins une moyenne diffère.

**Que signifie une p-value de 0,003 au seuil de 5 % ?**
Si H0 était vraie, la probabilité d'observer un écart au moins aussi grand
serait de 0,3 %. C'est inférieur à 5 %, donc on rejette H0.

---

## 11. Mini-devoir blanc — 30 minutes

**Exercice 1.** Les ventes mensuelles d'une entreprise ont une moyenne de 22
et un écart-type de 5. Elle anticipe une baisse de 25 %. Moyenne et
écart-type des ventes prévisionnelles ?

**Exercice 2.** Un chocolatier pèse 64 tablettes : moyenne 101,5 g, écart-type
connu de 4 g. (a) Intervalle de confiance à 95 % du poids moyen. (b) Combien
de tablettes peser pour un intervalle de largeur au plus 1 g ?

**Exercice 3.** Le poids annoncé est 100 g. Au seuil de 5 %, l'échantillon de
l'exercice 2 permet-il de conclure que le poids moyen diffère de 100 g ?

**Exercice 4.** Écris la formule Excel qui simule un client qui rachète avec
probabilité 0,35, puis celle qui compte, sur 500 clients simulés en A1:A500,
combien ont racheté.

### Corrigé

**1.** $Y = 0{,}75X$ : $\bar y = 0{,}75 \times 22 = 16{,}5$ ;
$\sigma_Y = 0{,}75 \times 5 = 3{,}75$.

**2.** (a) $\sigma/\sqrt n = 4/8 = 0{,}5$ ; IC $= 101{,}5 \pm 1{,}96 \times 0{,}5$,
soit **[100,52 ; 102,48] g**. (b) $n \ge (2 \times 1{,}96 \times 4/1)^2 = 245{,}9$,
donc **246 tablettes**.

**3.** $H_0 : \mu = 100$ contre $H_1 : \mu \ne 100$.
$Z = (101{,}5 - 100)/0{,}5 = 3 > 1{,}96$ : **rejet de $H_0$**, le poids moyen
diffère significativement de 100 g. Cohérent avec la question 2 : 100 n'est
pas dans l'intervalle de confiance. Un test bilatéral au seuil de 5 % et un
intervalle à 95 % disent la même chose.

**4.** `=ENT(ALEA()+0,35)` recopiée de A1 à A500, puis `=SOMME(A1:A500)` ou
`=NB.SI(A1:A500;1)`.
