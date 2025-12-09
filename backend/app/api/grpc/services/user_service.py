import grpc
from app.services.user_service import UserService
from app.database import get_db
import hashlib

class UserServicer:
    """gRPC User Service implementation"""
    
    def __init__(self):
        self.user_service = UserService()
    
    async def CreateUser(self, request, context):
        """Create new user via gRPC"""
        try:
            async for session in get_db():
                hashed_password = hashlib.sha256(request.password.encode()).hexdigest()
                user = await self.user_service.create_user(
                    session=session,
                    email=request.email,
                    username=request.username,
                    hashed_password=hashed_password
                )
                
                return {
                    "id": user.id,
                    "email": user.email,
                    "username": user.username,
                    "is_active": user.is_active,
                    "created_at": user.created_at.isoformat()
                }
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))
    
    async def GetUser(self, request, context):
        """Get user by ID via gRPC"""
        try:
            async for session in get_db():
                user = await self.user_service.get_user(session, request.user_id)
                
                if not user:
                    context.abort(grpc.StatusCode.NOT_FOUND, "User not found")
                
                return {
                    "id": user.id,
                    "email": user.email,
                    "username": user.username,
                    "is_active": user.is_active,
                    "created_at": user.created_at.isoformat()
                }
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))
    
    async def ListUsers(self, request, context):
        """List users with pagination via gRPC"""
        try:
            async for session in get_db():
                users = await self.user_service.list_users(
                    session,
                    limit=request.limit or 10,
                    offset=request.offset or 0
                )
                
                user_responses = [
                    {
                        "id": user.id,
                        "email": user.email,
                        "username": user.username,
                        "is_active": user.is_active,
                        "created_at": user.created_at.isoformat()
                    }
                    for user in users
                ]
                
                return {
                    "users": user_responses,
                    "total": len(user_responses)
                }
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))