import random, string

#objeto para receber o tamanho da senha
tamanho = 16

#estrutura da senha que será gerada
#metodo ascii_letters da lib string gera letras maiusculas e minusculas
#metodo digits da lib string seta somente digitos numerários 
chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+,.;:/?'

#na lib random, chama a função para gerar numeros aleatórios 
rnd = random.SystemRandom() #os.random


#rnd.choice(chars) => retorna uma lista com caracteres randomicos
#for alimenta a lista
print(''.join(rnd.choice(chars) for i in range (tamanho)))

