saldo = 2000.0
saque_max = 0
while True:
  opcao = int(input("""
============================
        banco maneiro
============================
[1] Sacar
[2] Extrato
[3] Depositar                    
[4] Sair                    
Informe uma opção: """ ))

  if opcao == 1:
    if saque_max < 3:
      while saldo > 0:
        saque = float(input("Informe o valor do saque: "))

        if saque <= 0 and saque > 500:
          print("\nPor favor, insira um valor válido e/ou dentro do limite!\n")
          continue

        elif saldo >= saque:
          print("Realizando saque...")
          saldo -= saque
          print("Saldo realizado!")
          print(f'\nSaldo atual: R$ {saldo:.2f}\n')
          saque_max += 1
          break
        else:
          print("\nSaldo insuficiente para saque.\n")
    else:
      print('\nLimite diário atingido.\n')

  elif opcao == 2:
    print(f'\nO seu extrato atual é: R$ {saldo:.2f}\n')
  elif opcao == 3:
    deposito = float(input("Informe o valor do Deposito: "))
    saldo += deposito
    print(f'Saldo atual: R$ {saldo:.2f}')
    opcao = 0
  elif opcao == 4:
    print("Saindo...")
    break
  else:
    print("\nOpção inválida\n")