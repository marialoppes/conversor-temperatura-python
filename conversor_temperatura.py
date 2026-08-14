# Solicita ao usuário a temperatura em graus Celsius

# Converte o valor digitado (string) para float, permitindo cálculos com casas decimais
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

# Realiza a conversão de Celsius para Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

# Exibe o resultado da conversão
print(f"A temperatura convertida é {temperatura_fahrenheit} graus Fahrenheit.")