try:
    a = 10
    print(a.name)
except Exception:
    print("AttributeError: 'int' object has no attribute 'name'")