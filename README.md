# „All-in-one“-Beispiel: Das Newton-Verfahren

Jupyter Notebooks können dafür verwendet werden Lehrveranstaltungen im MINT-Bereich in einem einzigen, interaktiven Dokument abzubilden. Neben dem klassischen Vorlesungsskript können zahlreiche weitere Begleitmaterialien, wie zum Beispiel Präsentationen, Rechnungen an der (virtuellen) Tafel und mit grafikfähigen/CAS-Taschenrechnern, interaktive Diagramme, Programmcode, 3D-Modelle, Videos, Übungsaufgaben, E-Assessment u.v.m. integriert werden. Das Notebook `Newton.ipynb` zeigt an einem beispielhaft gewählten Thema, wie Begleitmaterialien prinzipiell eingebunden werden können.


## Installation

* Installation von [Python 3.11](https://www.python.org/downloads/)
* optional: Einrichtung einer [virtuellen Umgebung](https://docs.python.org/3/library/venv.html#creating-virtual-environments) mittels `venv`
* Installation der benötigten Python-Pakete `python -m pip install notebook==6.5.6 numpy matplotlib ipycanvas`

Im Notebook wird für die Einbindung von Übungsaufgaben außerdem das E-Assessment-System [PyRope](https://github.com/PyRope-E-Assessment/pyrope) verwendet. Für die Installation von PyRope wird die Einrichtung einer virtuellen Umgebung empfohlen, um mögliche Versionskonflikte zu vermeiden.

Jupyter Notebook wird über die Konsole durch `jupyter notebook` gestartet.
