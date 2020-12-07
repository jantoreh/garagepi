from PIL import Image
import numpy as np
import io
from fastapi import FastAPI
from .cam import capture

app = FastAPI()


@app.get("/")
async def test():
    return {"message": "Hello World"}


@app.get("/capture")
async def _capture():
    return capture()
