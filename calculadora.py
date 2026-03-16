opcion=''
while opcion!=10:
    print("1.rectangulo")
    print("2.triangulo")
    print("3.circulo")
    print("4.trapecio")
    print("5.cubo")
    print("6.esfera")
    print("7.cilindro")
    print("8.cono")
    print("9.triangulo rectangulo")
    print("10.salir")
    #digita un numero entero del 1 al 10
    opcion=int(input("digite un numero del 1 al 10 de que desea calcular,o si desea salir:"))

    if opcion==1:
        print("1.Area")
        print("2.Perimetro")
        rectangulo=int(input("digite numero que desea calcular(1 Area o  2 Perimetro):"))
        
        if rectangulo==1:
            #puede numeros digitar decimales y enteros
            base_rectangulo=float(input("digite la base o largo  del rectangulo:"))
            altura_rectangulo=float(input("digite la altura rectangulo:"))
            Area= base_rectangulo*altura_rectangulo
            print("el Area del Rectangulo es:",Area)
        elif rectangulo==2:
            #puede numeros digitar decimales y enteros
            base_rectangulo=float(input("digite la base o largo del rectangulo:"))
            altura_rectangulo=float(input("digite la altura del rectangulo:"))
            Perimetro= 2*(base_rectangulo+altura_rectangulo)
            print("el Perimetro del Rectangulo es:",Perimetro)
        else:
            print("error debe elegir un el (1.area o 2.perimetro)")

    elif opcion==2:
        print("1.Area")
        print("2.Perimetro")
        triangulo=int(input("digite numero que desea calcular(1 Area o  2 Perimetro):"))

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
            print("numero invalido o no digito numero")
    elif opcion==3:
        print("1.Area")
        print("2.Perimetro")
        circulo=int(input("digite numero que desea calcular(1 Area o  2 Perimetro):"))
        pi=3.1415

        if circulo==1:
            #puede numeros digitar decimales y enteros
            radio_circulo=float(input("digite el radio del circulo:"))
            Area=pi*radio_circulo**2
            print("el Area del circulo es:",Area)
        elif circulo==2:
            radio_circulo=float(input("digite el radio del circulo:"))
            Perimetro=2*pi*radio_circulo
            print("el Perimetro del circulo es:",Perimetro)
        else:
            print("numero invalido o no digito numero")
    elif opcion==4:
        #puede numeros digitar enteros
        print("1.Area")
        print("2.Perimetro")
        trapecio=int(input("digite numero que desea calcular(1 Area o  2 Perimetro):"))

        if trapecio==1:
            #puede numeros digitar decimales y enteros
            base_mayor=float(input("digite la base o largo mayor del trapecio:"))
            base_menor=float(input("digite la base o largo menor del trapecio:"))
            altura_trapecio=float(input("digite la altura del trapecio"))
            if base_mayor>base_menor:
                Area=((base_mayor+base_menor)*altura_trapecio)/2
                print("el Area del trapecio es:",Area)
            else:
                print("error la base mayor debe ser un numero superior a la base menor")
        elif trapecio==2:
            #puede numeros digitar decimales y enteros
            base_mayor=float(input("digite la base o largo mayor del trapecio:"))
            base_menor=float(input("digite la base o largo menor del trapecio:"))
            lado_iz=float(input("digite el lado izquierdo del trapecio:"))
            lado_dr=float(input("digite el lado derecho del trapecio:"))
            if base_mayor>base_menor:
                Perimetro=base_mayor+base_menor+lado_dr+lado_iz
                print("el Perimetro del trapecio es:",Perimetro)
            else:
                print("error la base mayor debe ser un numero superior a la base menor")
        else:
            print("numero invalido o no digito numero")   
    elif opcion==5:
        print("1.Area")
        print("2.Volumen")
        cubo=int(input("digite numero que desea calcular(1 Area o  2 Volumen):"))

        if cubo==1:
            #puede numeros digitar decimales y enteros
            lado_cubo=float(input("digite el valor del lado del cubo:"))
            Area_superficie =6*lado_cubo**2
            print("el Area o Area superficie del cubo es:",Area_superficie)
        elif cubo==2:
            #puede numeros digitar decimales y enteros
            lado_cubo=float(input("digite el valor del lado del cubo:"))
            volumen=lado_cubo**3
            print("el Volumen del cubo es:",volumen)
        else:
            print("numero invalido o no digito numero")    
    elif opcion==6:
        print("1.Area")
        print("2.Volumen")
        esfera=int(input("digite numero que desea calcular(1 Area o  2 Volumen):"))
        pi=3.1415

        if esfera==1:
            #puede numeros digitar decimales y enteros
            radio_esfera=float(input("digite el valor del radio de la esfera:"))
            Area_superficie=4*pi*radio_esfera**2
            print("el Area o Area superficie de la esfera es:",Area_superficie)
        elif esfera==2:
            #puede numeros digitar decimales y enteros
            radio_esfera=float(input("digite el valor del radio de la esfera:"))
            volumen=(4/3)*pi*radio_esfera**3
            print("el Volumen de la esfera es:",volumen)
        else:
            print("numero invalido o no digito numero")
    elif opcion==7:
        print("1.Area")
        print("2.Volumen")
        cilindro=int(input("digite numero que desea calcular(1 Area o  2 Volumen):"))
        pi=3.1415

        if cilindro==1:
            #puede numeros digitar decimales y enteros
            radio_cilindro=float(input("digite el valor del radio del cilindro:"))
            altura_cilindro=float(input("digite la altura del cilindro"))
            Area_superficie=2*pi*radio_cilindro*(radio_cilindro+altura_cilindro)
            print("el Area o Area de superficie del cilindro es:",Area_superficie)
        elif cilindro==2:
            #puede numeros digitar decimales y enteros
            radio_cilindro=float(input("digite el valor del radio del cilindro:"))
            altura_cilindro=float(input("digite la altura del cilindro"))
            volumen=pi* radio_cilindro**2 *altura_cilindro
            print("el Volumen del cilindro es:",volumen)
        else:
            print("numero invalido o no digito numero")
    elif opcion==8:
        print("1.Area")
        print("2.Volumen")
        cono=int(input("digite numero que desea calcular(1 Area o  2 Volumen):"))
        pi=3.1415

        if cono==1:
            #puede numeros digitar decimales y enteros
            radio_cono=float(input("digite el valor del radio de el cono:"))
            #genratriz es la linea inclinada desde la punta hasta el borde de la base
            generatriz_cono=float(input("digite el valor de la generatriz:"))
            Area_superficie=pi*radio_cono*(radio_cono+generatriz_cono)
            print("el Area o Area de la superficie del cono es:",Area_superficie)
        elif cono==2:
            #puede numeros digitar decimales y enteros
            radio_cono=float(input("digite el valor del radio de el cono:"))
            altura_cono=float(input("digite el valor de la altura del cono:"))  
            volumen=(1/3)*pi* radio_cono**2 *altura_cono
            print("el Volumen del cono es:",volumen)
        else:
            print("numero invalido o no digito numero")      
    elif opcion==9:
        print("1.hipotenusa")
        print("2.cateto opuesto")
        print("3.cateto adyacente")
        triangulo_rectangulo=int(input("digite el numero de lo que desea calcular(1 hipotenusa ,2 cateto opuesto,3 cateto adyacente):"))

        if triangulo_rectangulo==1:
            #puede numeros digitar decimales y enteros
            #se calcula con el teorema de pitagora
            cateto_op=float(input("digite el valor del cateto opuesto del triangulo rectangulo:"))
            cateto_ad=float(input("digite el valor del cateto adyacente del triangulo rectangulo:"))
            hipotenusa=(cateto_op**2 + cateto_ad**2) **0.5
            print("el valor de la hipotenusa del triangulo es:",hipotenusa)
        elif triangulo_rectangulo==2:
            #puede numeros digitar decimales y enteros
            #se calcula con formula de la tangente
            cateto_ad=float(input("digite el valor del cateto adyacente del triangulo rectangulo:"))
            tangente=float(input("digite el valor de la tangente:"))
            opuesto=tangente*cateto_ad
            print("el valor del cateto opuesto del triangulo rectangulo es:",opuesto)
        elif triangulo_rectangulo==3:
            #puede numeros digitar decimales y enteros
            #se calcula con el teorema de pitagora
            cateto_op=float(input("digite el valor del cateto opuesto del triangulo rectangulo:"))
            hipotenusa=float(input("digite el valor de la hipotenusa:"))
            adyacente=(hipotenusa**2 - cateto_op**2) ** 0.5
            print("el valor del cateto adyacente del triangulo rectangulo es:",adyacente)
        else:
            print("numero invalido o no digito un numero")
    elif opcion==10:
        print("calculadora finalizada gracias por usar nuestra calculadora")