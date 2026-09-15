# Taller de Seguridad Informatica (TA051, FIUBA)

Apunte del Taller de Seguridad (catedra Mendez, Di Paola). Se arma con el
motor compartido de la plataforma
([fiuba-resumenes/motor](https://github.com/fiuba-resumenes/motor)), del que
depende una version fija (ver `requirements.txt`).

## Como se construye

Hay dos salidas, el mismo material en dos alturas de lectura:

| Salida | Fuentes | Que es |
|---|---|---|
| `index.html` | `fuentes/completo/` | el apunte desarrollado, con casos, ejemplos y tablas |
| `sintesis/index.html` | `fuentes/sintesis/` | la version corta, parrafos corridos pegados a la diapositiva |

```
fuentes/completo/<id>.html   capitulos del apunte (uno por clase)
fuentes/sintesis/s-<id>.html capitulos de la sintesis
fuentes/materia.py           identidad, paleta y agrupacion (CFG, CFG_SINTESIS)
```

```bash
pip install -r requirements.txt
python3 -m motor_apuntes.lint_fragmentos fuentes/completo
python3 -m motor_apuntes.lint_fragmentos fuentes/sintesis
python3 armar.py
```

`armar.py` arma las dos salidas de una. Se van sumando clases: se crea el
fragmento en la carpeta de fuentes que corresponda y se lo agrega a
`CFG["grupos"]` o a `CFG_SINTESIS["grupos"]` en `fuentes/materia.py`. Commitear
el fragmento junto con el output regenerado.

Las dos paginas se cruzan con el boton del sidebar (`boton_extra_href`). La
sintesis comparte paleta e icono con el apunte completo, pero tiene su propia
`clave` y `prefijo_ls` para que el cache del service worker y el estado en
localStorage no se pisen.
