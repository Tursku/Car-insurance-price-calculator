# -*- coding: utf-8 -*-
from op import insuranceOp
from if_ import insuranceIf

# Enter all the info here
hetu=   ("281098-5793") # <--- SSN Here
reg=    ("NIX-405")     # <--- Registeration 
km=     ("30000")       # <--- KM 
address=("Itainen Rantakatu 52")    # <--- Address
post=   ("20810")                   # <--- Postal code



insuranceOp(reg, hetu, km)
insuranceIf(reg, hetu, km, address, post)



