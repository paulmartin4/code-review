from copy import deepcopy

def primary_forbidden_sequences(list_of_all_forbidden_sequences,P):
    all_sequences = deepcopy(list_of_all_forbidden_sequences)
    index_to_be_taken = [0]*P
    for i in range(P):
        if index_to_be_taken[i] == 0:
            current_sequence = all_sequences[i]
            n = len(current_sequence)
            working_sequences = deepcopy(all_sequences)
            for j in range(n):
                if len(working_sequences) > 1:
                    working_sequences = [sequence for sequence in working_sequences if (len(sequence) >= j+1)] # We keep only the long enough sequences
                    """bis = []
                    for k in range(len(working_sequences)):
                        if len(working_sequences[k]) >= j+1:
                            bis.append(working_sequences[k])
                    working_sequences = bis"""
                    working_sequences = [sequence for sequence in working_sequences if current_sequence[j] == sequence [j]] #We keep only the sequences that match the j first characters
            
            # Here working_sequences contain all the sequences that starts the same as the ith one
            
            if len(working_sequences) > 1: #Means that a longer sequences as the ith one which start the same exist
                index_of_current = working_sequences.index(current_sequence)
                del working_sequences[index_of_current]
                for sequence in working_sequences:
                    index_of_non_primary = all_sequences.index(sequence)
                    index_to_be_taken[index_of_non_primary] += 1
    
    primary_forbidden_sequences = []
    for i in range(P):
        if index_to_be_taken[i] == 0:
            primary_forbidden_sequences.append(all_sequences[i])
    
    return primary_forbidden_sequences

def number_of_impossible_sequences(sequence):
    return 2**(N-len(sequence))

def total_number_of_possible_sequence(sequences):
    impossible_number = 0
    for sequence in sequences:
        impossible_number += number_of_impossible_sequences(sequence)
    return (2**N - impossible_number)

t = int(input())

for i in range(1,t+1):
    N,P = [int(s) for s in input().split(" ")]
    list_of_all_forbidden_sequences = []
    for j in range(P):
        list_of_all_forbidden_sequences.append(list(input()))
    print("Case #{}: {}".format(i,total_number_of_possible_sequence(primary_forbidden_sequences(list_of_all_forbidden_sequences,P))))