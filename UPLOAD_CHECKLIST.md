# Upload Checklist for PythonAnywhere

## What to Upload

### ✅ Backend Folder (Required)
Upload the **entire** `backend/` folder to `/home/yourusername/mathgame/backend/`

**Contents:**
- `app.py` - Main Flask application
- `wsgi.py` - WSGI configuration for PythonAnywhere
- `requirements.txt` - Python dependencies
- `images/` folder - Game images (1.png, 2.png, 3.png, 4.png)

### ✅ Frontend Dist Folder (Required)
Upload the **entire** `frontend/dist/` folder to `/home/yourusername/mathgame/frontend/dist/`

**Contents:**
- `index.html` - Main HTML file
- `assets/` folder - CSS and JavaScript files

## Upload Steps

1. **Go to PythonAnywhere Files tab**
2. **Create folder**: `/home/yourusername/mathgame/`
3. **Upload backend folder**:
   - Select your local `backend/` folder
   - Upload to `/home/yourusername/mathgame/backend/`
4. **Upload frontend dist folder**:
   - Select your local `frontend/dist/` folder
   - Upload to `/home/yourusername/mathgame/frontend/dist/`

## What NOT to Upload

- ❌ `frontend/src/` folder (source code, not needed)
- ❌ `frontend/node_modules/` folder (not needed)
- ❌ `frontend/package.json` (not needed)
- ❌ Any `.git/` folders
- ❌ Development files

## Verify Upload

After uploading, your PythonAnywhere file structure should look like this:
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

## Next Steps

After uploading, continue with:
1. Setting up Python environment (Step 3 in main guide)
2. Configuring web app (Step 4 in main guide)
3. Setting up WSGI file (Step 5 in main guide)
4. Configuring static files (Step 6 in main guide) 