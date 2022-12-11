import uvicorn
from fastapi import FastAPI

from lib.garage_doors import trigger_right_garage_door

app = FastAPI()


@app.get("/alive")
async def _alive():
    return "Hi"


@app.get("/door", status_code=200)
async def _trigger_door():
    trigger_right_garage_door()
    return "Something happening?"


if __name__ == "__main__":
    uvicorn.run("api.app:app", port=5000, host="0.0.0.0")
