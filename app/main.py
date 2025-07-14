from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import resume, user, auth

app = FastAPI(
    title="Resume Builder API",
    version="1.0.0",
    description="Backend for parsing resumes and generating suggestions",
)

# CORS settings (allow frontend dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include versioned routes
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(resume.router, prefix="/api/v1/resumes", tags=["Resumes"])

@app.get("/")
def root():
    return {"message": "Resume Builder API is live 🚀"}
