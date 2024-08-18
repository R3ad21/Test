def f():
    global x
    x*=2

x = 0
print(x)
f()
print(x)