from fastapi import FastAPI
from app.auth import routers as auth_routers
from app.todo import routers as to_routers
from app.database.database import Base
from app.database.database import engine
app=FastAPI()



@app.get("/")
def cheack():
    return {"fine"}


# Base.metadata.create_all(bind=engine)

app.include_router(auth_routers.router)
app.include_router(to_routers.router)



# ====================
# 2️⃣ main app এ দুইটা model import করতে হবে

# SQLAlchemy যেন দুইটা table register করতে পারে।

# main.py

# from app.database.database import Base
# from app.auth import models as auth_models
# from app.todo import models as todo_models

# এই import খুব important।

# কারণ SQLAlchemy তখন জানবে:

# users table
# todo table