# SIGR — Sistema Integral de Gestión de Restaurante

Aplicación web de propósito académico para la gestión operativa de un restaurante,
desarrollada para la asignatura **Gestión del Software**. Este repositorio contiene
la **línea base v1.0.0-baseline** del código fuente.

## Módulos incluidos
1. **Autenticación de usuarios** — acceso por rol (administrador, mesero, cliente).
2. **Menú digital** — CRUD de platos y categorías.
3. **Pedidos** — registro y seguimiento de pedidos en tiempo real.
4. **Reservas** — gestión de reservas por fecha y hora.
5. **Cierre de caja y reportes** — total de ventas y pedidos del día.

## Requisitos
- Python 3.10 o superior
- Flask

## Instalación y ejecución
```bash
git clone https://github.com/CRistianpuerta1125/SIGR.git
cd SIGR
pip install -r requirements.txt
python app/app.py
```
Luego abra en el navegador: http://127.0.0.1:5000

## Usuarios de prueba
| Usuario  | Contraseña  | Rol           |
|----------|-------------|---------------|
| admin    | admin123    | administrador |
| mesero   | mesero123   | mesero        |
| cliente  | cliente123  | cliente       |

## Estructura del proyecto
```
SIGR/
├── app/
│   ├── app.py            # Lógica y rutas de los 5 módulos
│   └── templates/        # Vistas HTML (Jinja2)
├── docs/
│   ├── modelo_datos.md   # Estructura de la base de datos
│   └── despliegue.md     # Manual de despliegue
├── README.md
├── CHANGELOG.md
├── LICENSE.txt
└── requirements.txt
```

## Licencia
Distribuido bajo licencia MIT. Ver `LICENSE.txt`.
