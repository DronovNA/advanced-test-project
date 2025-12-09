import pytest
from unittest.mock import AsyncMock, MagicMock
from app.services.user_service import UserService
from app.schemas import UserCreate
from app.models import User

@pytest.mark.unit
class TestUserService:
    """Unit tests for UserService"""
    
    @pytest.mark.asyncio
    async def test_create_user_success(self):
        """Test successful user creation"""
        db_mock = AsyncMock()
        service = UserService(db_mock)
        
        user_data = UserCreate(
            email="test@example.com",
            username="testuser",
            password="password123"
        )
        
        new_user = User(
            id=1,
            email="test@example.com",
            username="testuser",
            hashed_password="hashed_pass"
        )
        
        async def mock_refresh(obj):
            obj.id = 1
        
        db_mock.refresh = mock_refresh
        db_mock.add = MagicMock()
        db_mock.commit = AsyncMock()
        
        result = await service.create_user(user_data)
        
        db_mock.add.assert_called_once()
        db_mock.commit.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_get_user_by_email(self):
        """Test retrieving user by email"""
        db_mock = AsyncMock()
        service = UserService(db_mock)
        
        user = User(
            id=1,
            email="test@example.com",
            username="testuser",
            hashed_password="hashed"
        )
        
        result_mock = MagicMock()
        result_mock.scalars().first.return_value = user
        db_mock.execute.return_value = result_mock
        
        result = await service.get_user_by_email("test@example.com")
        
        assert result == user
        db_mock.execute.assert_called_once()

@pytest.mark.unit
@pytest.mark.regression
class TestUserServiceEdgeCases:
    """Unit tests for UserService edge cases"""
    
    @pytest.mark.asyncio
    async def test_get_nonexistent_user(self):
        """Test getting non-existent user returns None"""
        db_mock = AsyncMock()
        service = UserService(db_mock)
        
        result_mock = MagicMock()
        result_mock.scalars().first.return_value = None
        db_mock.execute.return_value = result_mock
        
        result = await service.get_user(999)
        
        assert result is None