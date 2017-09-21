agenda = {
    "Igor": {
        "telefone": ["555-5555", "7777-7777"],
        "e-mail" : "igor@email.com"

    },
    "Jorge" : "8888-8888",
    "Luciana" : ["9999-9999"]
}

print(agenda)
agenda["Igor"]["e-mail"] = input("Digite o e-mail: ")
print()
print(agenda)