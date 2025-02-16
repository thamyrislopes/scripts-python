nome = 'Thamyris'
cores = {'limpa':'\033[m', 
         'vermelho':'\033[31m', 'amarelo':'\033[33m', 
         'peb':'\033[7;30m'}
print('Olá! Tudo bem, {}{}{}?'.format(cores['vermelho'], nome, cores['limpa']))