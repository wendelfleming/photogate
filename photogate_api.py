import photogate_SC20
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
photogate_SC20 = photogate_SC20.Photogate_SC20(gate_0_pin=17, gate_1_pin=27, gate_distance=0.02)

# Allows cross server API call
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/run")
async def run():
    photogate_SC20.reset()
    speed = photogate_SC20.measure_speed()
    return {"speed": speed}




