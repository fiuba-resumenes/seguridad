# Taller de Seguridad Informatica (TA051, FIUBA)

Apunte del Taller de Seguridad (catedra Mendez, Di Paola). Se arma con el
motor compartido de la plataforma
([fiuba-resumenes/motor](https://github.com/fiuba-resumenes/motor)), del que
depende una version fija (ver `requirements.txt`).

## Como se construye

```
fuentes/completo/<id>.html   capitulos del apunte (uno por clase)
fuentes/materia.py           identidad, paleta y agrupacion (CFG)
```

```bash
pip install -r requirements.txt
python3 -m motor_apuntes.lint_fragmentos fuentes/completo
python3 armar.py
```

`armar.py` arma `index.html`. Se van sumando clases: se crea el fragmento
en `fuentes/completo/` y se lo agrega a `CFG["grupos"]` en
`fuentes/materia.py`. Commitear el fragmento junto con el output regenerado.
