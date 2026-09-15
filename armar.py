#!/usr/bin/env python3
"""Arma este apunte. Uso: python3 armar.py

Dos salidas sobre el motor compartido, el mismo material en dos alturas de
lectura: el apunte completo (fuentes/completo/ -> ./) y la sintesis
(fuentes/sintesis/ -> sintesis/). Se suman capitulos clase a clase editando
CFG["grupos"] y CFG_SINTESIS["grupos"] en fuentes/materia.py. Las dos se
cruzan con el boton boton_extra_href de cada CFG.
"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ / "fuentes"))

from motor_apuntes.armar import construir
from materia import CFG, CFG_SINTESIS

SALIDAS = (
    (CFG, RAIZ / "fuentes" / "completo", RAIZ),
    (CFG_SINTESIS, RAIZ / "fuentes" / "sintesis", RAIZ / "sintesis"),
)

if __name__ == "__main__":
    # Se arman las dos siempre: si una falla se sigue con la otra y el codigo
    # de salida es distinto de cero, asi un error no esconde al siguiente.
    sys.exit(max(construir(cfg, frag_dir=frag, out_dir=out)
                 for cfg, frag, out in SALIDAS))
