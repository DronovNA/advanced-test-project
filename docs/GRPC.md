# gRPC API Guide

## Overview

This project includes gRPC API for high-performance service-to-service communication.

## Service Definition

### User Service

Defined in `backend/app/api/grpc/protos/user.proto`:

```protobuf
service UserService {
  rpc CreateUser (CreateUserRequest) returns (UserResponse);
  rpc GetUser (GetUserRequest) returns (UserResponse);
  rpc ListUsers (ListUsersRequest) returns (UserListResponse);
}
```

## Running gRPC Server

```bash
cd backend
python -m app.grpc_server
```

Server runs on port `50051`

## Client Usage

### Python Client Example

```python
import grpc
from app.api.grpc.protos import user_pb2, user_pb2_grpc

# Connect to gRPC server
channel = grpc.insecure_channel('localhost:50051')
stub = user_pb2_grpc.UserServiceStub(channel)

# Create user
request = user_pb2.CreateUserRequest(
    email="grpc@example.com",
    username="grpcuser",
    password="password123"
)
response = stub.CreateUser(request)
print(f"User created: {response.id}")

# Get user
request = user_pb2.GetUserRequest(user_id=1)
response = stub.GetUser(request)
print(f"User: {response.username}")
```

## Generating gRPC Code

To regenerate Python code from proto files:

```bash
python -m grpc_tools.protoc \
  --proto_path=backend/app/api/grpc/protos \
  --python_out=backend/app/api/grpc/protos \
  --grpc_python_out=backend/app/api/grpc/protos \
  backend/app/api/grpc/protos/user.proto
```

## Performance Comparison

| Method | Latency | Throughput | Use Case |
|--------|---------|------------|----------|
| REST | ~50ms | 1K req/s | Public APIs |
| gRPC | ~10ms | 10K req/s | Microservices |

## Error Handling

gRPC uses status codes:

```python
try:
    response = stub.GetUser(request)
except grpc.RpcError as e:
    if e.code() == grpc.StatusCode.NOT_FOUND:
        print("User not found")
    elif e.code() == grpc.StatusCode.INTERNAL:
        print(f"Error: {e.details()}")
```

## Testing gRPC

Use `grpcurl` for manual testing:

```bash
# List services
grpcurl -plaintext localhost:50051 list

# Call method
grpcurl -plaintext -d '{"user_id": 1}' \
  localhost:50051 user.UserService/GetUser
```