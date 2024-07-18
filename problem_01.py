def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # Condicional acrescentada com o intuito de evitar a divisão por zero, pro caso de a lista estar vazia
    total = sum(numbers)
    return total / len(numbers)

def find_max(numbers):
    if len(numbers) == 0:
        return None  # Condicional acrescentada para lidar melhor com os casos em que a lista estiver vazia, retornando None, já que não há máximo em uma lista vazia
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def get_numbers():
    while True:
        try:
            numbers = input("Enter numbers separated by spaces: ").split()
            numbers = [int(num) for num in numbers] 
            return numbers
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")  # Bloco de tratamento de exceções acrescentado pro caso de a entrada ser inválida  

def main():
    numbers = get_numbers()
    if len(numbers) == 0:
        print("No numbers entered.")  # Condicional e mensagem acrescentadas para informar se/quando nenhum número for inserido
    else:
        print("Average:", calculate_average(numbers))
        print("Maximum:", find_max(numbers))

if __name__ == "__main__":
    main()
