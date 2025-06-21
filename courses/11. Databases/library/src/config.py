class Config:
    APP_NAME = "The Library REST API"
    VERSION = "1.0.1"
    DATABASE = "books.db"
    DEBUG = True
    PORT = 5000
    JSON_PATH = "./db/books.json"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
