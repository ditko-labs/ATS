class ProcessadorDeAcoes():

    def validar_dados(self, dados: dict) -> bool:
        return True

    def salvar_dados(self, dados: dict) -> bool:
        return True


def executar_processo(processador: ProcessadorDeAcoes, dados: dict):
        
        dados_validos = processador.validar_dados(dados)

        if dados_validos:
            processador.salvar_dados(dados)
            return "Dados salvos com sucesso"
        else:
            return "Erro na validação de dados"