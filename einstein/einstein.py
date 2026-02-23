def main():
    mass = int(input("m: "))
    
    c = 300000000
    
    # E = mc^2

    energy = mass * (c ** 2)
    print(energy)

if __name__ == "__main__":
    main()