# Advanced Test Project - Frontend

React + TypeScript frontend for the Advanced Test Project.

## Features

- React 18 with hooks
- TypeScript for type safety
- Vite for fast development and builds
- Axios for API communication
- Responsive design

## Development

```bash
npm install
npm run dev
```

Frontend will be available at `http://localhost:3000`

## Build for Production

```bash
npm run build
```

Generated files will be in `dist/` directory.

## Project Structure

```
src/
├── main.tsx          # Entry point
├── App.tsx           # Main component
└── App.css           # Styles
```

## API Integration

The frontend communicates with the backend via:
- REST API (`/api/v1/users`, `/api/v1/tasks`)
- Base URL configured in Vite config (proxied to `http://localhost:8000`)

## Docker

```bash
# Build image
docker build -t advanced-test-frontend .

# Run container
docker run -p 3000:3000 advanced-test-frontend
```
