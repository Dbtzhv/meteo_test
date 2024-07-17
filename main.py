import uvicorn
from fastapi import FastAPI

from routes.weather import weather_router

app = FastAPI()
app.include_router(weather_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )

