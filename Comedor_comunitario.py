class Comedores():
    def __init__(self, nombre_comedor = "", direccion = "", capacidad = 0, horaio = ""):
        self.nombre_comedor = nombre_comedor
        self. direccion = direccion
        self.capacidad = capacidad
        self.horaio = horaio

        
                       
class Alimentos(Comedores):
    def __init__(self, cereales_harinas = 0, proteinas = 0, verduras = 0, frutas = 0, bebidas_nutritivas = 0, platos_comida = 0):
        self.cereales_harinas = cereales_harinas
        self.proteinas = proteinas
        self.verduras = verduras
        self.frutas = frutas
        self.bebidas_nutritivas = bebidas_nutritivas
        self.platos_comida = platos_comida
        
    def entrega_alimentos (self, entrega_cereales_harinas, entrega_proteinas, entrega_verduras, entrega_frutas, entrega_bebidas_nutritivas):
        self.cereales_harinas += entrega_cereales_harinas
        self.proteinas += entrega_proteinas
        self.verduras += entrega_verduras
        self.frutas += entrega_frutas
        self.bebidas_nutritivas += entrega_bebidas_nutritivas 
        self.platos()
             
    def repartir_alimentos (self, repartir_cereales_harinas, repartir_proteinas, repartir_verduras, repartir_frutas, repartir_bebidas_nutritivas):
        self.cereales_harinas -= repartir_cereales_harinas
        self.proteinas -= repartir_proteinas
        self.verduras -= repartir_verduras
        self.frutas -= repartir_frutas
        self.bebidas_nutritivas -= repartir_bebidas_nutritivas
        self.platos()  

    def platos(self):
        porciones_cereal = self.cereales_harinas // 110
        porciones_proteinas = self.proteinas // 80
        porciones_verduras = self.verduras // 70
        porciones_frutas = self.frutas // 110
        porciones_bebidas_nutritivas = self.bebidas_nutritivas // 225
        self.platos_comida = min(porciones_cereal, porciones_proteinas, porciones_verduras, porciones_frutas, porciones_bebidas_nutritivas)
        
        
class Beneficiarios(Comedores):
    def __init__(self, nombre = "",numCedula = 0, edad = 0, sexo = "",estrato = 0 , discapacidad = False, puntaje_vulnerabilidad = 0):
        self.nombre = nombre
        self.numCedula = numCedula
        self.edad = edad
        self.sexo = sexo 
        self.estrato = estrato        
        self.discapacidad = discapacidad
        self.puntaje_vulnerabilidad = puntaje_vulnerabilidad
        
    def verificar_beneficiario(self, nuevo_beneficiario, salir = True, salir2 = True, salir3 = True):
        if edad_nuevo_beneficiario >= 18:
            print("\nLlene los siguientes datos para determinar si el beneficiario es apto o no")
            print("-------------------------")
        else:
            print("\nEn caso de ser menor de edad, debe llenar los siguientes datos de su representante legal")
            print("-------------------------")
                    
        while salir:
            comida_diaria = leer_entero("Cuantas veces al dia come: ",1 , 3)
            sueldo_mensual = leer_entero("Ingrese su sueldo mensual: ", 0, 9999999999999)
            personas_a_cargo = leer_entero("Cuantas personas dependen de usted económicamente: ", 0, 9999999999)
            self.discapacidad = input("Tiene alguna discapasidad(si/no): ").lower()
            vivienda = input("Tipo de vivienda (propia/arriendo/calle): ").lower()           
            if personas_a_cargo > 0:
                ingereso_por_persona = sueldo_mensual / personas_a_cargo
            else:
                ingereso_por_persona = sueldo_mensual
                
            while salir2:
                if comida_diaria == 1:
                    self.puntaje_vulnerabilidad += 5
                elif comida_diaria == 2:
                    self.puntaje_vulnerabilidad += 3
                elif comida_diaria == 3:
                    self.puntaje_vulnerabilidad += 0
                else:
                    print("Error: Numero de comidas al dia no valido, vuelva a intentarlo...")
                    print("-----------------")
                    break
                
                if ingereso_por_persona < 200000:
                    self.puntaje_vulnerabilidad += 5
                elif ingereso_por_persona > 300000:
                    self.puntaje_vulnerabilidad += 0
                else:
                    self.puntaje_vulnerabilidad += 3
                    
                if self.discapacidad == "si":
                    self.puntaje_vulnerabilidad += 5
                elif self.discapacidad == "no":
                    self.puntaje_vulnerabilidad += 0
                else:
                    print("Error: Respuesta de discapacidad no valida, vuelva a intentarlo...")
                    print("-----------------")
                    break
                    
                if vivienda == "propia":
                    self.puntaje_vulnerabilidad += 0
                elif vivienda == "arriendo":
                    self.puntaje_vulnerabilidad += 3
                elif vivienda == "calle":
                    self.puntaje_vulnerabilidad += 5
                else:
                    print("Error: Tipo de vivienda no valido, vuelva a intentarlo...")
                    print("-----------------")
                    break
                
                if self.puntaje_vulnerabilidad < 10:
                    print(f"El beneficiario {nuevo_beneficiario.nombre} NO es apto para recibir comida en este comedor comunitario")
                    salir = False
                    break
                
                elif self.puntaje_vulnerabilidad >= 15:
                    print(f"El beneficiario {nuevo_beneficiario.nombre} es apto para recibir comida en este comedor comunitario")
                    salir = False
                    break                    
                else:
                    print("Es necesario hacer una verificación adicional para determinar si el beneficiario es apto o no")
                    print("-----------------")                       
                    while salir3:
                        desplazamiento = input("El beneficiario ha sufrido de desplazamiento(si/no): ").lower()
                        if desplazamiento == "si":
                            self.puntaje_vulnerabilidad += 5
                            salir = False
                            salir2 = False
                            break
                        elif desplazamiento == "no":
                            self.puntaje_vulnerabilidad += 0
                            
                            menores_a_cargo = input("Tiene menores de 5 años a su cargo(si/no): ")
                            if menores_a_cargo == "si":
                                self.puntaje_vulnerabilidad += 5
                                salir = False
                                salir2 = False
                                break
                            elif menores_a_cargo == "no":
                                self.puntaje_vulnerabilidad += 0
                                salir = False
                                salir2 = False
                                break
                            else:
                                print("Error: Mala respuesta, vuelva a intentarlo...")  
                                print("-----------------") 
                        else:
                            print("Error: Mala respuesta, vuelva a intentarlo...")
                            print("-----------------")
                            
        if self.puntaje_vulnerabilidad >= 15:
            todos[res].agregar_nuevo_beneficiario(nuevo_beneficiario)
            print(f"Beneficiario insctiro con éxito")
        else:
            print(f"Beneficiario {nuevo_beneficiario.nombre} no apto para este comedor comunitario")

  
class Todo(Alimentos, Beneficiarios):
    def __init__(self, comedores, alimentos):
        self.comedores = comedores
        self.alimentos = alimentos
        self.beneficiarios = []
          
    def agregar_nuevo_beneficiario(self, nuevo_beneficiario):
        self.beneficiarios.append(nuevo_beneficiario)
        
    def retirar_beneficiario (self, retirar_beneficiario):
        self.beneficiarios.remove(retirar_beneficiario)
        
def leer_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                print(f"\nPor favor, ingrese un número entre {minimo} y {maximo}.")
            else:
                return valor
        except ValueError:
            print("\nEntrada no válida. Por favor, ingrese un número entero.")


comedor1 = Comedores("Los luceros","Cra 17F No. 69A-32 Sur (Lucero Sur)" , 250, "Lun a sáb, 10:30 a.m. - 3:00 p.m.")
comedor2 = Comedores("Potosí","Calle 81 Sur No. 42-09" , 230, "Lun a sáb, 11:00 a.m. - 2:30 p.m.")
comedor3 = Comedores("Caracolí","Calle 76A Sur No. 74B-05" , 220, "Lun a sáb, 11:00 a.m. - 2:30 p.m.")
comedor4 = Comedores("La Estrella","Cra 18 No. 74A Sur-87" , 240, "Lun a sáb, 10:30 a.m. - 3:00 p.m.")
comedor5 = Comedores("Bella Flor - La Torre","Cra 27 No. 75A-50 Sur" , 230, "Lun a sáb, 11:00 a.m. - 2:30 p.m.")
comedor6 = Comedores("Altos de la Cruz","Transv 22 No. 69K-19 Sur" , 225, "Lun a sáb, 11:00 a.m. - 2:30 p.m.")
comedor7 = Comedores("Juan Pablo II","Diag 68B Sur No. 18P-40" , 220, "Lun a sáb, 10:30 a.m. - 3:00 p.m.")
comedor8 = Comedores("Naciones Unidas","Cra 18R No. 77A Sur-27" , 235, "Lun a sáb, 10:30 a.m. - 3:00 p.m.")
comedor9 = Comedores("Jerusalén Canteras","Cra 47D No. 68G-08 Sur" , 250, "Lun a sáb, 11:00 a.m. - 2:30 p.m.")
comedor10 = Comedores("Estrella del Sur","Calle 74 No. 18 Bis-18" , 230, "Lun a sáb, 10:30 a.m. - 3:00 p.m.")
comedor11 = Comedores("Santa Viviana","Calle 75D Sur No. 75C-03 Sur" , 220, "Lun a sáb, 11:00 a.m. - 2:30 p.m.")
comedor12 = Comedores("Arborizadora","Cra 40 No. 63I-25 Sur" , 230, "Lun a sáb, 11:00 a.m. - 2:30 p.m.")
comedor13 = Comedores("Perdomo","Av. Villavicencio No. 60B-05 Sur" , 240, "Lun a sáb, 10:30 a.m. - 3:00 p.m.")
comedor14 = Comedores("El Tesoro","Cra 18F No. 76 Sur" , 225, "Lun a sáb, 11:00 a.m. - 2:30 p.m.")
comedor15 = Comedores("Vista Hermosa"," Calle 80B Sur No. 44-10" , 230, "Lun a sáb, 10:30 a.m. - 3:00 p.m.")

alimentos1 = Alimentos(0, 0, 0, 0, 0, 0)
alimentos2 = Alimentos(0, 0, 0, 0, 0, 0)
alimentos3 = Alimentos(0, 0, 0, 0, 0, 0)
alimentos4 = Alimentos(0, 0, 0, 0, 0, 0)
alimentos5 = Alimentos(0, 0, 0, 0, 0, 0)
alimentos6 = Alimentos(0, 0, 0, 0, 0, 0)
alimentos7 = Alimentos(0, 0, 0, 0, 0, 0)
alimentos8 = Alimentos(0, 0, 0, 0, 0, 0)
alimentos9 = Alimentos(0, 0, 0, 0, 0, 0)
alimentos10 = Alimentos(0, 0, 0, 0, 0, 0)
alimentos11 = Alimentos(0, 0, 0, 0, 0, 0)
alimentos12 = Alimentos(0, 0, 0, 0, 0, 0)
alimentos13 = Alimentos(0, 0, 0, 0, 0, 0)
alimentos14 = Alimentos(0, 0, 0, 0, 0, 0)
alimentos15 = Alimentos(0, 0, 0, 0, 0, 0)

comedores = [comedor1, comedor2, comedor3, comedor4, comedor5, comedor6, comedor7, comedor8, comedor9, comedor10, comedor11, comedor12, comedor13, comedor14, comedor15]
alimentos = [alimentos1, alimentos2, alimentos3, alimentos4, alimentos5, alimentos6, alimentos7, alimentos8, alimentos9, alimentos10, alimentos11, alimentos12, alimentos13, alimentos14, alimentos15]

todo1 = Todo(comedor1, alimentos1)
todo2 = Todo(comedor2, alimentos2)
todo3 = Todo(comedor3, alimentos3)
todo4 = Todo(comedor4, alimentos4)
todo5 = Todo(comedor5, alimentos5)
todo6 = Todo(comedor6, alimentos6)
todo7 = Todo(comedor7, alimentos7)
todo8 = Todo(comedor8, alimentos8)
todo9 = Todo(comedor9, alimentos9)
todo10 = Todo(comedor10, alimentos10)
todo11 = Todo(comedor11, alimentos11)
todo12 = Todo(comedor12, alimentos12)
todo13 = Todo(comedor13, alimentos13)
todo14 = Todo(comedor14, alimentos14)
todo15 = Todo(comedor15, alimentos15)

todos = [todo1, todo2, todo3, todo4, todo5, todo6, todo7, todo8, todo9, todo10, todo11, todo12, todo13, todo14, todo15]

while True:
    num = 1  
    print("\nEN CUAL COMEDOR DESEA TRABAJR")
    print("-------------------------")
    for comedor in comedores: 
        print(f"{num}. {comedor.nombre_comedor} - {comedor.direccion}")
        num += 1
    print (f"{num}. Slair del programa")
    print("-------------------------")
    res = leer_entero("Escriba el numero perteneciente al comedor: ", 1, 16)-1
    if res == num-1:
        print("\nSliendo...")
        break
    while True:
        num2 = 0
        if res + 1 <= num and res + 1 > 0:
            print(f"\nOPCIONES COMEDOR COMUNITARIO ({comedores[res].nombre_comedor})")
            print("-------------------------") 
            print("1. Inventario de Comida")
            print("2. Entrega de Comida")
            print("3. Repartir comida")    
            print("4. Beneficiarios inscritos")
            print("5. Añadir beneficiario")
            print("6. Retirar Beneficiario")
            print("7. Salir, escoger otro comedor")
            print("-------------------------")
            res2 = leer_entero("Escoja una opción: ",1, 7)
            
            if res2 == 1:
                print("\nCOMIDA ACTUAL:")               
                print("-----------------")
                print(f"{todos[res].alimentos.cereales_harinas}g en cereales y harinas")
                print(f"{todos[res].alimentos.proteinas}g en proteinas")
                print(f"{todos[res].alimentos.verduras}g en verduras")
                print(f"{todos[res].alimentos.frutas}g en frutas")
                print(f"{todos[res].alimentos.bebidas_nutritivas}g en bebidas nutritivas")
                print(f"este comedor cuenta con {todos[res].alimentos.platos_comida} platos de comida disponibles")
                print("-----------------")
                
            elif res2 == 2:
                entrega_cereales_harinas = 552
                entrega_proteinas = 558
                entrega_verduras = 765
                entrega_frutas = 240
                entrega_bebidas_nutritivas = 865
                todos[res].alimentos.entrega_alimentos(entrega_cereales_harinas, entrega_proteinas, entrega_verduras, entrega_frutas, entrega_bebidas_nutritivas)
                #print (todos[res].alimentos.proteinas)
                print("-----------------")   
                print("Al restaurante le acaba de llegar una carga de comida")
                
            elif res2 == 3:
                repartir_cereales_harinas = 110 * len(todos[res].beneficiarios)
                repartir_proteinas = 80 * len(todos[res].beneficiarios)
                repartir_verduras = 70 * len(todos[res].beneficiarios)
                repartir_frutas = 110 * len(todos[res].beneficiarios)
                repartir_bebidas_nutritivas = 225 * len(todos[res].beneficiarios)
                if len(todos[res].beneficiarios) > 0:
                    if len(todos[res].beneficiarios) <= todos[res].alimentos.platos_comida:
                        todos[res].alimentos.repartir_alimentos(repartir_cereales_harinas, repartir_proteinas, repartir_verduras, repartir_frutas, repartir_bebidas_nutritivas)
                        print("-----------------")   
                        print (f"Se acaban de entregar {len(todos[res].beneficiarios)} platos de comida")
                    else:
                        print("-----------------")   
                        print("En este comedor no tenemos suficiente comida para repartir a los beneficiarios")
                        print(f"Hacen falta {len(todos[res].beneficiarios) - (todos[res].alimentos.platos_comida)} platos de comida")               
                else:
                    print("-----------------")   
                    print("Este comedor aun no tiene beneficiarios.")
                    
            elif res2 == 4:
                print(f"\nBeneficiarios inscritos en el comedor {({comedores[res].nombre_comedor})}")
                print("-----------------")
                if len(todos[res].beneficiarios) > 0:
                    for i in range (len(todos[res].beneficiarios)):
                        print(f"{i+1}. Nombre: {todos[res].beneficiarios[i].nombre}")
                        print(f"   Numero de identificacion: {todos[res].beneficiarios[i].numCedula}")
                        print("-----------------")
                        num2 = i + 1
                    bene = leer_entero("Digite el numero correspondiente al beneficiario a consultar: ",0, 99999999) - 1
                    if bene + 1 <= num2 and bene + 1  > 0:
                        print("-----------------")   
                        print(f"Nombre: {todos[res].beneficiarios[bene].nombre}")
                        print(f"Numero de identificacion: {todos[res].beneficiarios[bene].numCedula}")
                        print(f"Edad: {todos[res].beneficiarios[bene].edad}")
                        print(f"Sexo: {todos[res].beneficiarios[bene].sexo }")
                        print(f"Sufre discapacidad: {todos[res].beneficiarios[bene].discapacidad}")
                        print(f"Estrato: {todos[res].beneficiarios[bene].estrato}")
                        print("-----------------")    
                    else:
                        print("Error: Numero de beneficiario no válido, vuelva a internarlo...") 
                else:
                    print("Este comedor aun no tiene beneficiarios.")
                    
            elif res2 == 5:
                print ("\nIngrese los siguietnes datos sobre el nuevo beneficiario")
                print("-----------------")   
                nombre_nuevo_beneficiario = input("Nombre: ").lower()
                numCedula_nuevo_beneficiario = input ("Numero de Cedula: ")
                edad_nuevo_beneficiario = leer_entero("Edad: ", 0, 150)
                sexo_nuevo_beneficiario = input("Sexo(M/F): ").lower()
                estrato_nuevo_beneficiario = input("Estrato: ")
                nuevo_beneficiario = Beneficiarios(nombre_nuevo_beneficiario, numCedula_nuevo_beneficiario, edad_nuevo_beneficiario, sexo_nuevo_beneficiario, estrato_nuevo_beneficiario,"", 0)
                nuevo_beneficiario.verificar_beneficiario(nuevo_beneficiario)
                print("-----------------")   
                
            elif res2 == 6:
                print(f"\nBeneficiarios inscritos en el comedor {({comedores[res].nombre_comedor})}")
                print("-----------------")
                if len(todos[res].beneficiarios) > 0:
                    for i in range (len(todos[res].beneficiarios)):
                        print(f"{i+1}. Nombre: {todos[res].beneficiarios[i].nombre}")
                        print(f"   Numero de identificacion: {todos[res].beneficiarios[i].numCedula}")
                        print("-----------------")
                        num2 = i + 1
                    bene = leer_entero("Digite el numero correspondiente al beneficiario que desea retirar: ", 1, 99999) - 1
                    if bene + 1 <= num2 and bene + 1  > 0:
                        retirar_beneficiario = todos[res].beneficiarios[bene]
                        todos[res].retirar_beneficiario(retirar_beneficiario)
                        print("-----------------")
                        print(f"Beneficiario retirado con éxito")    
                    else:
                        print("Error: Numero de beneficiario no válido, vuelva a internarlo...") 
                else:
                    print("Este comedor aun no tiene beneficiarios.")
                     
            elif res2 == 7:
                print("\n-----------------")   
                print("Saliendo...")
                break
            
            else:
                print("\n-----------------")   
                print("Opción no válida, intente nuevamente")
        else:
            print("\n-----------------")   
            print("Error: Ingrese un numero correspondiente a los comedores, vuelva a intentarlo...")
            break


