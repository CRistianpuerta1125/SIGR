"""
SIGR — Sistema Integral de Gestión de Restaurante
Aplicación web de propósito académico (Unidad 1 — Gestión del Software).

Versión de línea base: v1.0.0-baseline
Integra cinco módulos: autenticación, menú, pedidos, reservas y caja/reportes.
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "sigr-baseline-demo"

# ------------------------------------------------------------------
# Datos en memoria (línea base: sin base de datos externa todavía)
# ------------------------------------------------------------------
USUARIOS = {
    "admin":  {"clave": "admin123",  "rol": "administrador"},
    "mesero": {"clave": "mesero123", "rol": "mesero"},
    "cliente":{"clave": "cliente123","rol": "cliente"},
}

MENU = [
    {"id": 1, "nombre": "Ceviche de la casa", "categoria": "Entradas", "precio": 28000},
    {"id": 2, "nombre": "Bandeja paisa",      "categoria": "Fuertes",  "precio": 42000},
    {"id": 3, "nombre": "Trucha al ajillo",   "categoria": "Fuertes",  "precio": 38000},
    {"id": 4, "nombre": "Limonada de coco",   "categoria": "Bebidas",  "precio": 11000},
]
PEDIDOS = []
RESERVAS = []
_sec = {"menu": 5, "pedido": 1, "reserva": 1}


def requiere_login(func):
    """Decorador simple de control de acceso."""
    from functools import wraps
    @wraps(func)
    def wrapper(*a, **kw):
        if "usuario" not in session:
            return redirect(url_for("login"))
        return func(*a, **kw)
    return wrapper


# ------------------------------------------------------------------
# Módulo 1 — Autenticación de usuarios
# ------------------------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form.get("usuario", "")
        c = request.form.get("clave", "")
        if u in USUARIOS and USUARIOS[u]["clave"] == c:
            session["usuario"] = u
            session["rol"] = USUARIOS[u]["rol"]
            return redirect(url_for("panel"))
        flash("Usuario o contraseña incorrectos.")
    return render_template("login.html")


@app.route("/salir")
def salir():
    session.clear()
    return redirect(url_for("login"))


@app.route("/panel")
@requiere_login
def panel():
    return render_template("panel.html", rol=session.get("rol"))


# ------------------------------------------------------------------
# Módulo 2 — Menú digital (CRUD de platos)
# ------------------------------------------------------------------
@app.route("/menu")
@requiere_login
def menu():
    return render_template("menu.html", menu=MENU)


@app.route("/menu/agregar", methods=["POST"])
@requiere_login
def menu_agregar():
    MENU.append({
        "id": _sec["menu"],
        "nombre": request.form.get("nombre", "Sin nombre"),
        "categoria": request.form.get("categoria", "General"),
        "precio": int(request.form.get("precio") or 0),
    })
    _sec["menu"] += 1
    return redirect(url_for("menu"))


@app.route("/menu/eliminar/<int:pid>")
@requiere_login
def menu_eliminar(pid):
    global MENU
    MENU = [m for m in MENU if m["id"] != pid]
    return redirect(url_for("menu"))


# ------------------------------------------------------------------
# Módulo 3 — Pedidos (registro y seguimiento)
# ------------------------------------------------------------------
@app.route("/pedidos")
@requiere_login
def pedidos():
    return render_template("pedidos.html", pedidos=PEDIDOS, menu=MENU)


@app.route("/pedidos/crear", methods=["POST"])
@requiere_login
def pedidos_crear():
    plato = request.form.get("plato", "")
    PEDIDOS.append({
        "id": _sec["pedido"], "plato": plato,
        "estado": "En preparación",
        "hora": datetime.now().strftime("%H:%M"),
    })
    _sec["pedido"] += 1
    return redirect(url_for("pedidos"))


@app.route("/pedidos/listo/<int:pid>")
@requiere_login
def pedidos_listo(pid):
    for p in PEDIDOS:
        if p["id"] == pid:
            p["estado"] = "Entregado"
    return redirect(url_for("pedidos"))


# ------------------------------------------------------------------
# Módulo 4 — Reservas (por fecha y hora)
# ------------------------------------------------------------------
@app.route("/reservas")
@requiere_login
def reservas():
    return render_template("reservas.html", reservas=RESERVAS)


@app.route("/reservas/crear", methods=["POST"])
@requiere_login
def reservas_crear():
    RESERVAS.append({
        "id": _sec["reserva"],
        "nombre": request.form.get("nombre", ""),
        "fecha": request.form.get("fecha", ""),
        "hora": request.form.get("hora", ""),
        "personas": request.form.get("personas", "2"),
    })
    _sec["reserva"] += 1
    return redirect(url_for("reservas"))


# ------------------------------------------------------------------
# Módulo 5 — Cierre de caja y reportes
# ------------------------------------------------------------------
@app.route("/caja")
@requiere_login
def caja():
    entregados = [p for p in PEDIDOS if p["estado"] == "Entregado"]
    precios = {m["nombre"]: m["precio"] for m in MENU}
    total = sum(precios.get(p["plato"], 0) for p in entregados)
    return render_template("caja.html", entregados=entregados,
                           total=total, cantidad=len(entregados),
                           fecha=datetime.now().strftime("%d/%m/%Y"))


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
