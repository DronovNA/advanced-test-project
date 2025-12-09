import pytest
from unittest.mock import AsyncMock, MagicMock
from app.services.task_service import TaskService
from app.schemas import TaskCreate
from app.models import Task

@pytest.mark.unit
class TestTaskService:
    """Unit tests for TaskService"""
    
    @pytest.mark.asyncio
    async def test_create_task_success(self):
        """Test successful task creation"""
        db_mock = AsyncMock()
        service = TaskService(db_mock)
        
        task_data = TaskCreate(
            title="Test Task",
            description="Test Description",
            completed=False
        )
        
        async def mock_refresh(obj):
            obj.id = 1
        
        db_mock.refresh = mock_refresh
        db_mock.add = MagicMock()
        db_mock.commit = AsyncMock()
        
        result = await service.create_task(task_data, owner_id=1)
        
        db_mock.add.assert_called_once()
        db_mock.commit.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_list_tasks_by_owner(self):
        """Test listing tasks by owner"""
        db_mock = AsyncMock()
        service = TaskService(db_mock)
        
        tasks = [
            Task(id=1, title="Task 1", owner_id=1, completed=False),
            Task(id=2, title="Task 2", owner_id=1, completed=True),
        ]
        
        result_mock = MagicMock()
        result_mock.scalars().all.return_value = tasks
        db_mock.execute.return_value = result_mock
        
        result = await service.list_tasks(owner_id=1)
        
        assert len(result) == 2
        assert result[0].title == "Task 1"

@pytest.mark.unit
@pytest.mark.regression
class TestTaskServiceUpdate:
    """Unit tests for task update functionality"""
    
    @pytest.mark.asyncio
    async def test_update_task_success(self):
        """Test successful task update"""
        db_mock = AsyncMock()
        service = TaskService(db_mock)
        
        original_task = Task(
            id=1,
            title="Original",
            owner_id=1,
            completed=False
        )
        
        result_mock = MagicMock()
        result_mock.scalars().first.return_value = original_task
        db_mock.execute.return_value = result_mock
        
        async def mock_refresh(obj):
            pass
        
        db_mock.refresh = mock_refresh
        db_mock.commit = AsyncMock()
        
        update_data = TaskCreate(title="Updated", description="New desc", completed=True)
        result = await service.update_task(1, update_data)
        
        db_mock.commit.assert_called_once()