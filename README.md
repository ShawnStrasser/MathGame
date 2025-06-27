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

## Deploying to PythonAnywhere (from GitHub)

### 1. Push Your Project to GitHub
If you haven't already:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/mathgame.git
git push -u origin main
```

### 2. Clone on PythonAnywhere
- Open a **Bash console** on PythonAnywhere
- Run:
```bash
git clone https://github.com/yourusername/mathgame.git
cd mathgame
```

### 3. Set Up Python 3.12 Virtual Environment
```bash
python3.12 -m venv venv
source venv/bin/activate
cd backend
pip install -r requirements.txt
```

### 4. Configure Your Web App
- Go to the **Web** tab on PythonAnywhere
- Click **Add a new web app**
- Choose **Manual configuration** (not Flask)
- Select **Python 3.12**

### 5. Configure WSGI File
- In the **Web** tab, click the WSGI configuration file link
- Replace everything with:
```python
import sys
import os

path = '/home/yourusername/mathgame/backend'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```
- Replace `yourusername` with your PythonAnywhere username
- Save the file

### 6. Configure Static Files
- In the **Web** tab, scroll to **Static files**
- Add these mappings:
  - **URL**: `/static/` → **Directory**: `/home/yourusername/mathgame/frontend/dist/`
  - **URL**: `/api/images/` → **Directory**: `/home/yourusername/mathgame/backend/images/`

### 7. Reload and Test
- Click **Reload** in the Web tab
- Visit `https://yourusername.pythonanywhere.com` to test your app

---

**Troubleshooting:**
- Check error logs in the Web tab if something doesn't work
- Make sure your username and file paths are correct in the WSGI and static file settings
- Ensure you are using Python 3.12 everywhere

---

**File structure after cloning should look like:**
```
/home/yourusername/mathgame/
├── backend/
│   ├── app.py
│   ├── wsgi.py
│   ├── requirements.txt
│   └── images/
│       ├── 1.png
│       ├── 2.png
│       ├── 3.png
│       └── 4.png
└── frontend/
    └── dist/
        ├── index.html
        └── assets/
            ├── index-xxxx.css
            └── index-xxxx.js
```

## Setup Instructions

### Backend Setup
```