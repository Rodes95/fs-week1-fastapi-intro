from app.routers.items import router as item_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Connects the items endpoints with app
app.include_router(item_router)

origins = [
     "http://127.0.0.1:5173", # Vite
     "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Main Page
@app.get("/")
def root():
    return {"message": "Hello, Ro"}

# Check Page Status
@app.get("/health")
def health():
    return {"status": "ok"}