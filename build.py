#!/usr/bin/env python3
"""
Génère cours.html à partir des cartes markdown de data/cours/.

    python3 build.py

Le fichier produit est autonome : tout le contenu est embarqué, aucune
requête réseau hors Google Fonts. Relancer après chaque modification
d'une carte.
"""
import json
import pathlib
import re

import markdown

RACINE = pathlib.Path(__file__).parent
SOURCE = RACINE / "data" / "cours"
SORTIE = RACINE / "cours.html"

# ordre d'affichage, libellé court pour la navigation, teinte d'accent
DOCS = [
    ("maquette-s3.md",                      "Maquette S3",      "UE, codes et dates réelles", "maquette"),
    ("plan-de-travail-s3.md",               "Plan de travail",  "S3 — l'ordre d'attaque", "plan"),
    ("couts-devoir-blanc-cc.md",            "Devoir blanc — coûts", "CC du lundi 16 novembre", "blanccc"),
    ("micro-devoir-blanc-td5.md",           "Devoir blanc — micro", "TD 5 — mardi 3 novembre", "blanc"),
    ("monnaie-financement-carte.md",        "Monnaie et financement", "Chossat Noblot — 6 ECTS, 100 % terminal", "monnaie"),
    ("techniques-financieres-carte.md",     "Techniques financières", "Gaignette — 5 annales corrigées", "tefi"),
    ("microeconomie-carte.md",              "Microéconomie",    "Gharbi",         "micro"),
    ("calcul-analyse-couts-carte.md",       "Calcul des coûts", "Huet",           "couts"),
    ("techniques-enquete-carte.md",         "Techniques d'enquête", "Ledoux",     "enquete"),
    ("histoire-des-sciences-carte.md",      "Histoire des sciences", "Laude-Depezay", "sciences"),
    ("synthese-epistemologie-transversale.md", "Synthèse transversale", "Sciences × Enquête", "synthese"),
    ("inventaire-moodle-s3.md",              "Inventaire Moodle", "S3 — relevé du 21 octobre", "moodle"),
]

md = markdown.Markdown(extensions=["tables", "fenced_code", "attr_list"])


def decouper(html: str):
    """Découpe le document en sections de premier niveau (les <h2>)."""
    morceaux = re.split(r"(?=<h2)", html)
    sections = []
    for m in morceaux:
        if not m.strip():
            continue
        titre = re.search(r"<h2[^>]*>(.*?)</h2>", m, re.S)
        t = re.sub(r"<[^>]+>", "", titre.group(1)).strip() if titre else "Ouverture"
        sections.append({"titre": t, "html": m})
    return sections


def construire():
    docs = []
    for fichier, titre, sous_titre, cle in DOCS:
        chemin = SOURCE / fichier
        if not chemin.exists():
            print(f"  ignoré (absent) : {fichier}")
            continue
        brut = chemin.read_text(encoding="utf-8")
        # on retire le titre H1 et le sous-titre H2 d'en-tête, repris dans la coiffe
        brut = re.sub(r"\A#\s+.*?\n(##\s+.*?\n)?", "", brut, count=1)
        md.reset()
        html = md.convert(brut)
        docs.append({
            "cle": cle, "titre": titre, "sousTitre": sous_titre,
            "sections": decouper(html),
        })
        print(f"  {titre} — {len(decouper(html))} sections")

    gabarit = (RACINE / "gabarit.html").read_text(encoding="utf-8")
    sortie = gabarit.replace("/*__DONNEES__*/", json.dumps(docs, ensure_ascii=False))
    SORTIE.write_text(sortie, encoding="utf-8")
    ko = SORTIE.stat().st_size / 1024
    print(f"\ncours.html écrit — {ko:.0f} Ko")


if __name__ == "__main__":
    construire()
