expression = input("Expression: ")
x, y, z = expression.split(" ")

new_x = float(x)
new_z = float(z)

match y:
    case "+":
        result = new_x + new_z
    case "-":
        result = new_x - new_z
    case "*":
        result = new_x * new_z
    case "/":
        result = new_x / new_z

print(f"{result:.1f}")