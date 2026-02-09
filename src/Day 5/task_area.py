def calc_rectangale(length,width):
    area=length*width
    perimeter=2*(length+width)
    return area,perimeter
length=float(input("Enter the length:"))
width=float(input("Enter the width :"))
area,perimeter=calc_rectangale(length,width)
print(f"Area of :{area},perimeter:{perimeter}")
