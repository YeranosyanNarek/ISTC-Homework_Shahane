try:
    a = 10              # 'a' is 'int' type object
    print(a.name)       # the object 'a' has no function <.name>
except Exception:
    print("AttributeError: 'int' object has no attribute 'name'")
