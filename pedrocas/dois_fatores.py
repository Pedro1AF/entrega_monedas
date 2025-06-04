import random
codigo = random.randint(10000, 99999)
banco_db = "exemplo.alo@gmail.com"
email = input("Insira seu email: ")

if email == banco_db:
    print(f"codigo de verificação enviado para {email.replace(email[4:], '*********@gmail.com')}")
    print(codigo)
else:
    print("Email inválido")
    exit()
    
verific = int(input("Insira o codigo: ")) 

if verific == codigo:
    print("Email verificado com sucesso! Redirecionando para pagina...")
else:
    print("Codigo inválido!")