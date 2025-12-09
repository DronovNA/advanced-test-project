import grpc
import asyncio
from concurrent import futures
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.api.grpc.services.user_service import UserServicer

async def serve():
    """Start gRPC server"""
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Note: Actual gRPC service registration requires generated pb2_grpc code
    # This is a placeholder structure showing how it would be implemented
    
    server.add_insecure_port('[::]:50051')
    print("gRPC server starting on port 50051...")
    await server.start()
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(serve())