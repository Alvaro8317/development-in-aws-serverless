from fastapi import FastAPI
from fastapi import responses

from src.controllers.item_controller import router
from src.templates import root_template

app = FastAPI()

app.include_router(router)

@app.get("/", response_class=responses.HTMLResponse)
async def root():
    return responses.HTMLResponse(root_template.get_root_html())