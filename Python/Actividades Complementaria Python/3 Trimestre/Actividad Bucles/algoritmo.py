
print("Muy buenas noches mis queridisimos invitados a la mejor fiesta de disfraces brindada por el mismisimo ChatGPT que es nuestro patrocinador oficial, pero como esto va a ser un evento tan grande y exclusivo primero necesitamos verificar que cumples con todos nuestro requisitos para el ingrese, no siendo mas Bienvenido a la GPTFest")

ingreso = input("¿Quieres verificar si cumples con los requisitos para entrar?: ")

while ingreso == "si": 
    edad = int(input("¿Cuantos años tienes?: "))
    if edad < 18:
        print("No puedes entrar... \nRazón: \nNo eres mayor de edad...")
        break
    else:
        altura = float(input("¿Cuanto mides? Ej: 1.72: "))
        if altura < 1.50:
            print(f"No puedes entrar... \nRazón: \nLa infraestructura de nuestras instalaciones no permite personas de {altura}")
            break
        else:
            mascara = input("¿Cuentas con una mascara en tu disfraz?: ")
            if mascara == "no":
                print("No puedes entrar... \nRazón: \nNo puedes ingresar  a la fiesta de mascaras sin mascaras xd")
                break
            else:
                senior = input("¿Eres un programador avanzado?(Senior): ")
                if senior == "no":
                    print("No puedes entrar... \nRazón: \nDebes ser senior como minimo para entrar a nuestra fiesta exclusiva")
                    break
                else:
                    regalo = input("¿Traes un regalo?: ")
                    if regalo == "no":
                        print("No puedes entrar... \nRazón: \nNo puedes entrar sin regalo")
                        break
                    else:
                        print("Excelente, cumples con todos los requisitos para ingresar a GPTFest, Disfruta de tu estadía en nuestras instalaciones y nunca dejes de aprender ")



