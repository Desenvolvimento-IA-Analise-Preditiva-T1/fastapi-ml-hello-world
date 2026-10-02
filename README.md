# API de Predição de Crédito (Deploy com Arquivo Local)

Este projeto implementa uma API simples utilizando **FastAPI** para servir predições de um modelo de Machine Learning treinado com **Scikit-Learn**. 

Nesta arquitetura, os pesos do modelo preditivo são salvos diretamente em disco como um arquivo serializado (`.joblib`).

---

## Arquitetura do Projeto

1. **Treinamento & Serialização:** O script `modelo_ml.ipynb` treina o modelo preditivo e o congela em um arquivo físico `modelo_emprestimo.joblib`.
2. **Carregamento:** A API (`main.py`) carrega o arquivo `.joblib` para a memória RAM, durante o startup da aplicação.
3. **Validação com Pydantic:** Toda requisição `POST /predict` é validada antes de chegar ao modelo.
4. **Inferência em Tempo Real:** O modelo executa a predição e devolve a resposta no formato JSON.
