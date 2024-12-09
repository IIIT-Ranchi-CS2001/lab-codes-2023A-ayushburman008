#Calculate perimeter area and angles using sides of triangle
import math
a = float(input("Enter the length of first side: "))
b = float(input("Enter the length of Second side: "))
c = float(input("Enter the length of third side: "))
perimeter = a + b + c
semp = perimeter / 2
area = math.sqrt(semp * (semp - a) * (semp - b) * (semp - c))
ang_a1 = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
ang_b2 = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
ang_c3 = 180 - ang_a1 - ang_b2
print("The sides are:", a, b, c)
print("The perimeter is:", perimeter)
print("The area is:", area)
print("The angles are:", ang_a1, ang_b2, ang_c3)