#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Created on Mon Jan  4 20:08:27 2016
@author: giovanni
"""

brand = "Apple"
rate = 12.23411

prijs = 123.456

#message = "De prijs van een %s Computer is %4.2f \n\
#bij een precentage van %4.2f"%(brand,prijs,rate)

message = "De  prijs van een {0:s} is {2:4.2f} \n\
bij een prijs van {2:4.2f}".format(brand,prijs,rate)

print(message)

