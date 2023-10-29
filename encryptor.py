def debil(x):
    match x:
        case "decrypt":
            return("decrypt")
        case "encrypt":
            return("encrypt")
        case "getKey":
            return("getKey")
        case _:
            return("debile špatně")

while True:
    print((debil(input("vítej. co si přeješ udělat?\n"))))
    
    
    