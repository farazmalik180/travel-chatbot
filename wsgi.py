from app import create_app

app = create_app()

# This is needed for Lambda
def handler(event, context):
    return app(event, context)

if __name__ == "__main__":
    app.run()