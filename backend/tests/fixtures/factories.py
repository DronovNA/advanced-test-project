from app.models import User, Task
from app.schemas import UserCreate, TaskCreate
import hashlib
from typing import Optional

class UserFactory:
    """Factory for creating test User objects"""
    
    _counter = 0
    
    @classmethod
    def create(
        cls,
        email: Optional[str] = None,
        username: Optional[str] = None,
        is_active: bool = True
    ) -> User:
        cls._counter += 1
        return User(
            email=email or f"user{cls._counter}@test.com",
            username=username or f"user{cls._counter}",
            hashed_password=hashlib.sha256(b"password").hexdigest(),
            is_active=is_active
        )
    
    @classmethod
    def create_schema(cls, **kwargs) -> UserCreate:
        return UserCreate(
            email=kwargs.get("email", f"user{cls._counter}@test.com"),
            username=kwargs.get("username", f"user{cls._counter}"),
            password="password123"
        )

class TaskFactory:
    """Factory for creating test Task objects"""
    
    _counter = 0
    
    @classmethod
    def create(
        cls,
        title: Optional[str] = None,
        owner_id: int = 1,
        completed: bool = False
    ) -> Task:
        cls._counter += 1
        return Task(
            title=title or f"Task {cls._counter}",
            description=f"Test task {cls._counter}",
            owner_id=owner_id,
            completed=completed
        )
    
    @classmethod
    def create_schema(cls, **kwargs) -> TaskCreate:
        return TaskCreate(
            title=kwargs.get("title", f"Task {cls._counter}"),
            description=kwargs.get("description", "Test"),
            completed=kwargs.get("completed", False)
        )