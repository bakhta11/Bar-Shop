from fastapi import FastAPI
from app.db import init_db
from app.routes import auth_routes, product_routes, cart_routes
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Bar-Shop Project",
    lifespan=lifespan
)

app.include_router(auth_routes.router)
app.include_router(product_routes.router)
app.include_router(cart_routes.router)


@app.get("/")
def root():
    return {"msg": "Bar-Shop backend running"}



#from fastapi import FastAPI
#from .db import init_db
#from .routes import auth_routes, product_routes, cart_routes

#app = FastAPI(title='Bar-Shop Project')

#app.include_router(auth_routes.router)
#app.include_router(product_routes.router)
#app.include_router(cart_routes.router)

#@app.on_event('startup')
#def on_startup():
#    init_db()

#@app.get('/')
#def root():
#    return {"msg": "Bar-Shop backend running"}
