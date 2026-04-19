import inflect

def main():
        p = inflect.engine()
        names = []

        while True:
            try:
                name = input("Name: ")
                names.append(name)
            except EOFError:
                 print()
                 break
        output_names = p.join(names)
    
        print(f"Adieu, adieu, to {output_names}")

main()
                 
                