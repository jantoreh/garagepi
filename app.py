import uvicorn
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from lib.garage_doors import trigger_right_garage_door, trigger_left_garage_door
from lib.camera import detect_cars

app = FastAPI()


@app.get("/alive")
async def _alive():
    return "Hi"


@app.get("/door/right", status_code=200)
async def _trigger_door():
    trigger_right_garage_door()
    return "Right door triggered"


@app.get("/door/left", status_code=200)
async def _trigger_door():
    trigger_left_garage_door()
    return "Left door triggered"


@app.get("/camera/capture", status_code=200)
@app.on_event("startup")
@repeat_every(seconds=2)
async def _capture_image():
    detect_cars()
    return "Captured new image"


if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, host="0.0.0.0")
