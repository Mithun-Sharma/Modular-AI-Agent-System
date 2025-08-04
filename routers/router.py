from fastapi import APIRouter, Request
from pydantic import BaseModel
from agents.routing_agent import route_task

router = APIRouter()

class TaskRequest(BaseModel):
    task_type: str
    content: str

@router.post("/agent/")
async def handle_task(request: TaskRequest):
    response = route_task(request.task_type, request.content)
    return {"response": response}