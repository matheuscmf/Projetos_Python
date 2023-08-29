from datetime  import date # Importa a biblioteca datetime
import sys # Importa a biblioteca sys

date.today() # Retorna a data atual

print("A data de hoje é: "+str(date.today())) # Imprime a data atual

parsec = 25
anosluz = parsec * 3.26

print("A conversão de 25 parsecs em anos-luz é: "+str(anosluz)+" anos-luz") # Imprime a conversão de 25 parsecs em anos-luz

print(sys.argv) # Imprime os argumentos passados na linha de comando

print(sys.argv0) # Imprime o nome do arquivo que está sendo executado na linha de comando e é uma matriz

print(sys.argv[1]) # Imprime o primeiro argumento passado na linha de comando

print(sys.argv[2]) # Imprime o segundo argumento passado na linha de comando

nome = input("Digite seu nome: ") # Entrada do usuário

idade = input("Digite sua idade: ") # Entrada do usuário

print("Seu nome é: "+nome+" e sua idade é: "+idade) # Imprime o nome e a idade do usuário