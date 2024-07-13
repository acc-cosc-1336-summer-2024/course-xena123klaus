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





