import requests
import json
import time
 
# URL e cabeçalhos para a API do ChatGPT
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}
 
# Dados para a geração de descrição de produtos
data = {
    "model": "gpt-4",
    "messages": [
        {"role": "system", "content": "Você é um especialista em marketing e criação de descrições de produtos."},
        {"role": "user", "content": "Gere uma descrição atraente para um novo smartphone com câmera de 108MP, bateria de longa duração e tela AMOLED de 6,5 polegadas."}
    ],
    "temperature": 0.7,
    "max_tokens": 500,
    "n": 1
}
 
def gerar_descricao_produto():
    # Informar ao usuário que o processo está em andamento
    print("Gerando descrição do produto... Isso pode levar alguns segundos.")
    time.sleep(1)  # Pequena pausa para enfatizar a mensagem
 
    # Enviar a solicitação para a API
    response = requests.post(url, headers=headers, json=data)
 
    # Verificar se a resposta foi bem-sucedida
    if response.status_code == 200:
        response_json = response.json()
        message_content = response_json['choices'][0]['message']['content']
 
        # Formatar e exibir a descrição do produto
        print("\nDescrição do Produto:\n")
        formatted_message = formatar_texto(message_content)
        print(formatted_message)
    else:
        print(f"Erro: {response.status_code}")
        print(response.json())
 
def formatar_texto(texto, largura=80):
    """Função para formatar o texto com uma largura especificada."""
    import textwrap
    return "\n".join(textwrap.fill(paragrafo, largura) for paragrafo in texto.split("\n\n"))
 
# Chamar a função para gerar a descrição do produto
gerar_descricao_produto()
