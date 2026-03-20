from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

imac_unlock_status = False
@app.get("/unlock-imac")
def unlock_Imac():
    global imac_unlock_status
    imac_unlock_status = True
    return {"status": "unlocking_imac"}

@app.get("/imac-unlock-status")
def imac_unlock_status():
    global imac_unlock_status
    if imac_unlock_status:
        imac_unlock_status = False
        return True
    else:
        return False
    


garage_status = False
car_status = False
open_all = False
g_stat = False  # tempary varibles
c_stat = False  # tempary varibles

@app.get("/garage-and-car-status")
def get_garage_status():
    global garage_status, car_status
    if garage_status:
        g_stat = True
        garage_status = False
    else:
        g_stat = False
    if car_status:
        c_stat = True
        car_status = False
    else:
        c_stat = False
    return {"car": c_stat, "garage": g_stat}



@app.get("/open-garage")
def open_garage():
    global garage_status
    garage_status = True
    return {"status": "opening garage"}

@app.get("/close-garage")
def close_garage():
    global garage_status
    garage_status = True
    return {"status": "closing garage"}

@app.get("/start-car")
def start_car():
    global car_status
    car_status = True
    return {"status": "starting car"}

@app.get("/stop-car")
def start_car():
    global car_status
    car_status = True
    return {"status": "stopping car"}

@app.get("/open-both")
def both():
    global garage_status, car_status
    garage_status = True
    car_status = True
    return {"status": "opening both"}


routes = []
for route in app.routes:
    hi = ["/openapi.json", "/docs", "/docs/oauth2-redirect", "/redoc"]
    if route.path not in hi:
        print("http://127.0.0.1:8000"+route.path)
        if route.path not in routes:
            routes.append(route.path)



@app.get("/endpoints")
def get_endpoints():
    global routes
    return routes


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
"""
if __name__ == "__main__":
    uvicorn.run("everything_api:app", host="127.0.0.1", port=8000, reload=True)

"""