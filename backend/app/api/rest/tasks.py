from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import TaskCreate, TaskRead
from app.services.task_service import TaskService

router = APIRouter()

@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(task_data: TaskCreate, owner_id: int, db: AsyncSession = Depends(get_db)):
    service = TaskService(db)
    return await service.create_task(task_data, owner_id)

@router.get("/{task_id}", response_model=TaskRead)
async def get_task(task_id: int, db: AsyncSession = Depends(get_db)):
    service = TaskService(db)
    task = await service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("/", response_model=list[TaskRead])
async def list_tasks(owner_id: int, skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    service = TaskService(db)
    return await service.list_tasks(owner_id, skip, limit)

@router.put("/{task_id}", response_model=TaskRead)
async def update_task(task_id: int, task_data: TaskCreate, db: AsyncSession = Depends(get_db)):
    service = TaskService(db)
    task = await service.update_task(task_id, task_data)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task