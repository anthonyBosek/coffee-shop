#!/usr/bin/env python3
# import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee


cust1 = Customer("aust")
cust2 = Customer("kat")
cust3 = Customer("al")
c1 = Coffee("mocha")
c2 = Coffee("drip")
c3 = Coffee("fancy machiato")
o1 = Order(cust2, c1, 5.00)
o2 = Order(cust3, c3, 9.50)

if __name__ == "__main__":
    print("HELLO! :) let's debug")


print("here is my break")
# ipdb.set_trace()
