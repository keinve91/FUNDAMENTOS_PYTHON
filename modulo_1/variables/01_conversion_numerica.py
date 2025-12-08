# Definimos una variable con decimales (float)
float_a = 1.25

# USANDO int():
# Convierte el float a entero.
# Nota: No redondea, simplemente "corta" (trunca) la parte decimal.
resultado_int = int(float_a)
print(resultado_int)  # Salida: 1

# USANDO float():
# Convierte un entero a decimal agregando .0 al final.
numero_entero = 5
resultado_float = float(numero_entero)
print(resultado_float) # Salida: 5.0