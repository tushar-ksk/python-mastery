def name(naam):
    match naam:
        case "Tushar":
            return "Self"
        case "Soham":
            return "Brother"
        case _:
            return "Unknown name"
        
print(name("Tushar"))
