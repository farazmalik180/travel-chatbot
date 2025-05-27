# Travel Chatbot

A Flask-based chatbot that serves as a guide to tourist places in Pakistan.

## Features

- Interactive chat interface
- Information about tourist places in Pakistan
- Real-time responses
- Mobile-friendly design

## Project Structure

```
travel-chatbot/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── chatbot.py
│   ├── utils.py
│   └── templates/
│       └── index.html
├── requirements.txt
├── requirements-lambda.txt
├── wsgi.py
├── Procfile
├── zappa_settings.json
└── .ebextensions/
    └── python.config
```

## Local Development

1. Clone the repository:
```bash
git clone <repository-url>
cd travel-chatbot
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python wsgi.py
```

The application will be available at `http://127.0.0.1:5000`

## Deployment Options

### Option 1: AWS Elastic Beanstalk

1. Install the EB CLI:
```bash
pip install awsebcli
```

2. Initialize EB project:
```bash
eb init
```

3. Create and deploy:
```bash
eb create
```

4. For future deployments:
```bash
eb deploy
```

### Option 2: AWS Lambda + API Gateway

1. Install Lambda-specific dependencies:
```bash
pip install -r requirements-lambda.txt
```

2. Deploy using AWS Console:

   a. Create a Lambda Function:
   - Go to AWS Console → Lambda
   - Create new function (Python 3.9)
   - Upload code as ZIP file
   - Set memory to 512MB
   - Set timeout to 30 seconds

   b. Create API Gateway:
   - Create new REST API
   - Create resource and method
   - Enable CORS
   - Deploy to a stage

   c. Configure Lambda permissions:
   - Add API Gateway invoke permissions
   - Add CloudWatch Logs permissions

3. Test the deployment:
```bash
curl https://your-api-id.execute-api.region.amazonaws.com/stage/
```

## Environment Variables

- `FLASK_ENV`: Set to 'production' for deployment
- Add any other environment-specific variables in the respective deployment configurations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository.