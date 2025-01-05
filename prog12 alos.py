print ("======== OR ========")
x = 2
y = 3
z = True
nilai = x or y or True
print(x, "or" , y, "or" , True,  "=", nilai)

x = True
y = True
nilai = x or y
print(x, "or" , y, "=", nilai)

x = False
y = False
nilai = x or y
print(x, "or" , y, "=", nilai)

x = False
y = True
nilai = x or y
print(x, "or" , y, "=", nilai)

print ("======== XOR ========")
x = True
y = False
nilai =(x or y) and not (x and y)
print({x, "xor" , y}, "=", nilai)

x = True
y = True
nilai =(x or y) and not (x and y)
print({x, "xor" , y}, "=", nilai)

x = False
y = False
nilai =(x or y) and not (x and y)
print({x, "xor" , y}, "=", nilai)

x = False
y = True
nilai =(x or y) and not (x and y)
print({x, "xor" , y}, "=", nilai)
