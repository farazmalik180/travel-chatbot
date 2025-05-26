def fetch_tourist_places():
    # This function would ideally fetch data from a database or an API
    # For now, we will return a static list of tourist places in Pakistan
    return [
        {"name": "Hunza Valley", "description": "A mountainous valley located in the Gilgit-Baltistan region."},
        {"name": "Lahore Fort", "description": "A UNESCO World Heritage Site and a symbol of Lahore's rich history."},
        {"name": "Karimabad", "description": "The capital of Hunza, known for its stunning views of the Karakoram mountain range."},
        {"name": "Mohenjo-Daro", "description": "An archaeological site of the ancient Indus Valley Civilization."},
        {"name": "Fairy Meadows", "description": "A beautiful plateau near Nanga Parbat, ideal for trekking and camping."},
    ]

def format_response(data):
    # This function formats the response for the chatbot
    if not data:
        return "Sorry, I couldn't find any information."
    
    response = "Here are some tourist places in Pakistan:\n"
    for place in data:
        response += f"- {place['name']}: {place['description']}\n"
    
    return response.strip()