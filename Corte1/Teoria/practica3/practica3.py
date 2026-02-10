while True:
  a = input("porfavor ingrese un valor: ")
  aint =int(a)
  mod = aint%2

  if(mod == 0):
     print("a es un PAR")
  else:
     print("a no es PAR, es IMPAR")
  b = input ("¿Quieres contuniar?, Si(S) No(N): ")
  if b == "N":
     print("Terminamos. ")
     break
  if b == "S":
     print("continuamos: ")
  else:
     print("su respuesta no es valida")
  
     
  