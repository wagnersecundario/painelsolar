
class Energia:
    def __init__(self, eficiencia):
        self.eficiencia = eficiencia
        self.historico = []
        self.economia_total = 0

    def calcular_economia(self, energia_gerada):
        if energia_gerada < 0:
            return "Erro: Valor de energia gerada inválido."
        
        # Calcula a economia
        economia = energia_gerada * (self.eficiencia / 100)
        self.economia_total += economia
        self.historico.append(energia_gerada)
        
        # Retorna o histórico e a economia total
        return {
            "historico": self.historico,
            "economia_total": round(self.economia_total, 2)
        }

# Função para rodar o plano de testes
def plano_de_testes():
    eficiencia = 85
    energia_calculadora = Energia(eficiencia)

    # Testes com as entradas especificadas
    entradas = [150, 100, 200, 0, -50]
    for energia_gerada in entradas:
        resultado = energia_calculadora.calcular_economia(energia_gerada)
        if isinstance(resultado, dict):
            print(f'Energia Gerada: {energia_gerada}, Eficiência: {eficiencia}%')
            print(f'Histórico: {resultado["historico"]}, Economia Total: {resultado["economia_total"]} kWh\n')
        else:
            print(f'Energia Gerada: {energia_gerada}, Eficiência: {eficiencia}%')
            print(resultado + "\n")

# Executa o plano de testes
plano_de_testes()
