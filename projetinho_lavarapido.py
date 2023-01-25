# Projeto Lava rápido - fase 1 


# Mostrar serviços do lava-rápido
print('Tipo de serviços')
serviços = ['ducha simples' , 'ducha completa' , 'lavagem de motor', 'polimento', 'ducha com cera', 'ducha completa com cera']
for item in serviços:
    print(item)

# Valores dos Serviços
ducha_simples = 15
ducha_completa = 30 
lavagem_de_motor = 80 # sem ducha
polimento = 350
ducha_com_cera = 20
ducha_completa_com_cera = 35

print('Valores dos Serviços')
# Preços = 'Ducha simples' ducha_simples, 'Ducha completa' ducha_completa, 'Lavagem de Motor' lavagem_de_motor, 'Polimento' polimento, 'Ducha com cera'ducha_com_cera, 'Ducha completa com cera' ducha_completa_com_cera
# for item in Preços:
#     print(item)


# Faturamento médio do Lava rápido 
faturamento = 5000
Produtos = 700
Funcionários = 1500
Despesas=(Produtos + Funcionários)
Lucros=(faturamento - Produtos - Funcionários) 
Porcentagem_de_Lucro=(Lucros / Despesas * 100) 


print('Débitos', Despesas)
print('Lucros', Lucros) 
print('Porcentagem de Lucro', Porcentagem_de_Lucro)


