def max_subarray_sum(arr, k):
    n = len(arr)
    if n < k or k <= 0:
        return None  # Condicional modificada para fazer a verificação de entrada inválida: o array deve ter pelo menos k elementos e k deve ser positivo

    max_sum = sum(arr[:k])  # Trecho alterado para inicializar a soma máxima com a soma dos primeiros k elementos
    window_sum = max_sum  # Trecho substituído para configurar a soma da janela inicial

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]  
        max_sum = max(max_sum, window_sum) 

    return max_sum

def read_input():
    try:
        arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
        k = int(input("Enter the size of the subarray (k): "))
        return arr, k
    except ValueError:
        print("Invalid input. Please enter integers only.")  
        return [], 0  

def main():
    arr, k = read_input()
    if not arr or k <= 0 or len(arr) < k:  # Condicional acrescentada para fazer uma verificação adicional que confere se a entrada é válida
        print("Invalid input.")  # Exibe uma mensagem de erro se a entrada for inválida
    else:
        result = max_subarray_sum(arr, k)
        if result is not None:
            print("Maximum sum of a subarray of size {} is {}".format(k, result))  # Exibe o resultado

if __name__ == "__main__":
    main()
