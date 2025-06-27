# PythonAnywhere Deployment Guide

## Prerequisites
- A PythonAnywhere account (free or paid)
- Your Math Game project ready for deployment

## Step 1: Prepare Your Project

1. **Build the frontend** (if not already done):
   ```bash
   cd frontend
   npm run build
   cd ..
   ```

2. **Verify the following files are ready**:
   - `backend/app.py` (updated to serve static files)
   - `backend/wsgi.py` (WSGI file for PythonAnywhere)
   - `backend/requirements.txt` (updated dependencies)
   - `frontend/dist/` (built static files)
   - `backend/images/` (game images)

## Step 2: Upload Files to PythonAnywhere

### Option A: Using PythonAnywhere File Browser
1. Log into your PythonAnywhere account
2. Go to the **Files** tab
3. Create a new directory for your project (e.g., `mathgame`)
4. **Upload the backend folder**:
   - Upload the entire `backend/` folder to `/home/yourusername/mathgame/backend/`
   - This includes: `app.py`, `wsgi.py`, `requirements.txt`, and `images/` folder
5. **Upload the frontend dist folder**:
   - Upload the entire `frontend/dist/` folder to `/home/yourusername/mathgame/frontend/dist/`
   - This includes: `index.html` and `assets/` folder

**Final structure on PythonAnywhere should be:**
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

### Option B: Using Git (Recommended)
1. Push your project to GitHub/GitLab
2. In PythonAnywhere, go to the **Consoles** tab
3. Open a Bash console and run:
   ```bash
   git clone https://github.com/yourusername/mathgame.git
   cd mathgame
   ```

## Step 3: Set Up Python Environment

1. Go to the **Consoles** tab in PythonAnywhere
2. Open a Bash console
3. Navigate to your project directory:
   ```bash
   cd mathgame
   ```

4. Create a virtual environment:
   ```bash
   python3.9 -m venv venv
   source venv/bin/activate
   ```

5. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

## Step 4: Configure Web App

1. Go to the **Web** tab in PythonAnywhere
2. Click **Add a new web app**
3. Choose **Manual configuration** (not Flask)
4. Select **Python 3.9** (or latest available)
5. Set your domain name (e.g., `yourusername.pythonanywhere.com`)

## Step 5: Configure WSGI File

1. In the **Web** tab, click on the WSGI configuration file link
2. Replace the entire content with:
   ```python
   import sys
   import os
   
   # Add your project directory to the Python path
   path = '/home/yourusername/mathgame/backend'
   if path not in sys.path:
       sys.path.append(path)
   
   from app import app as application
   ```

3. **Important**: Replace `yourusername` with your actual PythonAnywhere username
4. Save the file

## Step 6: Configure Static Files

1. In the **Web** tab, scroll down to **Static files**
2. Add the following static file mappings:
   - **URL**: `/static/`
   - **Directory**: `/home/yourusername/mathgame/frontend/dist/`
   
3. Add another mapping for images:
   - **URL**: `/api/images/`
   - **Directory**: `/home/yourusername/mathgame/backend/images/`

## Step 7: Reload Web App

1. In the **Web** tab, click the **Reload** button
2. Wait for the reload to complete

## Step 8: Test Your Application

1. Visit your web app URL: `https://yourusername.pythonanywhere.com`
2. Test the game functionality
3. Check that images load correctly
4. Verify that the math problems work

## Troubleshooting

### Common Issues:

1. **Import Errors**: Make sure your project path is correct in the WSGI file
2. **Static Files Not Loading**: Verify static file mappings in the Web tab
3. **Images Not Loading**: Check that the images folder is uploaded and accessible
4. **500 Errors**: Check the error logs in the Web tab

### Error Logs:
- Go to the **Web** tab
- Click on **Error log** to see detailed error messages
- Check both the error log and server log for debugging information

### File Permissions:
- Make sure all files have proper read permissions
- Images should be accessible by the web server

## File Structure on PythonAnywhere

Your final structure should look like this:
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

## Security Notes

1. **Debug Mode**: Make sure debug mode is disabled in production
2. **CORS**: The app includes CORS headers for development; consider removing if not needed
3. **Environment Variables**: Use environment variables for any sensitive configuration

## Performance Tips

1. **Static Files**: PythonAnywhere serves static files efficiently
2. **Caching**: Consider adding cache headers for static assets
3. **Compression**: Enable gzip compression in your web app settings

## Support

If you encounter issues:
1. Check the PythonAnywhere help documentation
2. Review the error logs in the Web tab
3. Verify all file paths and permissions
4. Ensure all dependencies are installed correctly 