volar=(input("¿puede volar?:   "))
humano=(input("¿es humano?:   "))
mascara=(input("¿tiene mascara:  "))

if volar=="si" and humano=="si" and mascara=="si":
    print("Iromman")
elif volar=="si" and humano=="si" and mascara=="no":
    print("captain marvel")
elif volar=="si" and humano=="no" and mascara=="si":
        print("Roman accuser")
elif volar=="si" and humano=="si" and mascara=="no": 
         print("Vision")
elif volar=="no" and humano=="si" and mascara=="si":
         print("Spiderman")
elif volar=="no" and humano=="si" and mascara=="no":
  print("Hulk")
elif volar=="no" and humano=="no" and mascara=="si":
     print("Black Bolt")
elif volar=="no" and humano=="no" and mascara=="no":
   print("Thanos")