opcion=''
while opcion!='10':
    print("1.rectangulo")
    print("2.triangulo")
    print("3.circulo")
    print("4.pentágono")
    print("5.cubo")
    print("6.esfera")
    print("7.cilindro")
    print("8.cono")
    print("9.tiangulo rectangulo")
    print("10.salir")
    #digita un numero entero del 1 al 10
    opcion=int(input("digite que desea calcular,o si desea salir:"))

    if opcion==1:
        print("1.Area")
        print("2.Perimetro")
        rectangulo=input(input("digite que desea calcular(Area,Perimetro):"))
        
        if rectangulo==1:
            #puede numeros digitar decimales y enteros
            base_rectangulo=float(input("digite la base o largo  del rectangulo:"))
            altura_rectangulo=float(input("digite la altura rectangulo:"))
            Area= base_rectangulo*altura_rectangulo
            print("el Area del Rectangulo es:",Area)
        elif rectangulo==2:
            #puede numeros digitar decimales y enteros
            base_rectangulo=int(input("digite la base o largo del rectangulo:"))
            altura_rectangulo=int(input("digite la altura del rectangulo:"))
            Perimetro= 2*(base_rectangulo+altura_rectangulo)
            print("el Perimetro del Rectangulo es",Perimetro)
        else:
            ("error debe elegir un el (1.area o 2.perimetro)")

    elif opcion==2:
        print("1.Area")
        print("2.Perimetro")
        triangulo=int(input("digite que desea calcular(Area o Perimetro):"))

        if triangulo==1:
            #puede numeros digitar decimales y enteros
           base_triangulo=float(input("digite base o largo del triangulo:"))
           altura_triangulo=float(input("digite altura del triangulo:"))
           Area=(base_triangulo*altura_triangulo)/2
           print("el Area del triangulo es:",Area)
            #puede numeros digitar decimales y enteros
        elif triangulo==2:
            lado=float(input("digite la medida del lado triangulo"))
            Perimetro=lado*3
            print("el Perimetro del triangulo es:",Perimetro)
        else:
            ("numero invalido o no digito numero")
    elif opcion==3:
        print("1.Area")
        print("2.Perimetro")
        circulo=int(input("digite que desea calcular(Area o Perimetro)"))
        pi=3.1415

        if circulo==1:
            #puede numeros digitar decimales y enteros
            radio_circulo=float("digite el radio del circulo:")
            Area=pi*radio_circulo**2
            print("el Area del circulo es:",Area)
        elif circulo==2:
            radio_circulo=float("digite el radio del circulo:")
            Perimetro=2*pi*radio_circulo
            print("el Perimetro del circculo es:",Perimetro)
        else:
            ("numero invalido o no digito numero")
    