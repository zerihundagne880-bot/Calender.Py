import math

a = float(input("pls enter the value of a: "))
b = float(input("pls enter the value of b: "))
c = float(input("pls enter the value of c: "))

# dic (discriminant) ስሌት
dic = pow(b, 2) - (4 * a * c)

if dic > 0:
    # ስህተቱ እዚህ ጋር ነበር: math.sqrt() መሆን አለበት እና dic ብቻ ነው በሩት ውስጥ የሚገባው
    root1 = (-b + math.sqrt(dic)) / (2 * a)
    root2 = (-b - math.sqrt(dic)) / (2 * a)
    
    print("the equation has two roots")
    print(f"the first root is {root1}")
    print(f"the second root is {root2}")

elif dic == 0:
    root = -b / (2 * a)
    print(f"the equation has one root: {root}")

else:
    print("the equation has complex roots")

