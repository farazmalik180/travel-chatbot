class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'your_secret_key_here'
    DATABASE_URI = 'sqlite:///travel_chatbot.db'
    API_KEY = 'your_api_key_here'  # Replace with your actual API key if needed
    ALLOWED_HOSTS = ['*']  # Adjust as necessary for production use

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True