def g():
    print("XEER")
def y():
    print("YEER")
def f():
    global x
    x*=2
    g()
g()
x = 0
print(x)
f()
print(x)