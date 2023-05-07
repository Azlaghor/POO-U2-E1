from classes import Email
# ============= FUNCTIONS ============= #
def validateEmail(email):
    vId, vDom, vType, vPass = email.split(",")
    if vId != "" and vDom != "" and vType != "" and vPass != "":
        validate = True
    else:
        validate = False

    return validate


# ============= MAIN ============= #
# Example
name = input("Ingrese su nombre: ")
email = Email(input("Ingrese ID de la cuenta: "),
        input("Ingrese Dominio: "),
        input("Ingrese Tipo de dominio: "),
        input("Ingrese contraseña: "))

print("Estimado ", name, " te enviaremos tus mensajes a la direccion ", email.returnEmail(), "\n")

# Moddify Password
currentPass = input("Ingrese la contraseña actual: ")
if currentPass == email.password:
    newPass = input("Ingrese la nueva contraseña: ")
    email.password = newPass
else:
    print("Contraseña incorrecta")

print("Contraseña nueva: ", email.password, "\n")

# Crear objeto Email a partir de una direccion de correo
addr = input("Ingrese nuevo email: ")
newEmail = Email("","","","")
newEmail.createAcc(addr)
print("Nuevo correo creado: ", newEmail.returnEmail())

# Leer Archivo, separar correos y crear cuentas
with open("email.txt", "r") as archive:
    # lines = archive.readlines()
    accList = []
    for line in archive:
        if validateEmail(line) == True:
            # Crear cuenta
            vId, vDom, vType, vPass = line.split(",")
            newAcc = Email("","","","")
            newAcc.idAcc = vId
            newAcc.domain = vDom
            newAcc.domType = vType
            newAcc.password = vPass
            accList.append(newAcc)
            print("Nueva cuenta creada: ", newAcc.returnEmail())

        else:
            # Error
            print("Correo no valido")
            # print(line)

print("Espero haber sido util. By Lucifer")