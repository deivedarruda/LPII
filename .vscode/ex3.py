dias_semana = ("segunda", "teça", "quarta", "quinta", "sexta")

print(type(dias_semana))
print()
print(dias_semana)
print()
print(dias_semana[3])
print()
for i in range(len(dias_semana)):
    print(dias_semana[i])

from Exercício import minutos

R, h = minutos(125)
print("%dh %dm"%(R,h))
print()
R, h = minutos(249)
print("%dh %dm"%(R,h))