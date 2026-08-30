"""Config de este apunte para motor_apuntes. Ver contrato-fragmento.md del
paquete (motor_apuntes) para el vocabulario de los fragmentos.

Apunte del Taller de Seguridad Informática (TA051, cátedra Méndez, Di Paola).
Una sola salida: el apunte completo (fuentes/completo/ -> ./). Se arma con
motor_apuntes.armar.construir(). Los capitulos se van sumando clase a clase;
CFG["grupos"] lista solo los que ya tienen fragmento.

Paleta: propia de la materia (amarillo/ambar sobre neutros frios, tono de alerta), pensada para que se distinga de las otras materias de la
plataforma. Tema de seguridad, no reutiliza la turquesa de otro apunte.
"""

PALETA_LIGHT = """:root {
      color-scheme: light;
      --bg: #f7f5ec;
      --surface: #ffffff;
      --surface-2: #efeadb;
      --ink: #221f14;
      --muted: #6d6752;
      --line: #e4dfcd;
      --accent: #9a7d0a;
      --accent-2: #faedc4;
      --accent-ink: #6b5300;
      --warm: #9a5a12;
      --warm-bg: #fdeecf;
      --danger: #a33540;
      --danger-bg: #fbe7e9;
      --blue: #2f6f8f;
      --blue-bg: #e2f0f6;
      --ok: #35704a;
      --ok-bg: #e6f4ea;
      --exam: #8a3b86;
      --exam-bg: #f8e8f6;
      --hl-yellow: #ffe08a;
      --hl-mint: #a7ead2;
      --hl-pink: #ffc1d2;
      --hl-blue: #bcd7ff;
      --shadow: 0 18px 55px rgba(48, 40, 12, .09);
      --radius: 18px;
      --sidebar: 292px;
    }"""

PALETA_DARK = """html[data-theme="dark"] {
      color-scheme: dark;
      --bg: #14110a;
      --surface: #1c1810;
      --surface-2: #272013;
      --ink: #f4efe2;
      --muted: #b2a98f;
      --line: #372f1c;
      --accent: #e8c552;
      --accent-2: #38300f;
      --accent-ink: #f6e6a6;
      --warm: #f0b766;
      --warm-bg: #392a17;
      --danger: #f19aa2;
      --danger-bg: #3c2125;
      --blue: #86bdd6;
      --blue-bg: #163040;
      --ok: #86cf9b;
      --ok-bg: #182f21;
      --exam: #e29ad8;
      --exam-bg: #371f34;
      --hl-yellow: #725d19;
      --hl-mint: #185a4d;
      --hl-pink: #71384b;
      --hl-blue: #294f78;
      --shadow: 0 18px 55px rgba(0, 0, 0, .26);
    }"""

_CLASES = [
    ("threatmodel", "1", "Threat model, mecanismos y politicas"),
    ("offense", "2", "Ofensiva: red team, pentester y researcher"),
]

_LAB = [
    ("permisos", "A", "Permisos de Unix: identidad, claves y secretos"),
    ("escalada", "B", "Escalada de privilegios: sudo y setuid"),
]

CFG = {
    "clave": "seg",
    "codigo": "TA051",
    "catedra": "Méndez",
    "autores": ["flopeztancredi"],
    "prefijo_ls": "seg",
    "titulo_tab": "Taller de Seguridad - Apunte",
    "marca": "Taller de Seguridad",
    "h1": "Taller de Seguridad Informática",
    "hero": ("Apunte del Taller de Seguridad (TA051, cátedra Méndez, FIUBA). "
             "Clase por clase, con lo hablado en las notas del docente y los "
             "casos de las diapositivas, listo para el parcialito. Arranca "
             "por el threat model y la ofensiva de un pentest."),
    "descripcion": "Apunte del Taller de Seguridad Informática (TA051, FIUBA).",
    "theme_color": "#b58900",
    "favicon_hex": "b58900",
    "grupos": [
        ("Fundamentos", _CLASES[0:2]),
        ("Laboratorio", _LAB),
    ],
    "paleta_light": PALETA_LIGHT,
    "paleta_dark": PALETA_DARK,
}
