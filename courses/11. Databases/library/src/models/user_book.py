from sqlalchemy import Table, Column, Integer, ForeignKey
from src.db import BaseClass

# relation table for User-Book M-M relation

user_book = Table('user_book', BaseClass.metadata,
            Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
                  Column('book_id', Integer, ForeignKey('books.id'), primary_key=True)
                  )
