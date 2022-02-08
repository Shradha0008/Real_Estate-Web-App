import csv
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from unwrap import db
from unwrap.models import Products


def main():
    f = open("products.csv")
    reader = csv.reader(f)
    for name, price in reader:
    	product = Products(name=name,price=price)
    	db.session.add(product)
    	print(f"Added product {name}, {price}")
    db.session.commit()

if __name__ == "__main__":
    main()