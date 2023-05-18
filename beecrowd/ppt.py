while True:
 print('Jogo pedra papel e tesoura\nDigite: \npedra para pedra\npapel para papel\ntesoura para tesoura\nPedra Papel Tesouuura!')
 j1 = input('Selecione a primeira jogada: ')
 j2 = input('Selecione a segunda jogada: ')
 # 1 = pedra
 # 2 = papel
 # 3 = tesoura
 #Caso empate
 if j1 == j2:
  print('Empate')

 #Caso jogue pedra
 if j1 == 'pedra':
  if j2 == 'papel':
     print('Papel ganhou')
  if j2 == 'tesoura':
     print('Pedra ganhou')
 
 #Caso jogue papel
 if j1 == 'papel':
    if j2 == 'pedra':
     print('Papel ganha')
    if j2 == 'tesoura':
     print('Tesoura ganhou')

 #Caso jogue tesoura
 if j1 == 'tesoura':
    if j2 == 'pedra':
     print('Pedra ganhou')
    if j2 == 'papel':
     print('Tesoura ganhou')
 print('Use x para sair e y para continuar')
 sair = input()
 if sair == 'x':
   break
