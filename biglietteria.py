eta=int(input("Quanti anni hai?"))
biglietto=input("Hai il biglietto?")
if biglietto=="Si":
  print("Puoi entrare")
elif eta>=18:
 print("12€")
elif eta<18:
  print("8€")
