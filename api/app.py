from PIL import Image
import numpy as np
import io
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from api.cam import capture, video

app = FastAPI()


@app.get("/capture")
async def _capture():
    return StreamingResponse(capture(), media_type="image/png")

@app.get("/video")
async def _video():
    return StreamingResponse(video(), media_type="video/mp4")
