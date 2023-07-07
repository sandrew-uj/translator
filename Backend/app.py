from pydantic import BaseModel
from typing import Any, Dict

from fastapi import FastAPI

from utils import get_translation

app = FastAPI(title="translator_server")


class Translator(BaseModel):
    text: str
    to_language: str


@app.post("/translate_text")
async def translate_handler(translator: Translator):
    return get_translation(translator.text, translator.to_language)
