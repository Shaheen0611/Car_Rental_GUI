from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

car_customer_table = Table('car_customer', Base.metadata,
                               Column('car_id', Integer, ForeignKey('cars.id')),
                               Column('customer_id', Integer, ForeignKey('customers.id')))

class Cars(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    brand = Column(String)
    year = Column(Integer)
    seats = Column(Integer)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customers = relationship('Customers', back_populates='cars', secondary=car_customer_table)

class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    telephone = Column(Integer)
    cars = relationship('Cars', back_populates='customers', secondary=car_customer_table)


def main():
    # ENGINE DESCRIBES DATABASE AND CONNECTION URL
    engine = create_engine(f'sqlite:///cars.sqlite')
    # CREATE A SESSON MAKER (FACTORY PATTERN)
    Session = sessionmaker(bind=engine)
    # CREATING SESSION USING SESSIONMAKER
    session = Session()
    pass

if __name__ == '__main__':
    main()