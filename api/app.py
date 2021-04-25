import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from api.cam import convert_image_to_bytes, get_single_image
from api.garage_doors import trigger_right_garage_door

app = FastAPI()


@app.get("/alive")
async def _alive():
    return "Hi"


@app.get("/capture")
async def _capture():
    image = get_single_image()
    image = convert_image_to_bytes(image)
    return StreamingResponse(image, media_type="image/png")


@app.get("/door", status_code=200)
async def _trigger_door():
    trigger_right_garage_door()
    return



if __name__ == "__main__":
    uvicorn.run("api.app:app", port=5000, host="0.0.0.0")