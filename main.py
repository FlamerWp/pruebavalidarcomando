from datetime import datetime
import json

faltas = []
personas = []
bonos = []
ciclo = True
while ciclo:
    print("=====================================================")
    print ("\n1. Registro de empleados")
    print ("2. Registro  de inasistencia")
    print ("3. Registro de bonos extra-legales")
    print ("4. Calculo de nomina")
    print ("0. Salir del programa\n")
    ciclo = input("Ingrese la opcion que quiere escoger: \n")
    print("=====================================================")
    try:
        match ciclo:
            case "1":
                personas.clear()
                try:
                    with open("Json/datos.json", "r") as file:
                        datos = json.load(file)
                        personas.extend(datos)  # Usamos extend() para listas
                except FileNotFoundError:
                    personas.extend([])

                numeroIdentificacion = input("Ingrese el numero de identificacion: ")
                Nombre = input("Ingrese el nombre de la persona: ")
                Cargo = input("Ingrese el cargo de la persona: ")
                salario = int(input("Ingrese el salario de la persona: "))
                personas.append([numeroIdentificacion, Nombre, Cargo,salario])
                print ("Persona registrada exitosamente")
                with open("Json/datos.json", "w") as outfile:
                    json.dump(personas, outfile, indent=4)
            case "2":
                faltas.clear()
                
                try:
                    with open("Json/faltas.json", "r") as file:
                        datos = json.load(file)
                        faltas.extend(datos)  
                except FileNotFoundError:
                    faltas.extend([])
                numeroIdentificacion = input("Ingrese el numero de identificacion:  ")
                dia = input ("Ingrese el dia de la falta (1 al 31) ")
                mes = input ("Ingrese el mes de la falta (1 al 12)  ")
                fecha = (dia+"/"+mes+"/"+"2024")

                faltas.append ([numeroIdentificacion,fecha])
                print ("Falta registrada exitosamente ")
                with open("Json/faltas.json", "w") as outfile:
                    json.dump(faltas, outfile, indent=4)


            case "3":
                bonos.clear()
                
                try:
                    with open("Json/bonos.json", "r") as file:
                        datos = json.load(file)
                        bonos.extend(datos)  
                except FileNotFoundError:
                    bonos.extend([])
                print ("===============================================================")

                numeroIdentificacion = input("Ingrese el numero de identificacion: ")
                valorBono = int(input("Ingrese el valor del bono:"))
                concepto = input("Ingrese el concepto de bono: ")
                dia = input ("Ingrese el dia de la falta (1 al 31)")
                mes = input ("Ingrese el mes de la falta (1 al 12)")
                fecha = (dia+"/"+mes+"/"+"2024")

                bonos.append ([numeroIdentificacion,valorBono,concepto,fecha])
                print ("===============================================================")
                with open("Json/bonos.json", "w") as outfile:
                    json.dump(bonos, outfile, indent=4)

                print ("Bono registrado exitosamente")
            case "4":
                personas.clear()
                faltas.clear()
                bonos.clear()

                try:
                    with open("Json/datos.json", "r") as file:
                        datos = json.load(file)
                        personas.extend(datos)
                except FileNotFoundError:
                    personas.extend([])

                try:
                    with open("Json/faltas.json", "r") as file:
                        datos = json.load(file)
                        faltas.extend(datos)
                except FileNotFoundError:
                    faltas.extend([])

                try:
                    with open("Json/bonos.json", "r") as file:
                        datos = json.load(file)
                        bonos.extend(datos)
                except FileNotFoundError:
                    bonos.extend([])

                for persona in personas:
                    if persona[3] < 2000000:
                        datoT = ""
                        salario = persona[3] + (persona[3] * 0.02) # agregar bonificaciones, restar pensiones y salud
                        for bono in bonos:
                            if bono[0] == persona[0]:  # validar que el bono corresponda a la persona por cédula
                                salario += bono[1]
                                datoT += f"Cedula: {persona[0]}, Nombre: {persona[1]}, Cargo: {persona[2]}, Salario: {persona[3]}, Descuento de pension: {(persona[3] * 0.04)}, Descuento por salud: {(persona[3] * 0.04)}, Bono: {bono[1]}, Salario final: {salario}\n"
                        with open("reports/"+persona[1], "w") as file:
                            file.write(datoT)
                    else:
                        datoT = ""
                        salario = persona[3] - (persona[3] * 0.08)
                        for bono in bonos:
                            if bono[0] == persona[0]:
                                salario += bono[1]
                                datoT += f"Cedula: {persona[0]}, Nombre: {persona[1]}, Cargo: {persona[2]}, Salario: {persona[3]}, Descuento de pension: {int(persona[3] * 0.04)}, Descuento por salud: {int(persona[3] * 0.04)}, Bono: {bono[1]}, Salario final: {salario}\n"
                            else:
                                datoT += f"Cedula: {persona[0]}, Nombre: {persona[1]}, Cargo: {persona[2]}, Salario: {persona[3]}, Descuento de pension: {int(persona[3] * 0.04)}, Descuento por salud: {int(persona[3] * 0.04)}, Bono: {0}, Salario final: {salario}\n"

                        with open("reports/"+persona[1], "w") as file:
                            file.write(datoT)

            case "0":
                print("Ha salido del programa")
                ciclo = False
            case _:
                print("Ingrese una opción válida")
    except Exception as e:
        print("Ocurrió un error " + str(e))
