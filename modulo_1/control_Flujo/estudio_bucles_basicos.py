# Los bucles 'for' permiten iterar sobre una secuencia (lista, tupla, etc.)
# y aplicar la misma lógica a cada elemento.

# 1. Automatizando la lógica condicional con un Bucle
# En lugar de escribir un 'if' para cada cliente, usamos un 'for' para recorrer una lista.
customer_list = [20, 5, 10]

print("--- Automatización de clasificación de clientes ---")
for i_customer in customer_list:
    # Para cada 'i_customer' en la lista, se ejecuta esta lógica:
    if i_customer > 15:
        print(f"Valor {i_customer}: high")
    elif i_customer < 10:
        print(f"Valor {i_customer}: low")
    else:
        print(f"Valor {i_customer}: med")

# 2. Iterando sobre una Tupla
# Los bucles funcionan igual con tuplas (estructuras inmutables).
tuple1 = ('John', 10, 25, 30, 50, 'Mary')

print("\n--- Imprimiendo elementos de una tupla ---")
for i in tuple1:
    print(i)