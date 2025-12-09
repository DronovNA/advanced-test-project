import pytest
from app.models import User, Task
from sqlalchemy.ext.asyncio import AsyncSession
import hashlib

@pytest.fixture
async def sample_user(test_session: AsyncSession) -> User:
    """Create sample user for tests"""
    user = User(
        email="sample@test.com",
        username="sampleuser",
        hashed_password=hashlib.sha256(b"password").hexdigest()
    )
    test_session.add(user)
    await test_session.commit()
    await test_session.refresh(user)
    return user

@pytest.fixture
async def sample_tasks(sample_user: User, test_session: AsyncSession) -> list[Task]:
    """Create sample tasks for tests"""
    tasks = [
        Task(
            title="Sample Task 1",
            description="First task",
            owner_id=sample_user.id,
            completed=False
        ),
        Task(
            title="Sample Task 2",
            description="Second task",
            owner_id=sample_user.id,
            completed=True
        ),
    ]
    test_session.add_all(tasks)
    await test_session.commit()
    for task in tasks:
        await test_session.refresh(task)
    return tasks