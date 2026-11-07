# Manual de despliegue — SIGR

## Entorno local
1. Instalar Python 3.10+.
2. Clonar el repositorio y entrar a la carpeta.
3. Instalar dependencias: `pip install -r requirements.txt`
4. Ejecutar: `python app/app.py`
5. Abrir http://127.0.0.1:5000

## Notas
- La línea base usa el servidor de desarrollo de Flask.
- Para producción se recomienda Gunicorn + Nginx (iteración futura).
