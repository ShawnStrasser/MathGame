# Math Game - Pixel Reveal

A fun math game for kids where solving math problems reveals parts of a pixelated image!

## Features
- Addition, subtraction, and multiplication problems
- Pixelated images that reveal sections as problems are solved
- Progressive difficulty levels
- Multiple sample images included

## Project Structure
```
MathGame/
├── backend/          # Flask API server
├── frontend/         # Vue.js frontend with Vite
└── README.md         # This file
```

## Setup Instructions

### Backend Setup
```bash
cd backend
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python app.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## Development Commands

### Start Backend Server
```bash
cd backend
python app.py
```
Server will run on http://localhost:5000

### Start Frontend Development Server
```bash
cd frontend
npm run dev
```
Frontend will run on http://localhost:5173

## How to Play
1. Choose a difficulty level
2. Solve math problems to reveal parts of the hidden image
3. Complete the image to win! 