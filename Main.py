
from op import insuranceOp
from if_ import insuranceIf

# Enter all the info here
hetu=   ("mmddyy-1234") # <--- SSN Here
reg=    ("ABC-123")     # <--- Registeration 
km=     ("30000")       # <--- KM 
address=("Itäinen Rantakatu 2")    # <--- Address
post=   ("20810")                   # <--- Postal code



insuranceOp(reg, hetu, km)
insuranceIf(reg, hetu, km, address, post)



