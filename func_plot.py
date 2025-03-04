import numpy as np
import matplotlib.pyplot as plt

start = float(input("Enter start value: "))
end = float(input("Enter end value: "))
step = int(input("Enter step value: "))

x = np.linspace(start, end, step)

print("Choose a function to plot:")
print("1. y = x")
print("2. y = x^2")
print("3. y = x^3")
print("4. y = 1/x")
print("5. y = sqrt(x)")
print("6. y = cbrt(x)")
print("7. y = x^n")
print("8. y = e^x")
print("9. y = sin(x)")
print("10. y = cos(x)")
print("11. y = tan(x)")
print("12. y = ln(x)")
print("13. y = arcsin(x)")
print("14. y = arccos(x)")
print("15. y = arctan(x)")
print("16. y = sinh(x)")
print("17. y = cosh(x)")
print("18. y = tanh(x)")
print("19. y = asinh(x)")
print("20. y = acosh(x)")
print("21. y = atanh(x)")

choice = int(input("Enter your choice: "))
if choice == 1:
    y = x
    func_name = 'y = x'
elif choice == 2:
    y = x**2
    func_name = 'y = x^2'
elif choice == 3:
    y = x**3
    func_name = 'y = x^3'
elif choice == 4:
    y = 1/x
    func_name = 'y = 1/x'
elif choice == 5:
    y = np.sqrt(x)
    func_name = 'y = sqrt(x)'
elif choice == 6:
    y = np.cbrt(x)
    func_name = 'y = cbrt(x)'
elif choice == 7:
    n = float(input("Enter the value of n: "))
    y = x**n
    func_name = f'y = x^{n}'
elif choice == 8:
    y = np.exp(x)
    func_name = 'y = e^x'
elif choice == 9:
    y = np.sin(x)
    func_name = 'y = sin(x)'
elif choice == 10:
    y = np.cos(x)
    func_name = 'y = cos(x)'
elif choice == 11:
    y = np.tan(x)
    func_name = 'y = tan(x)'
elif choice == 12:
    y = np.log(x)
    func_name = 'y = ln(x)'
elif choice == 13:
    y = np.arcsin(x)
    func_name = 'y = arcsin(x)'
elif choice == 14:
    y = np.arccos(x)
    func_name = 'y = arccos(x)'
elif choice == 15:
    y = np.arctan(x)
    func_name = 'y = arctan(x)'
elif choice == 16:
    y = np.sinh(x)
    func_name = 'y = sinh(x)'
elif choice == 17:
    y = np.cosh(x)
    func_name = 'y = cosh(x)'
elif choice == 18:
    y = np.tanh(x)
    func_name = 'y = tanh(x)'
elif choice == 19:
    y = np.asinh(x)
    func_name = 'y = asinh(x)'
elif choice == 20:
    y = np.acosh(x)
    func_name = 'y = acosh(x)'
elif choice == 21:
    y = np.atanh(x)
    func_name = 'y = atanh(x)'
else:
    print("Invalid choice")
    exit()

# Create the plot
plt.plot(x, y)

# Add title and labels
plt.title(func_name)
plt.xlabel('x')
plt.ylabel(func_name)

# Show the plot
plt.show()