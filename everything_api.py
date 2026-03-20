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