# Math Game Images

This folder contains the pixel art images used in the math game.

## Current Images

The game currently uses text-based pixel art defined in the backend code:

1. **Happy Face (Easy)** - A simple smiley face
2. **Star (Medium)** - A five-pointed star  
3. **Heart (Hard)** - A heart shape

## How It Works

- Each image is defined as an array of strings in `app.py`
- Each string represents a row of pixels
- `█` represents a filled pixel
- Spaces represent empty pixels
- When a math problem is solved correctly, a random filled pixel is revealed

## Future Enhancements

- Add actual image files (PNG, JPG) for more complex images
- Create different themes (animals, objects, etc.)
- Add color variations
- Implement different reveal patterns (sequential, random, etc.) 