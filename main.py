from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, todos, profile
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

# Define the list of allowed origins
origins = [
    "*",
    "http://localhost:3000/"
]

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def entry():
    return "Welcome to the todo app!!!"

# Include routers
app.include_router(users.user_router, prefix="/users", tags=["users"])
app.include_router(todos.todo_router, prefix="/todos", tags=["todos"])
app.include_router(profile.profile_router, prefix="/profile", tags=["profile"])
