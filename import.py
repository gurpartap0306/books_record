import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

engine =create_engine(os.getenv("DATABASE_URL"))
db=scoped_session(sessionmaker(bind=engine))

def main():
    db.execute("CREATE TABLE books(isbn varchar(255) primary key,title varchar(255),author varchar(255), year integer)")
    db.commit()

    f=open("books.csv")
    reader=csv.reader(f)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)", {"isbn": isbn, "title": title, "author": author, "year": year})
        print(f"data has been added")
    db.commit()

if __name__=="__main__":
    main()
