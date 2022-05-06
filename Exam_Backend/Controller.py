from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from classData import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()
app = Flask(__name__)
api = Api(app)
engine = create_engine(f'sqlite:///cars.sqlite', connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
session = Session()
session_car_list = Session()
session_car_list_2 = Session()
session_car_list_3 = Session()
session_customer_list = Session()
session_customer_list_2 = Session()


class Cars_list(Resource): #API CAR
    def get(self): #GET ALL CARS ---------------------------------------------------------------------------------------
        lists_car = []
        list_car = session_car_list.query(Cars).all()
        for cars in list_car:
            list_car_json = {"id": f"{cars.id}",
                             "brand": f"{cars.brand}",
                             "year": f"{cars.year}",
                             "seats": f"{cars.seats}",
                             "customer_id": f"{cars.customer_id}"
                             }
            lists_car.append(list_car_json)
        session_car_list.close()
        return lists_car

    def post(self): #POST CARS -----------------------------------------------------------------------------------------
        add_car = request.get_json(Cars)
        list_new_add_car = Cars(brand=add_car['brand'],
                                year=int(add_car['year']),
                                seats=int(add_car['seats']))

        print(f'{add_car}')
        session_car_list.add(list_new_add_car)
        session_car_list.commit()
        session_car_list.close()
        return add_car

def list_for_id_car(session): #LIST FOR PUT AND DELETE CARS ----------------------------------------------------------------
    lists_car_2 = []
    list_car_2 = session.query(Cars).all()
    for cars_2 in list_car_2:
        list_car_json_2 = {"id": f"{cars_2.id}",
                        "brand": f"{cars_2.brand}",
                        "year": f"{cars_2.year}",
                        "seats": f"{cars_2.seats}",
                        "customer_id": f"{cars_2.customer_id}"
                        }

        lists_car_2.append(list_car_json_2)
    session_car_list.commit()
    session_car_list.close()
    return lists_car_2

class Car_list_change(Resource): #API CAR <ID>
    def get(self, id): #GET CAR ID -------------------------------------------------------------------------------------
        get_id = list_for_id_car(session_car_list)
        id_find = id
        for a in get_id:
            if int(a["id"]) == id_find:
                getting_id = {"id": a["id"], "brand": a["brand"], "year": a["year"],
                              "seats": a["seats"], "customer_id": a["customer_id"]}
        return getting_id

    def put(self, id): #PUT CAR-----------------------------------------------------------------------------------------
        car_list_save = session_car_list.query(Cars).get(id)
        car_list_edit = request.get_json(Cars)
        car_list_save.brand = car_list_edit['brand']
        car_list_save.year = car_list_edit['year']
        car_list_save.seats = car_list_edit['seats']
        session_car_list.commit()
        session_car_list.close()
        return car_list_edit

    def delete(self, id): #DELETE CAR-----------------------------------------------------------------------------------
        id_ = id
        del_id = session_car_list.query(Cars).get(id_)
        session_car_list.delete(del_id)
        session_car_list.commit()
        session_car_list.close()
        return id


#-----------------------------------------------------------------------------------------------------------------------


class Customers_list(Resource): #API CUSTOMER
    def get(self): #GET ALL CUSTOMERS ----------------------------------------------------------------------------------
        lists_customer = []
        list_customer = session_customer_list.query(Customers).all()
        for customers in list_customer:
            list_customer_json = {"id": f"{customers.id}",
                             "name": f"{customers.name}",
                             "email": f"{customers.email}",
                            "telephone": f"{customers.telephone}"}
            lists_customer.append(list_customer_json)
        session_customer_list.close()
        return lists_customer

    def post(self): #POST CUSTOMERS ------------------------------------------------------------------------------------
        add_customer = request.get_json(Customers)
        list_new_add_customer = Customers(name=add_customer['name'],
                                        email=add_customer['email'],
                                        telephone=int(add_customer['telephone']))

        print(f'{add_customer}')
        session_customer_list.add(list_new_add_customer)
        session_customer_list.commit()
        session_customer_list.close()
        return add_customer

def list_for_id_customer(session): #LIST FOR PUT AND DELETE CUSTOMER ---------------------------------------------------
    lists_customer_2 = []
    list_customer_2 = session.query(Customers).all()
    for customer_2 in list_customer_2:
        list_customer_json_2 = {"id": f"{customer_2.id}",
                        "name": f"{customer_2.name}",
                        "email": f"{customer_2.email}",
                        "telephone": f"{customer_2.telephone}"
                        }

        lists_customer_2.append(list_customer_json_2)
    session_customer_list.commit()
    session_customer_list.close()
    return lists_customer_2

class Customer_list_change(Resource): #API CUSTOMER <ID>
    def get(self, id): #GET CUSTOMER ID --------------------------------------------------------------------------------
        get_id = list_for_id_customer(session_customer_list)
        id_find = id
        for a in get_id:
            if int(a["id"]) == id_find:
                getting_id = {"id": a["id"], "name": a["name"], "email": a["email"],
                              "telephone": a["telephone"]}
        return getting_id

    def put(self, id): #PUT CUSTOMER -----------------------------------------------------------------------------------
        customer_list_save = session_customer_list.query(Customers).get(id)
        customer_list_edit = request.get_json(Customers)
        customer_list_save.name = customer_list_edit['name']
        customer_list_save.email = customer_list_edit['email']
        customer_list_save.telephone = customer_list_edit['telephone']
        session_customer_list.commit()
        session_customer_list.close()
        return customer_list_edit

    def delete(self, id): #DELETE CUSTOMER------------------------------------------------------------------------------
        id_ = id
        del_id = session_customer_list.query(Customers).get(id_)
        session_customer_list.delete(del_id)
        session_customer_list.commit()
        session_customer_list.close()
        return id


#-----------------------------------------------------------------------------------------------------------------------


class Cars_to_Customer(Resource):
    def put(self, id): #PUT CAR TO CUSTOMER-----------------------------------------------------------------------------
        car_list_save = session_car_list.query(Cars).get(id)
        car_list_edit = request.get_json(Cars)
        if session_car_list.query(Customers).get(car_list_edit['customer_id']):
            car_list_save.customer_id = car_list_edit['customer_id']
            session_car_list.commit()

            return car_list_edit
        return "Customer not Found"

    def delete(self, id): #DELETE CAR TO CUSTOMER-----------------------------------------------------------------------
        customer_id = id
        del_id = session_customer_list.query(Cars).get(customer_id)
        car_list_del = {"customer_id": None}
        del_id.customer_id = car_list_del['customer_id']
        session_customer_list.commit()
        session_customer_list.close()
        return id

#-----------------------------------------------------------------------------------------------------------------------


def main():

    # ENGINE DESCRIBES DATABASE AND CONNECTION URL
    engine = create_engine(f'sqlite:///cars.sqlite')
    # CREATE A SESSON MAKER (FACTORY PATTERN)
    Session = sessionmaker(bind=engine)
    # CREATING SESSION USING SESSIONMAKER


    api.add_resource(Cars_list, '/cars/')
    api.add_resource(Car_list_change, '/cars/<int:id>/', methods=["GET", "POST", "PUT", "DELETE"])
    api.add_resource(Customers_list, '/customers/')
    api.add_resource(Customer_list_change, '/customers/<int:id>/')
    api.add_resource(Cars_to_Customer, '/cars/<int:id>/customers')

    app.run(debug=True)

if __name__ == '__main__':
    main()


