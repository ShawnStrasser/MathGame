from flask import Flask, jsonify, request, send_from_directory, send_file
from flask_cors import CORS
import random
import os

# Get the absolute path to the project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIST = os.path.join(PROJECT_ROOT, 'frontend', 'dist')

app = Flask(__name__)
CORS(app)

IMAGE_FOLDER = os.path.join(os.path.dirname(__file__), 'images')

DIFFICULTY_GRID = {
    'easy': 2,
    'medium': 3,
    'hard': 4
}

def get_random_image_filename():
    files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return random.choice(files) if files else None

@app.route('/api/game/new', methods=['POST'])
def new_game():
    data = request.get_json()
    difficulty = data.get('difficulty', 'easy')
    grid_size = DIFFICULTY_GRID.get(difficulty, 2)
    image_filename = get_random_image_filename()
    if not image_filename:
        return jsonify({'error': 'No images found'}), 500
    image_url = f'/api/images/{image_filename}'
    total_sections = grid_size * grid_size
    return jsonify({
        'game_id': random.randint(1000, 9999),
        'difficulty': difficulty,
        'image_url': image_url,
        'grid_size': grid_size,
        'total_sections': total_sections,
        'revealed_sections': [],
        'current_problem': generate_math_problem(difficulty)
    })

def generate_math_problem(difficulty):
    if difficulty == 'easy':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-'])
        if operation == '-':
            if num1 < num2:
                num1, num2 = num2, num1
            answer = num1 - num2
        else:
            answer = num1 + num2
    elif difficulty == 'medium':
        operation = random.choice(['+', '-', '*'])
        if operation == '*':
            num1 = random.randint(2, 6)
            num2 = random.randint(2, 6)
            answer = num1 * num2
        else:
            num1 = random.randint(5, 20)
            num2 = random.randint(5, 20)
            if operation == '-':
                if num1 < num2:
                    num1, num2 = num2, num1
                answer = num1 - num2
            else:
                answer = num1 + num2
    else:
        operation = random.choice(['+', '-', '*'])
        if operation == '*':
            num1 = random.randint(3, 12)
            num2 = random.randint(3, 12)
            answer = num1 * num2
        else:
            num1 = random.randint(10, 50)
            num2 = random.randint(10, 50)
            if operation == '-':
                if num1 < num2:
                    num1, num2 = num2, num1
                answer = num1 - num2
            else:
                answer = num1 + num2
    problem = f"{num1} {operation} {num2}"
    return {
        'problem': problem,
        'answer': answer,
        'operation': operation
    }

@app.route('/api/game/problem', methods=['POST'])
def get_new_problem():
    data = request.get_json()
    difficulty = data.get('difficulty', 'easy')
    return jsonify(generate_math_problem(difficulty))

@app.route('/api/game/check-answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    user_answer = data.get('answer')
    correct_answer = data.get('correct_answer')
    try:
        user_answer = int(user_answer)
        is_correct = user_answer == correct_answer
        return jsonify({
            'correct': is_correct,
            'user_answer': user_answer,
            'correct_answer': correct_answer
        })
    except (ValueError, TypeError):
        return jsonify({
            'correct': False,
            'error': 'Invalid answer format'
        }), 400

@app.route('/api/images/<filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

@app.route('/')
def serve_frontend():
    return send_file(os.path.join(FRONTEND_DIST, 'index.html'))

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(FRONTEND_DIST, path)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000) 