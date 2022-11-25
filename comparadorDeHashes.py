import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

#construtor new que recebe qual o algoritmo de hash será utilizado
hash1 = hashlib.new('ripemd160')

#o update fará a comparação do hash, pegando o arquivo1 e o método rb fará a leitura 
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

#função digest resume o registro pssado pelo método update
if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diiferente do arquivo: {arquivo2}')
    #para printar o hash dos arquivos: 
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())

else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())