import pytest
from app.models import User
import hashlib

@pytest.mark.e2e
@pytest.mark.regression
class TestTaskWorkflow:
    """E2E tests for task workflows"""
    
    @pytest.mark.asyncio
    @pytest.mark.smoke
    async def test_complete_task_lifecycle(self, test_client, test_session):
        """Test complete task creation, update, and retrieval workflow"""
        
        user = User(
            email="taskworkflow@example.com",
            username="taskworkflow",
            hashed_password=hashlib.sha256(b"pass").hexdigest()
        )
        test_session.add(user)
        await test_session.commit()
        await test_session.refresh(user)
        
        create_payload = {
            "title": "Workflow Task",
            "description": "Test task",
            "completed": False
        }
        
        create_response = await test_client.post(
            f"/api/v1/tasks/?owner_id={user.id}",
            json=create_payload
        )
        assert create_response.status_code == 201
        
        task_id = create_response.json()["id"]
        
        update_payload = {
            "title": "Workflow Task Updated",
            "description": "Updated",
            "completed": True
        }
        
        update_response = await test_client.put(
            f"/api/v1/tasks/{task_id}",
            json=update_payload
        )
        assert update_response.status_code == 200
        assert update_response.json()["completed"] is True
        
        get_response = await test_client.get(f"/api/v1/tasks/{task_id}")
        assert get_response.status_code == 200
        assert get_response.json()["title"] == "Workflow Task Updated"