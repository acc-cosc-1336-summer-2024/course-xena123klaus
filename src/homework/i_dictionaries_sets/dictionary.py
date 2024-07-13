def get_p_distance(list1, list2):
    differences = sum(1 for a, b in zip(list1, list2) if a !=b)
    return differences / len(list1)


def get_p_distance_matrix(list_of_lists):
    n = len(list_of_lists)
    matrix = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = get_p_distance(list_of_lists[i], list_of_lists[j])

    return matrix


def is_valid_dna_string(dna_string):
    return all(char in 'ATCG' for char in dna_string)

def main():
    while True:
        print("1-Get p distance matrix")
        print("2-Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter the number of DNA strings: "))
            dna_strings = []
            dna_length = None
            for i in range(n):
                dna_string = input(f"Enter DNA string {i+1}: ").strip()

                if not is_valid_dna_string(dna_string):
                    print("Invalid DNA string. DNA strings must contain only 'A', 'T', 'C', 'G'.")
                    return
                
                if dna_length is None:
                    dna_length = len(dna_string)
                elif len(dna_string) != dna_length:
                    print("All DNA strings must be of the same length.")
                    return
                dna_strings.append(list(dna_string))

            matrix = get_p_distance_matrix(dna_strings)
            print("P-distance matrix:")
            for row in matrix:
                
                for dist in row:
                    print("{:.5f}".format(dist), end=' ')
                print()  
        
        elif choice == '2':
            break
        else:
            print("Invalid choice, please try again.")





