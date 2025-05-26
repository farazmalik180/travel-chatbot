# Travel Chatbot

This project is a travel chatbot designed to serve as a guide to tourist places in Pakistan. It is built using Flask and provides users with information about various tourist destinations.

## Features

- Interactive chatbot interface
- Information retrieval about tourist places in Pakistan
- User-friendly responses and suggestions

## Project Structure

```
travel-chatbot
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── chatbot.py
│   └── utils.py
├── requirements.txt
├── config.py
├── wsgi.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd travel-chatbot
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Set up your configuration in `config.py`.
2. Run the application:
   ```
   python wsgi.py
   ```
3. Access the chatbot through your web browser at `http://127.0.0.1:5000`.

## Deployment

This application can be deployed on AWS Cloud using services like Elastic Beanstalk or EC2. Ensure that the necessary environment variables and configurations are set up in the AWS environment.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.