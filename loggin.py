try:
    arquivo = open("idjogo.txt","r")
    ids = arquivo.readlines()
    print(ids)
    
    
except:
    arquivo = open("idjogo.txt","w")
    nome = input("Digite seu nome: ")
    arquivo.write("Nome: ")
    arquivo.write(nome)
    arquivo.write("\n")
    email = input("Digite seu e-mail: ")
    arquivo.write("e-mail: ")
    arquivo.write(email)
    arquivo.write("\n")