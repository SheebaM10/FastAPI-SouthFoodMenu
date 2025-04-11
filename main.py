from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

html_path = Path("food.html")
html_content = html_path.read_text(encoding="utf-8")

html_content = html_content.replace('href="styles.css"', 'href="/static/styles.css"')
html_content = html_content.replace('src="images/', 'src="/static/images/')

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse(content=html_content, status_code=200)
