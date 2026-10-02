from fastapi import HTTPException
from fastapi import APIRouter

from cliente import DadosCliente

import joblib


# Carregamos o modelo salvo em disco na memória
modelo = joblib.load("modelo_emprestimo.joblib")

# Criamos o roteador com prefixo
predict_route = APIRouter(prefix="/predict", tags=["Predição"])

# Criamos o endpoint de predição usando POST
@predict_route.post("/predict", tags=["Predição"])
def prever_aprovacao(cliente: DadosCliente):
    """
    Recebe as características do cliente e devolve se o crédito foi Aprovado ou Recusado.
    """
    try:
        # Preparamos os dados no formato de matriz 2D que o modelo espera: [[idade, score]]
        dados_entrada = [[cliente.idade, cliente.pontuacao_credito]]
        
        # Executamos a predição com o modelo congelado
        resultado = modelo.predict(dados_entrada)[0]
        
        # Traduzimos o resultado numérico (0 ou 1) em uma mensagem amigável de negócio
        if resultado == 1:
            status = "Aprovado"
        else:
            status = "Reprovado"
        
        return {
            "idade_informada": cliente.idade,
            "pontuacao_informada": cliente.pontuacao_credito,
            "decisao": status,
            "codigo_decisao": int(resultado)
        }
    except Exception as erro:
        # Tratamento de erros seguro sem derrubar o servidor
        raise HTTPException(status_code=500, detail=f"Erro no processamento da predição: {str(erro)}")