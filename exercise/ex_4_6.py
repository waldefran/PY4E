'''
    Devo capturar os valores de entrada do usuário
'''
def computepay(h, r):
    fh = float(h)
    fr = float(r)
    he = (fh-40)
    if fh > 40:
        pay = he*(fr*1.5)+(40*fr)
    else:
        pay = fh*fr
    return pay

#Entrada do usuário
print("----------------")
print("Cacula Pagamento")
print("----------------")

hrs = input("Informe a quantidade de horas trabalhadas: ")
re = input("Informe o valor da hora: ")

print(computepay(hrs, re))