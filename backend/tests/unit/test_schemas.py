import pytest
from pydantic import ValidationError
from app.schemas import UserCreate, TaskCreate

@pytest.mark.unit
class TestSchemaValidation:
    """Unit tests for schema validation"""
    
    def test_user_create_valid(self):
        """Test valid UserCreate schema"""
        user = UserCreate(
            email="test@example.com",
            username="testuser",
            password="password123"
        )
        assert user.email == "test@example.com"
        assert user.username == "testuser"
    
    def test_user_create_invalid_email(self):
        """Test UserCreate with invalid email"""
        with pytest.raises(ValidationError):
            UserCreate(
                email="invalid-email",
                username="testuser",
                password="password123"
            )
    
    def test_task_create_valid(self):
        """Test valid TaskCreate schema"""
        task = TaskCreate(
            title="Test Task",
            description="Description",
            completed=False
        )
        assert task.title == "Test Task"
        assert task.completed is False
    
    @pytest.mark.regression
    def test_task_create_empty_title(self):
        """Test TaskCreate with empty title"""
        with pytest.raises(ValidationError):
            TaskCreate(
                title="",
                description="Description"
            )