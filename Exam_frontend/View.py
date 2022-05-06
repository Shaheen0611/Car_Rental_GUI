from tkinter import *
import requests
from tkinter import ttk
import json
from tkinter.filedialog import asksaveasfile


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.welcome_page = Label(self, text='Welcome to Car rental', width=20, height=3)
        self.welcome_page.pack(side='top', padx=1, pady=1)
        self.welcome_page.pack()
#fix
        self.btn_quit = Button(self, text='Quit', fg='blue', width=15, height=3, command=self.master.destroy)
        self.btn_quit.pack(side='bottom', padx=1, pady=1)

        self.car_btn = Button(self, text='Car', width=15, height=3, command=self.car_view)
        self.car_btn.pack(side='left', padx=1, pady=1)
        self.car_btn.pack()

        self.customer_btn = Button(self, text='Cars for Customer', width=15, height=3,
                                   command=self.cars_to_customer_view)
        self.customer_btn.pack(side='right', padx=1, pady=1)
        self.customer_btn.pack()

        self.customer_btn = Button(self, text='Customer', width=15, height=3, command=self.customer_view)
        self.customer_btn.pack(side='right', padx=1, pady=1)
        self.customer_btn.pack()


#-----------------------------------------------------------------------------------------------------------------------


    def car_view(self):
        root_car = Tk()
        root_car.geometry('465x250+430+160')

        root_car.car_home_btn = Button(root_car, text='Home', fg='blue', width=15, height=3,
                                       command=root_car.destroy)
        root_car.car_home_btn.pack(side='bottom', padx=1, pady=1)


        root_car.car_read_btn = Button(root_car, text='Read car', width=15, height=3, command=self.car_read_view)
        root_car.car_read_btn.pack(side='left', padx=1, pady=1)
        root_car.car_read_btn.pack()

        root_car.car_add_btn = Button(root_car, text='Add car', width=15, height=3, command=self.car_add_view)
        root_car.car_add_btn.pack(side='left', padx=1, pady=1)
        root_car.car_add_btn.pack()

        root_car.car_edit_btn = Button(root_car, text='Edit car', width=15, height=3, command=self.car_edit_view)
        root_car.car_edit_btn.pack(side='left', padx=1, pady=1)
        root_car.car_edit_btn.pack()

        root_car.car_delete_btn = Button(root_car, text='Delete car', width=15, height=3, command=self.car_delete_view)
        root_car.car_delete_btn.pack(side='left', padx=1, pady=1)
        root_car.car_delete_btn.pack()


    def car_read_view(self):
        root_car_read = Tk()
        root_car_read.geometry('465x250+430+160')

        root_car_read.car_home_btn = Button(root_car_read, text='Back', fg='blue', width=15, height=2,
                                       command=root_car_read.destroy)
        root_car_read.car_home_btn.pack(side='bottom', padx=1, pady=1)

        root_car_read.car_home_label = Label(root_car_read, text='Car Details')
        root_car_read.car_home_label.pack(side='top')

        read = requests.get('http://localhost:5000/cars/')
        car = read.json()
        lists=[]
        for cars in car:
            list = (f"id: {cars['id']}, brand: {cars['brand']}, year: {cars['year']}, seats: {cars['seats']}, "
                  f"customer_id: {cars['customer_id']}\n")
            lists.append(list)

        Lb1 = Listbox(root_car_read, width=70, height=25)
        n = 0
        for x in lists:
            Lb1.insert(n, lists[int(n)])
            n +=1
        Lb1.pack()

#-----------------------------------------------------------------------------------------------------------------------


    def car_add_view(self):
        root_car_add = Tk()
        root_car_add.geometry('465x250+430+160')

        root_car_add.car_home_btn = Button(root_car_add, text='Back', fg='blue', width=15, height=3,
                                       command=root_car_add.destroy)
        root_car_add.car_home_btn.pack(side='bottom', padx=1, pady=1)

        root_car_add.title_label = Label(root_car_add,text='Add Cars')
        root_car_add.title_label.pack(side='top')

        root_car_add.label_brand = Label(root_car_add, text='Brand:')
        root_car_add.label_brand.place(x=133, y=45)
        self.enter_brand = Entry(root_car_add)
        self.enter_brand.place(x=175, y=47)

        root_car_add.label_year = Label(root_car_add, text='Year:')
        root_car_add.label_year.place(x=140, y=65)
        self.enter_year = Entry(root_car_add)
        self.enter_year.place(x=175, y=67)

        root_car_add.label_seats = Label(root_car_add, text='Seats:')
        root_car_add.label_seats.place(x=137, y=85)
        self.enter_seats = Entry(root_car_add)
        self.enter_seats.place(x=175, y=87)

        root_car_add.btn_ok = Button(root_car_add, text='Add Car', fg='blue', command=self.add_car_get)
        root_car_add.btn_ok.place(x=320, y=67)

    def add_car_get(self):
        get_brand= self.enter_brand.get()
        get_year = self.enter_year.get()
        get_seats = self.enter_seats.get()

        data = {'brand': get_brand,
                'year': int(get_year),
                'seats': int(get_seats),
                }

        result = requests.post('http://localhost:5000/cars/',json=data)

        self.enter_brand.delete(0, END)
        self.enter_year.delete(0, END)
        self.enter_seats.delete(0, END)


#-----------------------------------------------------------------------------------------------------------------------

    def car_edit_view(self):
        root_car_edit = Tk()
        root_car_edit.geometry('465x250+430+160')

        root_car_edit.car_home_btn = Button(root_car_edit, text='Back', fg='blue', width=15, height=2,
                                       command=root_car_edit.destroy)
        root_car_edit.car_home_btn.pack(side='bottom', padx=1, pady=1)

        root_car_edit.title_label = Label(root_car_edit, text='Edit Cars')
        root_car_edit.title_label.pack(side='top')


        root_car_edit.dropdown_id = Label(root_car_edit, text='Find ID:')
        root_car_edit.dropdown_id.place(x=128, y=45)

        self.dropdown = StringVar()
        self.id_choosen = ttk.Combobox(root_car_edit, width=27, textvariable=self.dropdown)



        read = requests.get(f"http://localhost:5000/cars/")
        car = read.json()
        lists = []
        self.id_choosen['values'] = ('None',)
        for cars in car:
            lists.append(cars['id'])
        for stuff in lists:
            self.id_choosen['values'] += (stuff,)

        #dropdown.set(lists)
        self.id_choosen.place(x=175, y=45)
        self.id_choosen.current()

        root_car_edit.label_brand = Label(root_car_edit, text='Brand:')
        root_car_edit.label_brand.place(x=133, y=95)
        self.enter_brand = Entry(root_car_edit)
        self.enter_brand.place(x=175, y=97)

        root_car_edit.label_year = Label(root_car_edit, text='Year:')
        root_car_edit.label_year.place(x=140, y=115)
        self.enter_year = Entry(root_car_edit)
        self.enter_year.place(x=175, y=117)

        root_car_edit.label_seats = Label(root_car_edit, text='Seats:')
        root_car_edit.label_seats.place(x=137, y=135)
        self.enter_seats = Entry(root_car_edit)
        self.enter_seats.place(x=175, y=137)

        root_car_edit.btn_ok = Button(root_car_edit, text='Update Car', fg='blue', command=self.edit_car_get)
        root_car_edit.btn_ok.place(x=320, y=115)


    def edit_car_get(self):
        get_brand= self.enter_brand.get()
        get_year = self.enter_year.get()
        get_seats = self.enter_seats.get()

        ca_id = self.id_choosen.get()

        data = {'brand': f"{get_brand}",
                'year': int(get_year),
                'seats': int(get_seats),
                }

        result = requests.put(f'http://localhost:5000/cars/{ca_id}/', json=data)

        self.enter_brand.delete(0, END)
        self.enter_year.delete(0, END)
        self.enter_seats.delete(0, END)



    def car_delete_view(self):
        root_car_delete = Tk()
        root_car_delete.geometry('465x250+430+160')

        root_car_delete.car_home_btn = Button(root_car_delete, text='Back', fg='blue', width=15, height=3,
                                       command=root_car_delete.destroy)
        root_car_delete.car_home_btn.pack(side='bottom', padx=1, pady=1)

        root_car_delete.title_label = Label(root_car_delete, text='Delete Cars')
        root_car_delete.title_label.pack(side='top')


        root_car_delete.dropdown_id = Label(root_car_delete, text='Find ID:')
        root_car_delete.dropdown_id.place(x=128, y=45)

        self.dropdown = StringVar()
        self.id_choosen = ttk.Combobox(root_car_delete, width=27, textvariable=self.dropdown)


        read = requests.get(f"http://localhost:5000/cars/")
        car = read.json()
        lists = []
        self.id_choosen['values'] = ('None',)
        for cars in car:
            lists.append(cars['id'])
        for stuff in lists:
            self.id_choosen['values'] += (stuff,)


        #dropdown.set(lists)
        self.id_choosen.place(x=175, y=45)
        self.id_choosen.current()

        root_car_delete.btn_ok = Button(root_car_delete, text='Delete Car', fg='red', command=self.delete_car_get)
        root_car_delete.btn_ok.place(x=200, y=115)



    def delete_car_get(self):
        ca_id = self.id_choosen.get()

        result = requests.delete(f'http://localhost:5000/cars/{ca_id}/')





#-----------------------------------------------------------------------------------------------------------------------


    def customer_view(self):
        root_customer = Tk()
        root_customer.geometry('465x250+430+160')

        root_customer.customer_home_btn = Button(root_customer, text='Home', fg='blue', width=15, height=3,
                                       command=root_customer.destroy)
        root_customer.customer_home_btn.pack(side='bottom', padx=1, pady=1)

        root_customer.customer_read_btn = Button(root_customer, text='Read customer', width=15, height=3,
                                                 command=self.customer_read_view)
        root_customer.customer_read_btn.pack(side='left', padx=1, pady=1)
        root_customer.customer_read_btn.pack()

        root_customer.customer_add_btn = Button(root_customer, text='Add customer', width=15, height=3,
                                                command=self.customer_add_view)
        root_customer.customer_add_btn.pack(side='left', padx=1, pady=1)
        root_customer.customer_add_btn.pack()

        root_customer.customer_edit_btn = Button(root_customer, text='Edit customer', width=15, height=3,
                                                 command=self.customer_edit_view)
        root_customer.customer_edit_btn.pack(side='left', padx=1, pady=1)
        root_customer.customer_edit_btn.pack()

        root_customer.customer_delete_btn = Button(root_customer, text='Delete customer', width=15, height=3,
                                                   command=self.customer_delete_view)
        root_customer.customer_delete_btn.pack(side='left', padx=1, pady=1)
        root_customer.customer_delete_btn.pack()


    def customer_read_view(self):
        root_cusomter_read = Tk()
        root_cusomter_read.geometry('465x250+430+160')

        root_cusomter_read.car_home_btn = Button(root_cusomter_read, text='Back', fg='blue', width=15, height=3,
                                       command=root_cusomter_read.destroy)
        root_cusomter_read.car_home_btn.pack(side='bottom', padx=1, pady=1)

        root_cusomter_read.car_home_label = Label(root_cusomter_read, text='Customer Details')
        root_cusomter_read.car_home_label.pack(side='top')

        read = requests.get('http://localhost:5000/customers/')
        customer = read.json()
        lists=[]
        for customers in customer:
            list = (f"id: {customers['id']}, name: {customers['name']}, email: {customers['email']}, "
                    f"telephone: {customers['telephone']}\n ")
            lists.append(list)

        Lb1 = Listbox(root_cusomter_read, width=70, height=25)
        n = 0
        for x in lists:
            Lb1.insert(n, lists[int(n)])
            n +=1
        Lb1.pack()

    def customer_add_view(self):
        root_customer_add = Tk()
        root_customer_add.geometry('465x250+430+160')

        root_customer_add.customer_home_btn = Button(root_customer_add, text='Back', fg='blue', width=15, height=3,
                                       command=root_customer_add.destroy)
        root_customer_add.customer_home_btn.pack(side='bottom', padx=1, pady=1)

        root_customer_add.title_label = Label(root_customer_add, text='Add Customer')
        root_customer_add.title_label.pack(side='top')

        root_customer_add.label_name = Label(root_customer_add, text='Name:')
        root_customer_add.label_name.place(x=133, y=45)
        self.enter_name = Entry(root_customer_add)
        self.enter_name.place(x=175, y=47)

        root_customer_add.label_email = Label(root_customer_add, text='Email:')
        root_customer_add.label_email.place(x=135, y=65)
        self.enter_email = Entry(root_customer_add)
        self.enter_email.place(x=175, y=67)

        root_customer_add.label_telephone = Label(root_customer_add, text='Telephone:')
        root_customer_add.label_telephone.place(x=110, y=85)
        self.enter_telephone = Entry(root_customer_add)
        self.enter_telephone.place(x=175, y=87)

        root_customer_add.btn_ok = Button(root_customer_add, text='Add Customer', fg='blue',
                                          command=self.add_customer_get)
        root_customer_add.btn_ok.place(x=320, y=67)

    def add_customer_get(self):
        get_name = self.enter_name.get()
        get_email = self.enter_email.get()
        get_telephone = self.enter_telephone.get()

        data = {'name': get_name,
                'email': get_email,
                'telephone': int(get_telephone),
                }

        result = requests.post('http://localhost:5000/customers/', json=data)

        self.enter_name.delete(0, END)
        self.enter_email.delete(0, END)
        self.enter_telephone.delete(0, END)

    def customer_edit_view(self):
        root_customer_edit = Tk()
        root_customer_edit.geometry('465x250+430+160')

        root_customer_edit.car_home_btn = Button(root_customer_edit, text='Back', fg='blue', width=15, height=3,
                                       command=root_customer_edit.destroy)
        root_customer_edit.car_home_btn.pack(side='bottom', padx=1, pady=1)

        root_customer_edit.title_label = Label(root_customer_edit, text='Edit Customer')
        root_customer_edit.title_label.pack(side='top')

        root_customer_edit.dropdown_id = Label(root_customer_edit, text='Find ID:')
        root_customer_edit.dropdown_id.place(x=128, y=45)

        self.dropdown = StringVar()
        self.id_choosen = ttk.Combobox(root_customer_edit, width=27, textvariable=self.dropdown)

        read = requests.get(f"http://localhost:5000/customers/")
        customer = read.json()
        lists = []
        self.id_choosen['values'] = ('None',)
        for customers in customer:
            lists.append(customers['id'])
        for stuff in lists:
            self.id_choosen['values'] += (stuff,)

        # dropdown.set(lists)
        self.id_choosen.place(x=175, y=45)
        self.id_choosen.current()

        root_customer_edit.label_brand = Label(root_customer_edit, text='Name:')
        root_customer_edit.label_brand.place(x=133, y=95)
        self.enter_name = Entry(root_customer_edit)
        self.enter_name.place(x=175, y=97)

        root_customer_edit.label_year = Label(root_customer_edit, text='Email:')
        root_customer_edit.label_year.place(x=135, y=115)
        self.enter_email = Entry(root_customer_edit)
        self.enter_email.place(x=175, y=117)

        root_customer_edit.label_seats = Label(root_customer_edit, text='Telephone:')
        root_customer_edit.label_seats.place(x=110, y=135)
        self.enter_telephone = Entry(root_customer_edit)
        self.enter_telephone.place(x=175, y=137)

        root_customer_edit.btn_ok = Button(root_customer_edit, text='Update Customer', fg='blue',
                                           command=self.edit_customer_get)
        root_customer_edit.btn_ok.place(x=320, y=115)

    def edit_customer_get(self):
        get_name = self.enter_name.get()
        get_email = self.enter_email.get()
        get_telephone = self.enter_telephone.get()

        cu_id = self.id_choosen.get()

        data = {'name': get_name,
                'email': get_email,
                'telephone': get_telephone,
                }

        result = requests.put(f'http://localhost:5000/customers/{cu_id}/', json=data)

        self.enter_name.delete(0, END)
        self.enter_email.delete(0, END)
        self.enter_telephone.delete(0, END)



    def customer_delete_view(self):
        root_customer_delete = Tk()
        root_customer_delete.geometry('465x250+430+160')

        root_customer_delete.car_home_btn = Button(root_customer_delete, text='Back', fg='blue', width=15, height=3,
                                       command=root_customer_delete.destroy)
        root_customer_delete.car_home_btn.pack(side='bottom', padx=1, pady=1)

        root_customer_delete.title_label = Label(root_customer_delete, text='Delete Customer')
        root_customer_delete.title_label.pack(side='top')

        root_customer_delete.dropdown_id = Label(root_customer_delete, text='Find ID:')
        root_customer_delete.dropdown_id.place(x=128, y=45)

        self.dropdown = StringVar()
        self.id_choosen = ttk.Combobox(root_customer_delete, width=27, textvariable=self.dropdown)

        read = requests.get(f"http://localhost:5000/customers/")
        customer = read.json()
        lists = []
        self.id_choosen['values'] = ('None',)
        for customers in customer:
            lists.append(customers['id'])
        for stuff in lists:
            self.id_choosen['values'] += (stuff,)

        # dropdown.set(lists)
        self.id_choosen.place(x=175, y=45)
        self.id_choosen.current()

        root_customer_delete.btn_ok = Button(root_customer_delete, text='Delete Customer', fg='red',
                                             command=self.delete_customer_get)
        root_customer_delete.btn_ok.place(x=185, y=115)

    def delete_customer_get(self):
        cu_id = self.id_choosen.get()

        result = requests.delete(f'http://localhost:5000/customers/{cu_id}/')



#-----------------------------------------------------------------------------------------------------------------------


    def cars_to_customer_view(self):
        root_cars_customer = Tk()
        root_cars_customer.geometry('465x250+430+160')

        root_cars_customer.cars_customer_home_btn = Button(root_cars_customer, text='Home', fg='blue', width=15,
                                                           height=3, command=root_cars_customer.destroy)
        root_cars_customer.cars_customer_home_btn.pack(side='bottom', padx=1, pady=1)

        root_cars_customer.cars_customer_edit_btn = Button(root_cars_customer, text='Add Car to Customer', width=20,
                                                           height=3,
                                                           command=self.car_customer_add_view)
        root_cars_customer.cars_customer_edit_btn.place(x=70, y=70)


        root_cars_customer.cars_customer_delete_btn = Button(root_cars_customer, text='Delete Car from Customer',
                                                             width=20, height=3,
                                                             command=self.car_customer_delete_view)
        root_cars_customer.cars_customer_delete_btn.place(x=230, y=70)



    def car_customer_add_view(self):
        root_car_customer_edit = Tk()
        root_car_customer_edit.geometry('465x250+430+160')

        root_car_customer_edit.car_home_btn = Button(root_car_customer_edit, text='Back', fg='blue', width=15, height=3,
                                       command=root_car_customer_edit.destroy)
        root_car_customer_edit.car_home_btn.pack(side='bottom', padx=1, pady=1)

        root_car_customer_edit.title_label = Label(root_car_customer_edit, text='Add Car to Customer')
        root_car_customer_edit.title_label.pack(side='top')

        self.dropdown = StringVar()
        self.id_choosen1 = ttk.Combobox(root_car_customer_edit, width=27, textvariable=self.dropdown)

        read = requests.get(f"http://localhost:5000/customers/")
        customer = read.json()
        lists=[]
        for customers in customer:
            list = (f"Customer id: {customers['id']}, Name: {customers['name']}\n")
            lists.append(list)

        Lb1 = Listbox(root_car_customer_edit, width=70, height=4)
        n = 0
        for x in lists:
            Lb1.insert(n, lists[int(n)])
            n +=1
        Lb1.pack()

        car_read = requests.get(f"http://localhost:5000/cars/")
        car = car_read.json()
        lists = []
        self.id_choosen1['values'] = ('None',)
        for cars in car:
            lists.append(cars['id'])
        for stuffs in lists:
            self.id_choosen1['values'] += (stuffs,)

        # dropdown.set(lists)
        self.id_choosen1.place(x=175, y=145)
        self.id_choosen1.current()

        root_car_customer_edit.label_customer_id = Label(root_car_customer_edit, text='Customer ID:')
        root_car_customer_edit.label_customer_id.place(x=100, y=95)
        self.enter_customer_id = Entry(root_car_customer_edit)
        self.enter_customer_id.place(x=175, y=97)

        root_car_customer_edit.btn_ok = Button(root_car_customer_edit, text='Add Car to Customer', fg='blue',
                                             command=self.car_customer_edit_get)
        root_car_customer_edit.btn_ok.place(x=325, y=95)

    def car_customer_edit_get(self):
        get_customer_id = self.enter_customer_id.get()


        ca_cu_id = self.id_choosen1.get()

        data = {'customer_id': get_customer_id,
                }

        result = requests.put(f'http://localhost:5000/cars/{ca_cu_id}/customers', json=data)


        self.enter_customer_id.delete(0, END)


    def car_customer_delete_view(self):
        root_car_customer_delete = Tk()
        root_car_customer_delete.geometry('465x250+430+160')

        root_car_customer_delete.car_home_btn = Button(root_car_customer_delete, text='Back', fg='blue', width=15,
                                                       height=3, command=root_car_customer_delete.destroy)
        root_car_customer_delete.car_home_btn.pack(side='bottom', padx=1, pady=1)

        root_car_customer_delete.title_label = Label(root_car_customer_delete, text='Delete Customer from Car')
        root_car_customer_delete.title_label.pack(side='top')

        root_car_customer_delete.dropdown_id = Label(root_car_customer_delete, text='Find Car ID:')
        root_car_customer_delete.dropdown_id.place(x=95, y=95)


        self.dropdown1 = StringVar()
        self.id_choosen1 = ttk.Combobox(root_car_customer_delete, width=27, textvariable=self.dropdown1)
        # self.id_choosen1.place(x=128, y=25)

        car_read = requests.get(f"http://localhost:5000/cars/")
        car = car_read.json()
        lists = []
        self.id_choosen1['values'] = ('None',)
        for cars in car:
            lists.append(cars['id'])
        for stuffs in lists:
            self.id_choosen1['values'] += (stuffs,)

        # dropdown.set(lists)
        self.id_choosen1.place(x=165, y=95)
        self.id_choosen1.current()

        root_car_customer_delete.btn_ok = Button(root_car_customer_delete, text='Delete Customer From Car', fg='red',
                                               command=self.car_customer_delete_get)
        root_car_customer_delete.btn_ok.place(x=165, y=145)

        read = requests.get('http://localhost:5000/cars/')
        car = read.json()
        lists=[]
        for cars in car:
            list = (f"id: {cars['id']}, customer_id: {cars['customer_id']}\n")
            lists.append(list)

        Lb1 = Listbox(root_car_customer_delete, width=70, height=4)
        n = 0
        for x in lists:
            Lb1.insert(n, lists[int(n)])
            n +=1
        Lb1.pack()


    def car_customer_delete_get(self):
        ca_cu_id = self.id_choosen1.get()
        result = requests.delete(f'http://localhost:5000/cars/{ca_cu_id}/customers')




def main():
    #Tkinter window
    root = Tk()

    #Set size and position of the window in string
    root.geometry('465x250+430+160')

    #Add widget here/Create window object
    app = Application(master=root)


    #Run the main loop
    app.mainloop()




if __name__ == '__main__':
    main()