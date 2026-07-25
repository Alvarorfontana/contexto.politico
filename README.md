# Contexto Político

## Ejecutar localmente

1. Abrir la terminal en la raíz del proyecto.
2. Ejecutar:
   ```bash
   python serve.py
   ```
3. Abrir en el navegador:
   ```text
   http://127.0.0.1:8000/index.html
   ```

## Estructura actual

- content/index.html: portada del portal.
- content/articulo.html: página de detalle por id.
- content/noticias/: archivos JSON de las noticias.

## Futura base de datos

Cuando el volumen de noticias crezca, conviene reemplazar los JSON estáticos por un backend que exponga una API REST y almacene las notas en una base de datos como PostgreSQL o SQLite. El flujo sería:

1. El frontend solicita /api/noticias/:id.
2. El backend consulta la base de datos.
3. La página de detalle renderiza la respuesta de la API.
