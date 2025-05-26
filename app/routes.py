from flask import Blueprint, request, jsonify, render_template
from .chatbot import get_chatbot_response

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@bp.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400
    
    response = get_chatbot_response(user_input)
    return jsonify({'response': response})

@bp.route('/places', methods=['GET'])
def get_places():
    places = [
        {'name': 'Karachi', 'description': 'A bustling metropolis and the largest city in Pakistan.'},
        {'name': 'Lahore', 'description': 'Known for its rich history and vibrant culture.'},
        {'name': 'Islamabad', 'description': 'The capital city, known for its modern architecture and greenery.'},
        {'name': 'Murree', 'description': 'A popular hill station with stunning views.'},
        {'name': 'Hunza Valley', 'description': 'Famous for its breathtaking landscapes and hospitality.'},
        {'name': 'Skardu', 'description': 'Gateway to some of the world’s highest peaks and beautiful lakes.'},
        {'name': 'Fairy Meadows', 'description': 'A lush green plateau near Nanga Parbat, ideal for trekking.'},
        {'name': 'Swat Valley', 'description': 'Known as the Switzerland of the East for its scenic beauty.'},
        {'name': 'Multan', 'description': 'The city of saints, famous for its shrines and bazaars.'},
        {'name': 'Gwadar', 'description': 'A port city with beautiful beaches on the Arabian Sea.'}
    ]
    return jsonify({'places': places})