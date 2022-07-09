def myfunc(n):
   return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(2))
print(mytripler(3))