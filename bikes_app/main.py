from fastapi import FastAPI, HTTPException
from routes import bike_routes, client_routes, partner_routes

import uvicorn

app = FastAPI()
app.include_router(bike_routes)
app.include_router(client_routes)
app.include_router(partner_routes)
if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True, host='127.0.0.1', port=8001)
