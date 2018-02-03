def escolher_palavra (palavra_escondida):
  palavra=input()
  return palavra_escondida==palavra
    


print ("Escolha uma palavra")
palavra_escondida=input()
for i in range(0,len(palavra_escondida)):
  print ("_ ",end="")
descoberto = False  
tentativas=[]
while descoberto == False:
  print ("caractere ou palavra")
  opcao=input()
  if opcao=="caractere":
    print("")
    caractere=input()
    if len(caractere)==1 :
      tentativas+= caractere
  elif opcao=="palavra":
   descoberto= escolher_palavra(palavra_escondida)
   if(not(descoberto)):
    for i in range(0,len(palavra_escondida)):
      if palavra_escondida[i] in tentativas:
        print (palavra_escondida[i], end='')
      else:
        print("_ ",end='')

