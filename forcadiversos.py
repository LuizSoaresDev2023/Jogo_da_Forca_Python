import os
import random
os.system('cls')

print("\nJOGO DA FORCA\nBy Luiz Soares, developer\n")
input("Pressione Enter para começar:\n\n")

nome = input("\nQual o seu nome? \n\n")
print (f'\nSeja bem vindo(a) {nome} ! Vamos começar o JOGO DA FORCA?')
input ('\nPressione Enter para começar! \n\n')

while True:
    try:
        opcao = int(input("\nEscolha um tema para começar:\n1 - animais;\n2 - países;\n3 - frutas;\n4 - nomes;\nQualquer outro dígito:\n--- Encerrar jogo!\n\n"))
    except ValueError:
        print ("\nPor favor, escolha uma opção válida! ")
        continue

    if opcao == 1:
      print (f'\n{nome}, você escolheu o TEMA 1: - ANIMAIS.\nVamos ver se você é bom mesmo neste tema: \n')
      input ('\nPressione Enter para prosseguir!\n\n')
      
      lista_de_palavras = ['gato', 'cachorro', 'formiga', 'zebra', 'galo', 'galinha', 'elefante', 'veado', 'tigre', 'galinha', 'cavalo', 'cobra', 'rato', 'sapo', 'minhoca', 'pato', 'coruja', 'corvo', 'vespa', 'mosca', 'aranha']
      palavra_selecionada = random.choice (lista_de_palavras).upper()
      tamanho_palavra = len(palavra_selecionada)
      palavra_codificada = ['_']*tamanho_palavra
      quantidade_de_erros = 0

      while '_' in palavra_codificada and quantidade_de_erros < 5:
          print (f'\nSua palavra tem {tamanho_palavra} letras. O tema é animais.')
          print (f'\nErros: {quantidade_de_erros} de 5.')
          for letra in palavra_codificada:
              print (letra, end = ' ')
          print()

          letra_escolhida = input ('\nDigite uma letra (sem acentos ou cedilhas por favor): ').upper()
          acertou = False
          for i in range(len(palavra_selecionada)):
              if letra_escolhida == palavra_selecionada[i]:
                  palavra_codificada [i] = letra_escolhida
                  acertou = True

          if acertou == True:
              print (f'\nParabéns {nome}! Você acertou essa letra!')
          else:
              print ('\nErrou!!! Essa letra não faz parte da palavra secreta!')
              quantidade_de_erros = quantidade_de_erros + 1

      if quantidade_de_erros == 5:
          print (f'\nFala sério, {nome}! Você perdeu! Deu moleee! 😿💩')
      else: print (f'\nParabéns, {nome}! Você ganhou!!! 😀😁😎🏆🥇')

      print (f'\nA palavra secreta era: {palavra_selecionada}')

      input ('\nPressione Enter para retornar!')


    elif opcao == 2:
      print (f'\n{nome}, você escolheu o TEMA 2: - PAÍSES.\nVamos ver se você é bom mesmo neste tema: \n')
      input ('\nPressione Enter para prosseguir!\n\n')
      
      lista_de_palavras = ['brasil', 'jamaica', 'egito', 'argentina', 'uruguai', 'venezuela', 'dinamarca', 'italia', 'nigeria', 'china', 'belgica', 'alemanha', 'japao', 'holanda', 'inglaterra', 'peru', 'mexico', 'portugal', 'suica', 'suecia', 'bulgaria']
      palavra_selecionada = random.choice (lista_de_palavras).upper()
      tamanho_palavra = len(palavra_selecionada)
      palavra_codificada = ['_']*tamanho_palavra
      quantidade_de_erros = 0

      while '_' in palavra_codificada and quantidade_de_erros < 5:
          print (f'\nSua palavra tem {tamanho_palavra} letras. O tema é países.')
          print (f'\nErros: {quantidade_de_erros} de 5.')
          for letra in palavra_codificada:
              print (letra, end = ' ')
          print()

          letra_escolhida = input ('\nDigite uma letra (sem acentos ou cedilhas, por favor): ').upper()
          acertou = False
          for i in range(len(palavra_selecionada)):
              if letra_escolhida == palavra_selecionada[i]:
                  palavra_codificada [i] = letra_escolhida
                  acertou = True

          if acertou == True:
              print (f'\nParabéns {nome}! Você acertou essa letra!')
          else:
              print ('\nErrou!!! Essa letra não faz parte da palavra secreta!')
              quantidade_de_erros = quantidade_de_erros + 1

      if quantidade_de_erros == 5:
          print (f'\nFala sério, {nome}! Você perdeu! Deu moleee! 😿💩')
      else: print (f'\nParabéns, {nome}! Você ganhou!!! 😀😁😎🏆🥇')

      print (f'\nA palavra secreta era: {palavra_selecionada}')

      input ('\nPressione Enter para retornar!')


    elif opcao == 3:
      print (f'\n{nome}, você escolheu o TEMA 3: - FRUTAS.\nVamos ver se você é bom mesmo neste tema: \n')
      input ('\nPressione Enter para prosseguir!\n\n')
      
      lista_de_palavras = ['abacaxi', 'framboesa', 'ameixa', 'caju', 'cereja', 'figo', 'goiaba', 'jaca', 'limao', 'laranja', 'kiwi', 'maca', 'morango', 'manga', 'pera', 'pessego', 'tangerina', 'uva', 'damasco', 'banana', 'acerola']
      palavra_selecionada = random.choice (lista_de_palavras).upper()
      tamanho_palavra = len(palavra_selecionada)
      palavra_codificada = ['_']*tamanho_palavra
      quantidade_de_erros = 0

      while '_' in palavra_codificada and quantidade_de_erros < 5:
          print (f'\nSua palavra tem {tamanho_palavra} letras. O tema é frutas.')
          print (f'\nErros: {quantidade_de_erros} de 5.')
          for letra in palavra_codificada:
              print (letra, end = ' ')
          print()

          letra_escolhida = input ('\nDigite uma letra (sem acentos ou cedilhas, por favor): ').upper()
          acertou = False
          for i in range(len(palavra_selecionada)):
              if letra_escolhida == palavra_selecionada[i]:
                  palavra_codificada [i] = letra_escolhida
                  acertou = True

          if acertou == True:
              print (f'\nParabéns {nome}! Você acertou essa letra!')
          else:
              print ('\nErrou!!! Essa letra não faz parte da palavra secreta!')
              quantidade_de_erros = quantidade_de_erros + 1

      if quantidade_de_erros == 5:
          print (f'\nFala sério, {nome}! Você perdeu! Deu moleee! 😿💩')
      else: print (f'\nParabéns, {nome}! Você ganhou!!! 😀😁😎🏆🥇')

      print (f'\nA palavra secreta era: {palavra_selecionada}')

      input ('\nPressione Enter para retornar!')


    elif opcao == 4:
      print (f'\n{nome}, você escolheu o TEMA 4: - NOMES.\nVamos ver se você é bom mesmo neste tema: \n')
      input ('\nPressione Enter para prosseguir!\n\n')
      
      lista_de_palavras = ['amanda', 'bruno', 'evelin', 'luiz', 'jose', 'jessica', 'dominique', 'davi', 'renata', 'paula', 'rodrigo', 'arthur', 'pedro', 'viviane', 'elisangela', 'pamela', 'vanessa', 'barbara', 'janaina', 'carlos', 'fernando']
      palavra_selecionada = random.choice (lista_de_palavras).upper()
      tamanho_palavra = len(palavra_selecionada)
      palavra_codificada = ['_']*tamanho_palavra
      quantidade_de_erros = 0

      while '_' in palavra_codificada and quantidade_de_erros < 5:
          print (f'\nSua palavra tem {tamanho_palavra} letras. O tema é nomes.')
          print (f'\nErros: {quantidade_de_erros} de 5.')
          for letra in palavra_codificada:
              print (letra, end = ' ')
          print()

          letra_escolhida = input ('\nDigite uma letra (sem acentos ou cedilhas, por favor): ').upper()
          acertou = False
          for i in range(len(palavra_selecionada)):
              if letra_escolhida == palavra_selecionada[i]:
                  palavra_codificada [i] = letra_escolhida
                  acertou = True

          if acertou == True:
              print (f'\nParabéns {nome}! Você acertou essa letra!')
          else:
              print ('\nErrou!!! Essa letra não faz parte da palavra secreta!')
              quantidade_de_erros = quantidade_de_erros + 1

      if quantidade_de_erros == 5:
          print (f'\nFala sério, {nome}! Você perdeu! Deu moleee! 😿💩')
      else: print (f'\nParabéns, {nome}! Você ganhou!!! 😀😁😎🏆🥇')

      print (f'\nA palavra secreta era: {palavra_selecionada}')

      input ('\nPressione Enter para retornar!')


    else:
      print(f"\nJogo encerrado! \nObrigado por jogar, {nome}! Até a próxima!")
      print("Siga @luizsoares.designer.dev no Instagram! 🙂👍 ")
      input()
      break

    





