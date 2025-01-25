print('estação de conversão de kg,G,Mg')
print('Unidades de medida ')
print('G')
print('Mg')
escolha = int(input('Qual a seu valor = '))
escolha2 = str(input('Escolha uma das unidades para converter = '))

if escolha2 == 'G'or 'g':
  calculo = escolha * 1000
  print(f'Sua escolha =({escolha}) convertido para Gramas =({calculo})')

elif escolha2 == 'Mg'or 'mg' or 'MG' or 'mG':
  calculo_2 = escolha * 1000000
  print(f'Sua escolha =({escolha}) convertido para Gramas =({calculo_2})')
