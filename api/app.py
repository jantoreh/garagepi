import io

import numpy as np
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from api.cam import convert_numpy_image_to_bytes, get_single_image

app = FastAPI()


@app.get("/capture")
async def _capture():
    image = get_single_image()
    image = convert_numpy_image_to_bytes(image)
    return StreamingResponse(image, media_type="image/png")
