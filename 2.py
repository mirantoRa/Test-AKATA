def ConsecutiveDigits(num_str):
    for i in range(len(num_str) - 1):
        if num_str[i] == num_str[i + 1]:
            return True
    return False

def nonConsecutiveDigits(N):
    J = N + 1  
    
    while ConsecutiveDigits(str(J)):
        J += 1 
    
    return J

# Exemple 
N = 7
print(nonConsecutiveDigits(N))  # Affiche 8
