# Math Game - Deployment Instructions

## Quick Deploy to PythonAnywhere

### Step 1: Upload Files
1. Go to [PythonAnywhere](https://www.pythonanywhere.com) and create an account
2. Go to the **Files** tab
3. Create a folder called `mathgame`
4. **Upload these two folders:**
   - Upload your local `backend/` folder to `/home/yourusername/mathgame/backend/`
   - Upload your local `frontend/dist/` folder to `/home/yourusername/mathgame/frontend/dist/`

### Step 2: Set Up Python Environment
1. Go to **Consoles** tab → Open Bash console
2. Run these commands:
   ```bash
   cd mathgame
   python3.9 -m venv venv
   source venv/bin/activate
   cd backend
   pip install -r requirements.txt
   ```

### Step 3: Create Web App
1. Go to **Web** tab
2. Click **Add a new web app**
3. Choose **Manual configuration** (not Flask)
4. Select **Python 3.9**

### Step 4: Configure WSGI File
1. In **Web** tab, click the WSGI configuration file link
2. Replace everything with:
   ```python
   import sys
   import os
   
   path = '/home/yourusername/mathgame/backend'
   if path not in sys.path:
       sys.path.append(path)
   
   from app import app as application
   ```
3. **Replace `yourusername` with your actual username**
4. Save the file

### Step 5: Configure Static Files
1. In **Web** tab, scroll to **Static files**
2. Add these mappings:
   - **URL**: `/static/` → **Directory**: `/home/yourusername/mathgame/frontend/dist/`
   - **URL**: `/api/images/` → **Directory**: `/home/yourusername/mathgame/backend/images/`

### Step 6: Reload and Test
1. Click **Reload** button in Web tab
2. Visit your app: `https://yourusername.pythonanywhere.com`

## What Files Are Ready

- ✅ `backend/app.py` - Flask app that serves frontend
- ✅ `backend/wsgi.py` - WSGI config for PythonAnywhere  
- ✅ `backend/requirements.txt` - All dependencies
- ✅ `frontend/dist/` - Built Vue.js app (HTML/CSS/JS)
- ✅ `backend/images/` - Game images

## Troubleshooting

**If it doesn't work:**
1. Check error logs in **Web** tab
2. Verify file paths in WSGI file
3. Make sure both folders uploaded correctly
4. Check static file mappings

**Common issues:**
- Wrong username in WSGI file
- Missing static file mappings
- Files not uploaded to correct locations

## File Structure on PythonAnywhere

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
            ├── index-1bfda9c7.css
            └── index-cde47dce.js
```

That's it! Your Math Game should be live at `https://yourusername.pythonanywhere.com` 