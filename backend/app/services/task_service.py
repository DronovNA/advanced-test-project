from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import Task
from app.schemas import TaskCreate

class TaskService:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create_task(self, task_data: TaskCreate, owner_id: int) -> Task:
        db_task = Task(
            title=task_data.title,
            description=task_data.description,
            owner_id=owner_id,
            completed=task_data.completed
        )
        self.db.add(db_task)
        await self.db.commit()
        await self.db.refresh(db_task)
        return db_task
    
    async def get_task(self, task_id: int) -> Task | None:
        result = await self.db.execute(
            select(Task).where(Task.id == task_id)
        )
        return result.scalars().first()
    
    async def list_tasks(self, owner_id: int, skip: int = 0, limit: int = 10):
        result = await self.db.execute(
            select(Task).where(Task.owner_id == owner_id).offset(skip).limit(limit)
        )
        return result.scalars().all()
    
    async def update_task(self, task_id: int, task_data: TaskCreate) -> Task | None:
        db_task = await self.get_task(task_id)
        if not db_task:
            return None
        db_task.title = task_data.title
        db_task.description = task_data.description
        db_task.completed = task_data.completed
        await self.db.commit()
        await self.db.refresh(db_task)
        return db_task