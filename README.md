# Algorithmic Trading Dashboard

This project is a minimal scaffolding for a dashboard that compiles, backtests and deploys QuantConnect algorithms.

## Requirements
- Python 3.11+
- Node.js 20+
- Docker (for running the stack)

## Development

### Backend
```
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```
cd frontend
npm install
npm run dev
```

### Docker Compose
```
cd docker
docker-compose up --build
```

## CI
GitHub Actions runs lint and build checks on push.
