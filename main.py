"""
==============================================================
Project    : AI Fitness Intelligence Platform

Phase      : FastAPI

Module     : Main Application

Author     : Harsh 

Description:
Main entry point of the FastAPI backend.
==============================================================
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ==========================================================
# Import Routers
# ==========================================================

from src.api.routes.ai import router as ai_router
from src.api.routes.auth import router as auth_router
from src.api.routes.health import router as health_router
from src.api.routes.users import router as users_router
from src.api.routes.meals import router as meals_router
from src.api.routes.sleep import router as sleep_router
from src.api.routes.progress import router as progress_router
from src.api.routes.workouts import router as workout_router

# ==========================================================
# Create FastAPI App
# ==========================================================

app = FastAPI(
    title="AI Fitness Intelligence Platform",
    description="AI Powered Fitness Intelligence Platform APIs",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# ==========================================================
# CORS
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================================
# Root
# ==========================================================

@app.get("/", tags=["Root"])
async def root():

    return {
        "application": "AI Fitness Intelligence Platform",
        "version": "1.0.0",
        "status": "Running",
        "swagger": "/docs",
    }


# ==========================================================
# Health
# ==========================================================

@app.get("/health", tags=["Health"])
async def health():

    return {
        "status": "Healthy"
    }


# ==========================================================
# Include Routers
# ==========================================================

app.include_router(auth_router)
app.include_router(ai_router)
app.include_router(users_router)
app.include_router(meals_router)
app.include_router(workout_router)
app.include_router(progress_router)
app.include_router(sleep_router)
app.include_router(health_router)

# ==========================================================
# Startup
# ==========================================================

@app.on_event("startup")
async def startup():

    print("=" * 60)
    print("AI Fitness Intelligence Platform Started")
    print("Server : http://127.0.0.1:8000")
    print("Swagger: http://127.0.0.1:8000/docs")
    print("=" * 60)


# ==========================================================
# Shutdown
# ==========================================================

@app.on_event("shutdown")
async def shutdown():

    print("=" * 60)
    print("Server Stopped")
    print("=" * 60)


# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )