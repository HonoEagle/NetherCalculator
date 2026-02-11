# NetherCalculator

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FFCC00)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-2ea44f)

Convertisseur de coordonnées Minecraft entre l'Overworld et le Nether avec une interface graphique simple en Python (`tkinter`).

## Aperçu
- Conversion `Overworld -> Nether` (X et Z divisés par 8)
- Conversion `Nether -> Overworld` (X et Z multipliés par 8)
- Coordonnée `Y` conservée
- Validation des entrées avec message d'erreur

## Prérequis
- Python 3.x
- `tkinter` (généralement inclus avec Python)

## Installation
```bash
git clone https://github.com/HonoEagle/NetherCalculator.git
cd NetherCalculator
```

## Lancement
Option 1 (Windows, recommandé) :
- Double-clique sur `start.bat`

Option 2 (terminal) :
```bash
python nether-calc.py
```

## Utilisation
1. Sélectionne la direction de conversion.
2. Entre les valeurs `X`, `Y`, `Z`.
3. Clique sur **Calculer**.
4. Lis le résultat affiché.

## Formules
- `Overworld -> Nether`
  - `X' = X / 8`
  - `Z' = Z / 8`
  - `Y' = Y`
- `Nether -> Overworld`
  - `X' = X * 8`
  - `Z' = Z * 8`
  - `Y' = Y`

## Exemple
Entrée : `Overworld -> Nether`, `X=800`, `Y=64`, `Z=-160`

Sortie :
- `X = 100.0`
- `Y = 64.0`
- `Z = -20.0`

## Structure du projet
```text
NetherCalculator/
|- nether-calc.py
|- start.bat
|- README.md
|- LICENSE
```

## Contribution
Les PR sont bienvenues. Ouvre une issue pour proposer une amélioration ou signaler un bug.

## Licence
Ce projet est sous licence MIT. Voir `LICENSE`.


