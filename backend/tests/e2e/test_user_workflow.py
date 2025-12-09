import pytest
from sqlalchemy.ext.asyncio import AsyncSession

@pytest.mark.e2e
@pytest.mark.regression
class TestUserWorkflow:
    """E2E tests for user workflows"""
    
    @pytest.mark.asyncio
    @pytest.mark.smoke
    async def test_complete_user_lifecycle(self, test_client, test_session):
        """Test complete user creation and retrieval workflow"""
        
        user_payload = {
            "email": "e2e@example.com",
            "username": "e2euser",
            "password": "password123"
        }
        
        create_response = await test_client.post("/api/v1/users/", json=user_payload)
        assert create_response.status_code == 201
        
        user_id = create_response.json()["id"]
        
        get_response = await test_client.get(f"/api/v1/users/{user_id}")
        assert get_response.status_code == 200
        
        retrieved_user = get_response.json()
        assert retrieved_user["email"] == "e2e@example.com"
        assert retrieved_user["username"] == "e2euser"