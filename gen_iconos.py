#!/usr/bin/env python3
"""Rasteriza los iconos PNG de la PWA (requiere ImageMagick). Correr solo si
cambia favicon_hex. Uso: python3 gen_iconos.py"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ / "fuentes"))

from motor_apuntes.gen_iconos import generar
from materia import CFG, CFG_SINTESIS

if __name__ == "__main__":
    # La sintesis comparte favicon_hex con el apunte completo, asi que los PNG
    # salen identicos, pero la PWA de cada salida los busca en su propia
    # carpeta: se rasterizan en las dos.
    generar(CFG, RAIZ)
    generar(CFG_SINTESIS, RAIZ / "sintesis")
