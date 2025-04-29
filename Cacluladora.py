class Calculadora:
    def suma(self, a ,b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return " División por cero"

calculadora = Calculadora()


print("Bienvenido a la calculadora")
print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Elige una operación : ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == "1":
    print("Resultado:", calculadora.suma(num1, num2))
elif opcion == '2':
    print("Resultado:", calculadora.resta(num1, num2))
elif opcion == '3':
    print("Resultado:", calculadora.multiplicacion(num1, num2))
elif opcion == '4':
    print("Resultado:", calculadora.division(num1, num2))
else:
    print("Opción no válida")



