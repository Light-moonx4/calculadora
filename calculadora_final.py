opción=''

while opción!=10:
    print("1.rectángulo")
    print("2.triángulo")
    print("3.círculo")
    print("4.trapecio")
    print("5.cubo")
    print("6.esfera")
    print("7.cilindro")
    print("8.cono")
    print("9.triangulo rectangulo")
    print("10.salir")

    try:
        opción=int(input("digite un numero del 1 al 10 de que desea calcular,o si desea salir:"))
    except:
        print("error: ingrese un numero valido")
        opción=''

    #rectángulo
    if opción==1:
        print("1.Área")
        print("2.Perímetro")
        try:
            rectangulo=int(input("digite numero que desea calcular(1 Area o 2 Perimetro):"))
        except:
            print("error")
            rectangulo=0
        
        if rectangulo==1:
            try:
                base_rectangulo=float(input("digite la base o largo del rectangulo:"))
                altura_rectangulo=float(input("digite la altura rectangulo:"))
                Area= base_rectangulo*altura_rectangulo
                print("el Area del Rectángulo es:",Area)
            except:
                print("error en datos")

        elif rectangulo==2:
            try:
                base_rectangulo=float(input("digite la base o largo del rectangulo:"))
                altura_rectangulo=float(input("digite la altura del rectangulo:"))
                Perimetro= 2*(base_rectangulo+altura_rectangulo)
                print("el Perimetro del Rectángulo es:",Perimetro)
            except:
                print("error en datos")
        else:
            print("error debe elegir un el (1.area o 2.perimetro)")

    #triángulo
    elif opción==2:
        print("1.Área")
        print("2.Perímetro")
        try:
            triangulo=int(input("digite numero que desea calcular(1 Area o 2 Perimetro):"))
        except:
            triangulo=0

        if triangulo==1:
            try:
                base_triangulo=float(input("digite base o largo del triangulo:"))
                altura_triangulo=float(input("digite altura del triangulo:"))
                Area=(base_triangulo*altura_triangulo)/2
                print("el Area del triangulo es:",Area)
            except:
                print("error")

        elif triangulo==2:
            try:
                lado=float(input("digite la medida del lado triangulo:"))
                Perimetro=lado*3
                print("el Perimetro del triangulo es:",Perimetro)
            except:
                print("error")
        else:
            print("numero invalido")

    #círculo
    elif opción==3:
        print("1.Área")
        print("2.Perímetro")
        pi=3.1415
        try:
            circulo=int(input("número numérico que desea calcular(1 Área o 2 Perimetro):"))
        except:
            circulo=0

        if circulo==1:
            try:
                radio_circulo=float(input("digite la radio del circulo:"))
                if radio_circulo>0:
                    Area=pi*radio_circulo**2
                    print("el Area del circulo es:",Area)
                else:
                    print("error la radio no puede ser negativo")
            except:
                print("error")

        elif circulo==2:
            try:
                radio_circulo=float(input("digite la radio del circulo:"))
                if radio_circulo>0:
                    Perimetro = 2 * pi * radio_circulo
                    print("el Perimetro del circulo es:",Perimetro)
                else:
                    print("error la radio no puede ser negativo")
            except:
                print("error")
        else:
            print("numero invalido")

    #trapecio
    elif opción==4:
        print("1.Área")
        print("2.Perímetro")
        try:
            trapecio=int(input("digite numero que desea calcular(1 Area o 2 Perimetro):"))
        except:
            trapecio=0

        if trapecio==1:
            try:
                base_mayor=float(input("digite la base o largo mayor del trapecio:"))
                base_menor=float(input("digite la base o largo menor del trapecio:"))
                altura_trapecio=float(input("digite la altura del trapecio:"))
                if base_mayor>base_menor:
                    Area=((base_mayor+base_menor)*altura_trapecio)/2
                    print("el Area del trapecio es:",Area)
                else:
                    print("error")
            except:
                print("error")

        elif trapecio==2:
            try:
                base_mayor=float(input("digite la base o largo mayor del trapecio:"))
                base_menor=float(input("digite la base o largo menor del trapecio:"))
                lado_iz=float(input("digite el lado izquierdo del trapecio:"))
                lado_dr=float(input("digite el lado derecho del trapecio:"))
                if base_mayor>base_menor:
                    Perimetro=base_mayor+base_menor+lado_dr+lado_iz
                    print("el Perimetro del trapecio es:",Perimetro)
                else:
                    print("error")
            except:
                print("error")

    #cubo
    elif opción==5:
        print("1.Área")
        print("2.Volumen")
        try:
            cubo=int(input("digite numero que desea calcular(1 Area o 2 Volumen):"))
        except:
            cubo=0

        if cubo==1:
            try:
                lado_cubo=float(input("digite el valor del lado del cubo:"))
                Area_superficie =6*lado_cubo**2
                print("el Area o Area superficie del cubo es:",Area_superficie)
            except:
                print("error")

        elif cubo==2:
            try:
                lado_cubo=float(input("digite el valor del lado del cubo:"))
                volumen=lado_cubo**3
                print("el Volumen del cubo es:",volumen)
            except:
                print("error")

    #esfera
    elif opción==6:
        print("1.Área")
        print("2.Volumen")
        pi=3.1415
        try:
            esfera=int(input("digite numero que desea calcular(1 Area o 2 Volumen):"))
        except:
            esfera=0

        if esfera==1:
            try:
                radio_esfera=float(input("digite el valor del radio de la esfera:"))
                if radio_esfera>=0:
                    Area_superficie=4*pi*radio_esfera**2
                    print("el Area o Area superficie de la esfera es:",Area_superficie)
                else:
                    print("error")
            except:
                print("error")

        elif esfera==2:
            try:
                radio_esfera=float(input("digite el valor del radio de la esfera:"))
                if radio_esfera>=0:
                    volumen=(4/3)*pi*radio_esfera**3
                    print("el Volumen de la esfera es:",volumen)
                else:
                    print("error")
            except:
                print("error")

    #cilindro
    elif opción==7:
        print("1.Área")
        print("2.Volumen")
        pi=3.1415
        try:
            cilindro=int(input("digite numero que desea calcular(1 Area o 2 Volumen):"))
        except:
            cilindro=0

        if cilindro==1:
            try:
                radio_cilindro=float(input("digite el valor del radio del cilindro:"))
                altura_cilindro=float(input("digite la altura del cilindro:"))
                if radio_cilindro>0:
                    Area_superficie=2*pi*radio_cilindro*(radio_cilindro+altura_cilindro)
                    print("el Area o Area de superficie del cilindro es:",Area_superficie)
                else:
                    print("error")
            except:
                print("error")

        elif cilindro==2:
            try:
                radio_cilindro=float(input("digite el valor del radio del cilindro:"))
                altura_cilindro=float(input("digite la altura del cilindro:"))
                if radio_cilindro>0:
                    volumen=pi* radio_cilindro**2 *altura_cilindro
                    print("el Volumen del cilindro es:",volumen)
                else:
                    print("error")
            except:
                print("error")

    #cono
    elif opción==8:
        print("1.Área")
        print("2.Volumen")
        pi=3.1415
        try:
            cono=int(input("digite numero que desea calcular(1 Area o 2 Volumen):"))
        except:
            cono=0

        if cono==1:
            try:
                radio_cono=float(input("digite el valor del radio de el cono:"))
                generatriz_cono=float(input("digite el valor de la generatriz:"))
                if radio_cono>=0:
                    Area_superficie=pi*radio_cono*(radio_cono+generatriz_cono)
                    print("el Area o Area de la superficie del cono es:",Area_superficie)
                else:
                    print("error")
            except:
                print("error")

        elif cono==2:
            try:
                radio_cono=float(input("digite el valor del radio de el cono:"))
                altura_cono=float(input("digite el valor de la altura del cono:"))
                if radio_cono>=0:
                    volumen=(1/3)*pi* radio_cono**2 *altura_cono
                    print("el Volumen del cono es:",volumen)
                else:
                    print("error")
            except:
                print("error")

    #triángulo rectángulo
    elif opción==9:
        print("1.hipotenusa")
        print("2.cateto opuesto")
        print("3.cateto adyacente")
        print("4.ángulo")

        try:
            triangulo_rectangulo=int(input("digite el numero:"))
        except:
            triangulo_rectangulo=0

        if triangulo_rectangulo==1:
            try:
                cateto_op=float(input("digite el valor del cateto opuesto:"))
                cateto_ad=float(input("digite el valor del cateto adyacente:"))
                hipotenusa=(cateto_op**2 + cateto_ad**2) **0.5
                print("hipotenusa:",hipotenusa)
            except:
                print("error")

        elif triangulo_rectangulo==2:
            try:
                cateto_ad=float(input("adyacente:"))
                hipotenusa=float(input("hipotenusa:"))
                if hipotenusa>cateto_ad:
                    opuesto=(hipotenusa**2 -cateto_ad**2)**0.5
                    print("opuesto:",opuesto)
                else:
                    print("error")
            except:
                print("error")

        elif triangulo_rectangulo==3:
            try:
                cateto_op=float(input("opuesto:"))
                hipotenusa=float(input("hipotenusa:"))
                if hipotenusa>cateto_op:
                    adyacente=(hipotenusa**2 - cateto_op**2) ** 0.5
                    print("adyacente:",adyacente)
                else:
                    print("error")
            except:
                print("error")

        elif triangulo_rectangulo==4:
            try:
                angulo=float(input("digite el valor del angulo:"))
                if angulo<=90:
                    angulo_faltante=90-angulo
                    print("angulo faltante:",angulo_faltante)
            except:
                print("error")

    elif opción==10:
        print("calculadora finalizada gracias por usar nuestra calculadora")