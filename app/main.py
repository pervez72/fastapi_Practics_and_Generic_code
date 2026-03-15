from fastapi import FastAPI
from app.auth import routers as auth_routers
from app.todo import routers as to_routers
from app.database.database import Base
from app.database.database import engine
app=FastAPI()



@app.get("/helthy")
async def health_check():
    return {"status": "helthy"}



# Base.metadata.create_all(bind=engine) // its not use, beacuse i use alembic,so its line not use 

app.include_router(auth_routers.router)
app.include_router(to_routers.router)


