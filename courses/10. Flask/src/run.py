from config import Config
from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=Config, port=8080)
