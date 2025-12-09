import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User
from app.database import get_db

@pytest.mark.integration
@pytest.mark.regression
class TestUserEndpoints:
    """Integration tests for user endpoints"""
    
    @pytest.mark.asyncio
    @pytest.mark.smoke
    async def test_create_user_endpoint(self, test_client):
        """Test creating user via REST endpoint"""
        payload = {
            "email": "integration@example.com",
            "username": "integrationuser",
            "password": "password123"
        }
        
        response = await test_client.post("/api/v1/users/", json=payload)
        
        assert response.status_code == 201
        data = response.json()
        assert data["email"] == "integration@example.com"
        assert data["username"] == "integrationuser"
        assert "id" in data
    
    @pytest.mark.asyncio
    @pytest.mark.smoke
    async def test_get_user_endpoint(self, test_client, test_session):
        """Test getting user via REST endpoint"""
        import hashlib
        
        user = User(
            email="gettest@example.com",
            username="getuser",
            hashed_password=hashlib.sha256(b"pass").hexdigest()
        )
        test_session.add(user)
        await test_session.commit()
        await test_session.refresh(user)
        
        response = await test_client.get(f"/api/v1/users/{user.id}")
        
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == "gettest@example.com"
    
    @pytest.mark.asyncio
    @pytest.mark.regression
    async def test_create_duplicate_user(self, test_client):
        """Test creating duplicate user returns error"""
        payload = {
            "email": "duplicate@example.com",
            "username": "dupuser1",
            "password": "password123"
        }
        
        await test_client.post("/api/v1/users/", json=payload)
        response = await test_client.post("/api/v1/users/", json=payload)
        
        assert response.status_code == 400
    
    @pytest.mark.asyncio
    @pytest.mark.regression
    async def test_get_nonexistent_user(self, test_client):
        """Test getting non-existent user returns 404"""
        response = await test_client.get("/api/v1/users/99999")
        
        assert response.status_code == 404