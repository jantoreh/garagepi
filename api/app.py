import io

import numpy as np
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from api.cam import convert_image_to_bytes, get_single_image

app = FastAPI()


@app.get("/capture")
async def _capture():
    image = get_single_image()
    image = convert_image_to_bytes(image)
    return StreamingResponse(image, media_type="image/png")


if __name__ == "__main__":
    uvicorn.run("api.app:app", port=5000, host="0.0.0.0")