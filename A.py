def f_to_m(n):
    return round(n * 0.3048, 2)

def m_to_f(n):
    return round(n / 0.3048, 2)

def menu():
    print("Conversions Menu:")
    print("a.\tFeet to Meters")
    print("b.\tMeters to Feet")
    selection = input("Select a conversion (a/b):")
    return selection