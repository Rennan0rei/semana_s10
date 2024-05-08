class Termometro:
    def __init__(self, temperatura=0):
        # Inicializa o objeto Termometro com uma temperatura em Celsius (padrão: 0)
        self.__temperatura_celsius = temperatura

    def set_temperatura_celsius(self, temperatura):
        # Define a temperatura em Celsius
        self.__temperatura_celsius = temperatura

    def set_temperatura_fahrenheit(self, temperatura):
        # Define a temperatura em Fahrenheit, convertendo-a para Celsius e armazenando-a
        self.__temperatura_celsius = (temperatura - 32) * 5/9

    def get_temperatura_celsius(self):
        # Obtém a temperatura atual em Celsius
        return self.__temperatura_celsius

    def get_temperatura_fahrenheit(self):
        # Obtém a temperatura atual em Fahrenheit, convertendo-a a partir da temperatura em Celsius
        return (self.__temperatura_celsius * 9/5) + 32

# Uso da classe
termometro = Termometro()
termometro.set_temperatura_fahrenheit(32)
print(termometro.get_temperatura_celsius())  # Deve mostrar 68
