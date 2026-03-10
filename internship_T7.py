#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""Problem 1: Smart Light Controller
Problem Statement
Create a class to control a smart light that can be turned ON or OFF and display its status.
🌍 Real-Time Use
Smart home automation systems
📥 Sample Input
Light Name: Bedroom Light
Action: ON
📤 Expected Output
Bedroom Light is ON"""

class SmartLight:
    def __init__(self, name):
        self.name = name

    def control(self, action):
        print(self.name + " is " + action)


light = SmartLight("Bedroom Light")
light.control("ON")
light = SmartLight("Bedroom Light")
light.control("OFF")


# In[7]:


"""Problem 2: Employee ID Card System
 Problem Statement
Create a class that stores employee name, ID, and department and displays ID card details.
Real-Time Use
Corporate HR systems
📥 Sample Input
Employee Name: Rahul
Employee ID: EMP102
Department: IT

📤 Expected Output
Employee ID Card
Name: Rahul
ID: EMP102
Department: IT

"""

class emp:
    def __init__(self,emp_name,emp_id,dep):
        self.emp_name=emp_name
        self.emp_id=emp_id
        self.dep=dep
    def show(self):
        print(f"Employee Name: {self.emp_name}\nEmployee ID: {self.emp_id}\nDepartment:{self.dep}")
        
x=emp("Valli",123,"IT")
x.show()

y=emp("Rukmini",321,"IT")
y.show()


# In[10]:


"""Problem 3: Mobile Contact Record
Problem Statement
Create a class to store contact name and phone number and display contact information.
Real-Time Use
Mobile contact applications
📥 Sample Input
Contact Name: Anita
Phone Number: 9876543210
📤 Expected Output
Contact Saved
Name: Anita
Phone: 9876543210
"""

class Mobile:
    def __init__(self,name,phno):
        self.name=name
        self.phno=phno
    def show(self):
        print(f"Contact Name:{self.name}\nPhone Number:{self.phno}")
        
x=Mobile("Anita",9876543210)
x.show()


# In[2]:


"""Problem 4: Product Price Tag Generator
Problem Statement
Create a class that stores product name and price and prints a formatted price tag.
 Real-Time Use
Retail billing systems
📥 Sample Input
Product Name: Headphones
Price: 2499
📤 Expected Output
Product: Headphones
Price: ₹2499
"""

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def show(self):
        print(f"Name:{self.name}\nPrice:{self.price}")
        
x=Product("Headphones",2499)
x.show()


# In[3]:


"""Problem 5: Movie Rating Display System
Problem Statement
Create a class that stores movie name and rating and displays movie details.
Real-Time Use
Streaming platforms
📥 Sample Input
Movie Name: Inception
Rating: 4.8
📤 Expected Output
Movie: Inception
Rating: 4.8 / 5
"""

class Movie:
    def __init__(self,name,Rating):
        self.name=name
        self.Rating=Rating
    def show(self):
        print(f"Name:{self.name}\nPrice:{self.Rating}/5")
        
x=Movie("Inception",4.8)
x.show()


# In[8]:


"""Problem 6: Delivery Address Manager
Problem Statement
Create a class that stores customer name and delivery address and prints delivery details.
Real-Time Use
Courier and logistics platforms
📥 Sample Input
Customer Name: Suman
Address: Hyderabad
📤 Expected Output
Delivery Details
Customer: Suman
Address: Hyderabad
"""

class Delivery:
    def __init__(self,name,Address):
        self.name=name
        self.Address=Address
    def show(self):
        print(f"Customer:{self.name}\nAddress:{self.Address}")
        
x=Delivery("Suman","Hyderabad")
x.show()


# In[ ]:





# In[ ]:




