class Lampada:
    def __init__(self):
        self.estado = False  # Começa desligada

    def ligar(self):
        if not self.estado:  # Verifica se a lâmpada já está ligada
            self.estado = True
            print("Lâmpada ligada.")
        else:
            print("A lâmpada já está ligada.")

    def desligar(self):
        if self.estado:  # Verifica se a lâmpada já está desligada
            self.estado = False
            print("Lâmpada desligada.")
        else:
            print("A lâmpada já está desligada.")

# Função para escolher entre ligar e desligar
def escolher_opcao(lampada):
    while True:
        opcao = input("Digite 1 para ligar a lâmpada, 0 para desligar ou qualquer outra coisa para sair do programa: ")
        if opcao == '1':
            lampada.ligar()
        elif opcao == '0':
            lampada.desligar()
        else:
            print("Saindo do programa...")
            break

# Uso da classe
lampada = Lampada()
escolher_opcao(lampada)
print(lampada.estado)