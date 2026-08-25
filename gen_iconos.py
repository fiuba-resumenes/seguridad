#!/usr/bin/env python3
"""Rasteriza los iconos PNG de la PWA (requiere ImageMagick). Correr solo si
cambia favicon_hex. Uso: python3 gen_iconos.py"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ / "fuentes"))

from motor_apuntes.gen_iconos import generar
from materia import CFG

if __name__ == "__main__":
    generar(CFG, RAIZ)
