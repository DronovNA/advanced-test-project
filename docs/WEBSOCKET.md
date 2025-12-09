# WebSocket API Guide

## Overview

WebSocket endpoint provides real-time updates for task changes.

## Endpoint

```
ws://localhost:8000/ws/tasks/{user_id}
```

## Connection

### JavaScript Client

```javascript
const ws = new WebSocket('ws://localhost:8000/ws/tasks/1');

ws.onopen = () => {
  console.log('Connected to WebSocket');
};

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Received:', data);
  
  if (data.event === 'task_created') {
    // Update UI with new task
    addTaskToList(data.task);
  }
};

ws.onerror = (error) => {
  console.error('WebSocket error:', error);
};

ws.onclose = () => {
  console.log('Disconnected from WebSocket');
};
```

### Python Client

```python
import asyncio
import websockets
import json

async def connect():
    uri = "ws://localhost:8000/ws/tasks/1"
    async with websockets.connect(uri) as websocket:
        # Send message
        await websocket.send(json.dumps({
            "type": "task_created",
            "task": {"id": 1, "title": "New Task"}
        }))
        
        # Receive message
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.run(connect())
```

## Message Format

### Task Created
```json
{
  "type": "task_created",
  "task": {
    "id": 1,
    "title": "New Task",
    "completed": false
  }
}
```

### Task Updated
```json
{
  "type": "task_updated",
  "task": {
    "id": 1,
    "title": "Updated Task",
    "completed": true
  }
}
```

## Testing WebSocket

```bash
# Using wscat
npm install -g wscat
wscat -c ws://localhost:8000/ws/tasks/1
```

## Use Cases

1. **Real-time task updates** - Notify users when tasks change
2. **Collaborative editing** - Multiple users editing same task list
3. **Live notifications** - Push notifications without polling