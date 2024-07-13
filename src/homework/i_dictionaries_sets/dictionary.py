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

def parse_fasta(fasta_str):
    sequences = []
    current_seq = []
    for line in fasta_str.split('\n'):
        if line.startswith('>'):
            if current_seq:
                sequences.append(current_seq)
                current_seq = []
        else:
            current_seq.extend(list(line.strip()))
    if current_seq:
        sequences.append(current_seq)
    return sequences

def main():
    while True:
        print("1-Get p distance matrix")
        print("2-Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter the number of DNA strings: "))
            dna_strings = []
            for i in range(n):
                dna_string = input("Enter DNA string {}: " .format(i+1))
                dna_strings.append(list(dna_string.strip()))

            matrix = get_p_distance_matrix(dna_strings)
            print("P-distance matrix:")
            for row in matrix:
                print(' '.join("(:.5f)".format(dist) for dist in row))
        
        elif choice == '2':
            break
        else:
            print("Invalid choice, try again.")