def f():
    global x
    x+=1

x = 0
print(x)
f()
print(x)