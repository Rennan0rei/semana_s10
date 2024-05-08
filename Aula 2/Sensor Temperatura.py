class SensorTemperatura:
    def __init__(self, temperatura=0):
        self.__temperatura = temperatura

    def set_temperatura(self, nova_temperatura):
        if -50 <= nova_temperatura <= 150:
            self.__temperatura = nova_temperatura
        else:
            print("Temperatura fora do intervalo permitido.")

    def get_temperatura(self):
        return self.__temperatura

# Uso da classe
sensor = SensorTemperatura()
sensor.set_temperatura(25)
print(sensor.get_temperatura())  # Saída: 25
