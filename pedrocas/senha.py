servidor = ['pedro', 'luis', 'guilherme'] #representar uma consulta ao servidor
senha = []
usuario = input("insira seu nome: ".lower()) #representar entrada de dados
if usuario in servidor: #representar uma consulta onde o usuario tem de existir no servidor e ser valido
    print("usuario encontrado")
    print("Redefina sua senha")
    nova_senha = input("insira sua nova senha: ")
else:
    print("usuario nao encontrado, tente novamente")
    exit()

confirmação_senha = input("insira sua nova senha novamente: ")

if confirmação_senha == nova_senha:
    print("senha redefinida com sucesso")
    senha.append(nova_senha)
    print(senha)
else:
    print("por favor tente novamente as senhas nao condizem")
