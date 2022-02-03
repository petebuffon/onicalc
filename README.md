# OniCalc

OniCalc is a Python library of various calculators for the survival simulation video game [Oxygen Not Included](https://www.klei.com/games/oxygen-not-included). It supports Python 3.8+.

*Not official Klei product. Not approved by or associated with Klei.*
## Features
- Colony food calculator for figuring out raw resources required for any number of dupes
- Spaced Out! foods currently in beta (ratios not 100% confirmed)
## Installation

Install my-project with npm

```bash
  pip install onicalc
```
    
## Usage/Examples

```python
>>> from onicalc import foodcalc
>>> foodcalc(4, "Gristle Berry")
{'Gristle Berry': 2.0, 'Bristle Blossom': 12.0, 'Water': 240.0}
```
