from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "contexto.politico" / "content"


def test_article_page_exists_and_uses_query_param():
    article_page = CONTENT_DIR / "articulo.html"
    assert article_page.exists(), "Falta la página de detalle de la nota"

    html = article_page.read_text(encoding="utf-8")
    assert "id=" in html, "La página de detalle debe leer el parámetro id de la URL"
    assert "manifest.json" in html or "fetch(" in html, "La página debe cargar datos desde el manifiesto o un JSON"


def test_manifest_points_to_existing_notes():
    manifest = CONTENT_DIR / "noticias" / "manifest.json"
    assert manifest.exists(), "Falta el manifiesto de noticias"

    import json

    data = json.loads(manifest.read_text(encoding="utf-8"))
    for item in data["portada"]:
        note_file = CONTENT_DIR / "noticias" / f"{item['id']}.json"
        assert note_file.exists(), f"No existe el archivo de la nota {item['id']}"
