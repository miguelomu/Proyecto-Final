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

    def platos(self):
        porciones_cereal = self.cereales_harinas // 110
        porciones_proteinas = self.proteinas // 80
        porciones_verduras = self.verduras // 70
        porciones_frutas = self.frutas // 110
        porciones_bebidas_nutritivas = self.bebidas_nutritivas // 225
        print(porciones_cereal, porciones_proteinas, porciones_verduras, porciones_frutas, porciones_bebidas_nutritivas)
        self.platos_comida = min(porciones_cereal, porciones_proteinas, porciones_verduras, porciones_frutas, porciones_bebidas_nutritivas)
        
        
class Beneficiarios(Comedores):
    def __init__(self, nombre = "",numCedula = 0, edad = 0, peso = 0, sexo = "", discapacidad = False, estrato = 0):
        self.nombre = nombre
        self.numCedula = numCedula
        self.edad = edad
        self.peso = peso
        self.sexo = sexo 
        self.discapacidad = discapacidad
        self.estrato = estrato
        
    def verificar_beneficiario(self, nuevo_beneficiario):
        #condiciones para agregar beneficiario
        #todos[res].agregar_nuevo_beneficiario(nuevo_beneficiario)
        pass   
  
class Todo(Alimentos, Beneficiarios):
    def __init__(self, comedores, alimentos):
        super().__init__(cereales_harinas = 0, proteinas = 0, verduras = 0, frutas = 0, bebidas_nutritivas = 0, platos_comida = 0)
        self.comedores = comedores
        self.alimentos = alimentos
        self.beneficiarios = []
        
    def repartir_alimentos (self, repartir_cereales_harinas, repartir_proteinas, repartir_verduras, repartir_frutas, repartir_bebidas_nutritivas):
        self.cereales_harinas -= repartir_cereales_harinas
        print(self.proteinas)
        self.proteinas -= repartir_proteinas
        print(self.proteinas)
        self.verduras -= repartir_verduras
        self.frutas -= repartir_frutas
        self.bebidas_nutritivas -= repartir_bebidas_nutritivas
        self.platos()    
        
    def agregar_nuevo_beneficiario(self, nuevo_beneficiario):
        self.beneficiarios.append(nuevo_beneficiario)
        
    def retirar_beneficiario (self, retirar_beneficiario):
        self.beneficiarios.remove(retirar_beneficiario)
        

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

beneficiarios1 = Beneficiarios()

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

print (todo6.comedores.direccion)
while True:
    num = 1
    print("\n-------------------------")
    print("EN CUAL COMEDOR DESEA TRABAJR")
    for comedor in comedores: 
        print(f"{num}. {comedor.nombre_comedor} - {comedor.direccion}")
        num += 1
    print (f"{num}. Slair del programa")
    print("-------------------------")
    res = int(input("Escriba el numero perteneciente al comedor: "))-1
    if res == num-1:
        print("\nSliendo...")
        break
    while True:
        num2 = 0
        if res + 1 <= num and res + 1 > 0:
            print("")
            print("\n-------------------------")
            print(f"OPCIONES COMEDOR COMUNITARIO ({comedores[res].nombre_comedor})")
            print("1. Inventario de Comida")
            print("2. Entrega de Comida")
            print("3. Repartir comida")    
            print("4. Beneficiarios inscritos")
            print("5. Añadir beneficiario")
            print("6. Retirar Beneficiario")
            print("7. Salir, escoger otro comedor")
            print("-------------------------")
            res2 = int(input("Escoja una opción: "))
            print("")
            
            if res2 == 1:
                print("-----------------")               
                print("COMIDA ACTUAL:")
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
                print("Al restaurante le acaba de llegar una carga de comida")
                
            elif res2 == 3:
                repartir_cereales_harinas = 110
                repartir_proteinas = 80
                repartir_verduras = 70
                repartir_frutas = 110
                repartir_bebidas_nutritivas = 225
                if len(todos[res].beneficiarios) > 0:
                    if len(todos[res].beneficiarios) <= todos[res].alimentos.platos_comida:
                        todos[res].repartir_alimentos(repartir_cereales_harinas, repartir_proteinas, repartir_verduras, repartir_frutas, repartir_bebidas_nutritivas)
                        print (f"Se acaban de entregar {todos[res].alimentos.platos_comida} platos de comida")
                    else:
                        print("En este comedor no tenemos suficiente comida para repartir a los beneficiarios")
                        print(f"Hacen falta {len(todos[res].beneficiarios) - (todos[res].alimentos.platos_comida)} platos de comida")               
                else:
                    print("Este comedor aun no tiene beneficiarios.")
                    
            elif res2 == 4:
                print("-----------------")
                print(f"Beneficiarios inscritos en el comedor {({comedores[res].nombre_comedor})}")
                if len(todos[res].beneficiarios) > 0:
                    for i in range (len(todos[res].beneficiarios)):
                        print(f"{i+1}. Nombre: {todos[res].beneficiarios[i].nombre}")
                        print(f"   Numero de identificacion: {todos[res].beneficiarios[i].numCedula}")
                        print("-----------------")
                        num2 = i + 1
                    bene = int(input("Digite el numero correspondiente al beneficiario a consultar: ")) - 1
                    if bene + 1 <= num2 and bene + 1  > 0:
                        print(f"Nombre: {todos[res].beneficiarios[bene].nombre}")
                        print(f"Numero de identificacion: {todos[res].beneficiarios[bene].numCedula}")
                        print(f"Edad: {todos[res].beneficiarios[bene].edad}")
                        print(f"Peso: {todos[res].beneficiarios[bene].peso}")
                        print(f"Sexo: {todos[res].beneficiarios[bene].sexo }")
                        print(f"Sufre discapacidad: {todos[res].beneficiarios[bene].discapacidad}")
                        print(f"Estrato: {todos[res].beneficiarios[bene].estrato}")
                        print("-----------------")    
                    else:
                        print("Error: Numero de beneficiario no válido, vuelva a internarlo...") 
                else:
                    print("Este comedor aun no tiene beneficiarios.")
                    
            elif res2 == 5:
                print ("Ingrese los siguietnes datos sobre el nuevo beneficiario")
                nombre_nuevo_beneficiario = input("Nombre: ").lower()
                numCedula_nuevo_beneficiario = input ("Numero de Cedula: ")
                edad_nuevo_beneficiario = int(input("Edad: "))
                peso_nuevo_beneficiario = input("Peso: ")
                sexo_nuevo_beneficiario = input("Sexo(M/F): ").lower()
                estrato_nuevo_beneficiario = input("Estrato: ")
                discapacidad_nuevo_beneficiario = input("Tiene alguna discapasidad(si/no): ").lower()
                if edad_nuevo_beneficiario >= 18:
                    fuente_ingreso = input("De cuanto es su fuente de ingerso mensualmente: ")
                    personas_a_cargo = input("Cuantas personas tiene a cargo: ")
                    vivienda = input("Vive cerca a este sector (si/no): ").lower()
                    if sexo_nuevo_beneficiario == "f":
                        embarazo = input("Está embarazada(si/no):").lower()
                nuevo_beneficiario = Beneficiarios(nombre_nuevo_beneficiario, numCedula_nuevo_beneficiario, edad_nuevo_beneficiario, peso_nuevo_beneficiario, sexo_nuevo_beneficiario, discapacidad_nuevo_beneficiario, estrato_nuevo_beneficiario)
                nuevo_beneficiario.verificar_beneficiario(nuevo_beneficiario)
                todos[res].agregar_nuevo_beneficiario(nuevo_beneficiario)
                print(f"Beneficiario insctiro con éxito")
                
            elif res2 == 6:
                print("-----------------")
                print(f"Beneficiarios inscritos en el comedor {({comedores[res].nombre_comedor})}")
                if len(todos[res].beneficiarios) > 0:
                    for i in range (len(todos[res].beneficiarios)):
                        print(f"{i+1}. Nombre: {todos[res].beneficiarios[i].nombre}")
                        print(f"   Numero de identificacion: {todos[res].beneficiarios[i].numCedula}")
                        print("-----------------")
                        num2 = i + 1
                    bene = int(input("Digite el numero correspondiente al beneficiario que desea retirar: ")) - 1
                    if bene + 1 <= num2 and bene + 1  > 0:
                        retirar_beneficiario = todos[res].beneficiarios[bene]
                        todos[res].retirar_beneficiario(retirar_beneficiario)
                        print(f"Beneficiario retirado con éxito")
                        print("-----------------")    
                    else:
                        print("Error: Numero de beneficiario no válido, vuelva a internarlo...") 
                else:
                    print("Este comedor aun no tiene beneficiarios.")
                
               
            elif res2 == 7:
                print("\nSaliendo...")
                break
            
            else:
                print("Opción no válida, intente nuevamente")
        else:
            print("Error: Ingrese un numero correspondiente a los comedores, vuelva a intentarlo...")
            break


