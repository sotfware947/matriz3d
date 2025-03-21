def calcular_descuento(monto_total, porcentaje_descuento=10):
	# calcula el monto del descuento en funcion del porcentaje dado.
	# *param monto_total: float - monto total de la compra
	# *param porcentaje_descuento: float - porcentaje de descuento (por defecto es 10%)

	descuento = (monto_total * porcentaje_descuento) / 100
	return descuento

# Llamadas a la funcion
monto1 = 200.0
monto2 = 400.0
porcentaje_descuento2 = 20

descuento1 = calcular_descuento(monto1)
descuento2 = calcular_descuento(monto2, porcentaje_descuento2)

# Calculo del monto final a pagar 
monto_final1 = monto1 - descuento1
monto_final2 = monto2 - descuento2

# Mostrar resultados
print(f"compra 1: monto total: ${monto1:.2f}, descuento: ${descuento1:.2f}, monto final: ${monto_final1:.2f}")
print(f"compra 2: monto total: ${monto2:.2f}, descuento: ${descuento2:.2f}, monto final: ${monto_final2:.2f}")