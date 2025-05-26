from flask import jsonify

class Chatbot:
    def __init__(self):
        self.tourist_places = {
            "Karachi": "A bustling metropolis known for its beaches and vibrant culture.",
            "Lahore": "Famous for its rich history, food, and the Badshahi Mosque.",
            "Islamabad": "The capital city, known for its modern architecture and greenery.",
            "Murree": "A popular hill station with stunning views and pleasant weather.",
            "Hunza": "Known for its breathtaking landscapes and hospitable people."
        }

    def get_response(self, user_input):
        user_input_lower = user_input.lower().strip()
        if "places" in user_input_lower:
            return self.list_places()
        elif "recommend" in user_input_lower:
            return self.recommend_place()
        # Check if user mentioned a place
        for place in self.tourist_places:
            if place.lower() in user_input_lower:
                return f"{place}: {self.tourist_places[place]}"
        return "I'm sorry, I didn't understand that. You can ask me about tourist places in Pakistan."

    def list_places(self):
        places = ", ".join(self.tourist_places.keys())
        return f"Here are some popular tourist places in Pakistan: {places}."

    def recommend_place(self):
        return "I recommend visiting Lahore for its historical significance and delicious food!"


chatbot_instance = Chatbot()

def get_chatbot_response(user_input):
    return chatbot_instance.get_response(user_input)