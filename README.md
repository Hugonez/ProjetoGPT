# Gerador de Descrições de Produtos

Este projeto é um gerador de descrições de produtos otimizado para SEO, utilizando a API GPT-3.5 da OpenAI. O objetivo é criar descrições persuasivas e claras para produtos, levando em consideração suas características e o público-alvo.

## Requisitos

- Python 3.x
- Biblioteca `openai` (você pode instalá-la com `pip install openai`)

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Instale as dependências necessárias:
    ```bash
    pip install openai
    ```

3. Configure sua chave da API OpenAI. Você pode adicionar sua chave diretamente no código ou configurar uma variável de ambiente.

## Uso

### Exemplo de Uso

1. Abra o arquivo `gerador_descricao.py` e adicione sua chave da API OpenAI na variável `api_key`.
2. Defina o nome do produto, as características e o público-alvo. 
3. Execute o script:

    ```bash
    python gerador_descricao.py
    ```

### Parâmetros

- `api_key`: Sua chave da API OpenAI.
- `product_name`: O nome do produto para o qual deseja gerar uma descrição.
- `features`: Uma lista de características do produto.
- `audience`: O público-alvo do produto.

### Exemplo de Entrada

```python
api_key = "ADICIONAR API AQUI"
product_name = "Tênis de Corrida"
features = ["leve", "respirável", "sola antiderrapante", "disponível em várias cores"]
audience = "corredores de longa distância"
