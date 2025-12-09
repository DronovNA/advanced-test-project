import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User, Task
import hashlib

@pytest.mark.integration
@pytest.mark.regression
class TestTaskEndpoints:
    """Integration tests for task endpoints"""
    
    @pytest.fixture
    async def user_fixture(self, test_session):
        """Create test user"""
        user = User(
            email="tasktest@example.com",
            username="taskuser",
            hashed_password=hashlib.sha256(b"pass").hexdigest()
        )
        test_session.add(user)
        await test_session.commit()
        await test_session.refresh(user)
        return user
    
    @pytest.mark.asyncio
    @pytest.mark.smoke
    async def test_create_task_endpoint(self, test_client, user_fixture):
        """Test creating task via REST endpoint"""
        payload = {
            "title": "Integration Test Task",
            "description": "Test description",
            "completed": False
        }
        
        response = await test_client.post(
            f"/api/v1/tasks/?owner_id={user_fixture.id}",
            json=payload
        )
        
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Integration Test Task"
        assert data["completed"] is False
    
    @pytest.mark.asyncio
    @pytest.mark.regression
    async def test_update_task_endpoint(self, test_client, test_session, user_fixture):
        """Test updating task via REST endpoint"""
        task = Task(
            title="Original Task",
            owner_id=user_fixture.id,
            completed=False
        )
        test_session.add(task)
        await test_session.commit()
        await test_session.refresh(task)
        
        update_payload = {
            "title": "Updated Task",
            "description": "Updated description",
            "completed": True
        }
        
        response = await test_client.put(
            f"/api/v1/tasks/{task.id}",
            json=update_payload
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated Task"
        assert data["completed"] is True
    
    @pytest.mark.asyncio
    @pytest.mark.smoke
    async def test_list_tasks_endpoint(self, test_client, test_session, user_fixture):
        """Test listing user tasks"""
        for i in range(3):
            task = Task(
                title=f"Task {i+1}",
                owner_id=user_fixture.id,
                completed=i % 2 == 0
            )
            test_session.add(task)
        await test_session.commit()
        
        response = await test_client.get(f"/api/v1/tasks/?owner_id={user_fixture.id}")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 3