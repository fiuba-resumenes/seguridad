#!/usr/bin/env python3
"""Arma este apunte. Uso: python3 armar.py

Una salida sobre el motor compartido: el apunte completo
(fuentes/completo/ -> ./). Se suman capitulos clase a clase editando
CFG["grupos"] en fuentes/materia.py.
"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ / "fuentes"))

from motor_apuntes.armar import construir
from materia import CFG

if __name__ == "__main__":
    sys.exit(construir(CFG, frag_dir=RAIZ / "fuentes" / "completo", out_dir=RAIZ))
