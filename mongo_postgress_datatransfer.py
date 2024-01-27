from mongoengine import connect
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    MetaData,
)
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from mongo_models import Author as mAuthor, Quote as mQuote


# Connect to MongoDB
from mongoengine import connect

url = "mongodb+srv://jasinsky:BmCJg7doGgfFEACx@mj.l7d1sxj.mongodb.net/?retryWrites=true&w=majority"
db_name = "hw8"

try:
    connect(db=db_name, host=url)
except Exception as e:
    print(f"the error {e} occured with MongoDB connection")

# Connect to PostgreSQL
db_url = f"postgresql+psycopg2://postgres:Dinamo12@172.17.0.2:5432/school_hw7.db"

engine = create_engine(db_url, echo=False)
DBsession = sessionmaker(bind=engine)
session = DBsession()
metadata = MetaData()
Base = declarative_base()


# Define the PostgreSQL models
class Author(Base):
    __tablename__ = "polls_author"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(100), nullable=False)
    born_date = Column(String(255), nullable=True)
    born_location = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)


class Quote(Base):
    __tablename__ = "polls_quote"
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey("polls_author.id"), nullable=False)
    tags = Column(Text)
    quote = Column(Text, nullable=False)

    # Add a foreign key constraint between the quote table and the author table
    author = relationship("Author", backref="quotes")


# Create the tables in the PostgreSQL
Base.metadata.create_all(engine)

# Retrieve all authors from MongoDB
authors = mAuthor.objects.all()

# Create instances of the PostgreSQL Author model for each MongoDB author
postgresql_authors = set()
for mongo_author in authors:
    postgresql_author = Author(
        fullname=mongo_author.fullname,
        born_date=mongo_author.born_date,
        born_location=mongo_author.born_location,
        description=mongo_author.description,
    )

    postgresql_authors.add(postgresql_author)

# Save the PostgreSQL authors to the database
session.add_all(postgresql_authors)
session.commit()

# Retrieve all quotes from MongoDB
quotes = mQuote.objects.all()

# Create instances of the PostgreSQL Quote model for each MongoDB quote
postgresql_quotes = set()
for mongo_quote in quotes:
    author_id = None

    # Find the corresponding PostgreSQL author
    for postgresql_author in session.query(Author).filter(
        Author.fullname == mongo_quote.author.fullname
    ):
        author_id = postgresql_author.id
        break

    postgresql_quote = Quote(
        author_id=author_id,
        tags=mongo_quote.tags,
        quote=mongo_quote.quote,
    )

    postgresql_quotes.add(postgresql_quote)

# Save the PostgreSQL quotes to the database
session.add_all(postgresql_quotes)
session.commit()

print("data successfully transfered from MongoDB to PostgreSQL")
