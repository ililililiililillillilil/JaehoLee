def T(Sum):
    Total = round(Sum * tax, 2)
    return Total

def Tat(Sum):
    Sales_tax = T(Sum)
    Total_after_tax = round(Sum + Sales_tax, 2)
    return Total_after_tax

def S():
    print("ENTER ITEMS (ENTER 0 TO END)")
    Sum = 0
    while True:
        Coi = float(input("Cost of item: "))
        if Coi == 0:
            break
        Sum += Coi
    return Sum

def Results(Sum):
    sales_tax = T(Sum)
    total_after_tax = Tat(Sum)
    print(f"Total:  {Sum}")
    print(f"Sales tax:\t{sales_tax}")
    print(f"Total after tax: {total_after_tax}\n")