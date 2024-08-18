def g():
    print("XEER")
def f():
    global x
    x*=2
    g()
g()
x = 0
print(x)
f()
print(x)