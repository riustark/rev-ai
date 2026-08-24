from fastapi import APIRouter
# import the router from the github module
from app.api.routes.github import router as github_router

#create router
api_router = APIRouter()
#include router
api_router.include_router(github_router)