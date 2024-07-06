from strings import get_hamming_distance, get_dna_complement

def main_menu():
    while True:
        print("\nMenu:")
        print("1-Hamming Distance")
        print("2-DNA Complement")
        print("3-Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            dna1 = input("Enter the first DNA string: ")
            dna2 = input("Enter the second DNA string: ")
            try:
                distance = get_hamming_distance(dna1, dna2)
                print("Hamming Distance:" + str(distance))
            except ValueError as e:
                print ("Error: " + str(e))

        elif choice == "2":
            dna = input("Enter the DNA string: ")
            try:
                complement = get_dna_complement(dna)
                print("DNA complement: " + complement)
            except ValueError as e:
                print("Error: " + str(e)) 
        

        elif choice == "3":
            print("Exiting the program. ")
            break

        else:
            print("Invalid option. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main_menu()
            
    