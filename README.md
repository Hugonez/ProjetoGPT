# Gerador de Descrições de Produtos

Este projeto utiliza a API do OpenAI ChatGPT para gerar descrições de produtos com base em especificações fornecidas. O objetivo é criar descrições atraentes e informativas para novos produtos, como smartphones, destacando suas principais características.

## Integrantes do Projeto

- Hugo Jorge
- Gustavo Folena Araujo
- Igor Leonardo
- Felipe Renan
- Diana Astro
- Mateus Viera
- Pedro Balder

## Tecnologias Utilizadas

- **Python**: Linguagem de programação para o script.
- **requests**: Biblioteca para realizar chamadas HTTP.
- **json**: Biblioteca para manipulação de dados JSON.
- **OpenAI API**: API para gerar o texto da descrição com o modelo GPT-4.

## Funcionamento

1. **Configuração da API**: O código configura a URL e os cabeçalhos necessários para fazer solicitações à API do OpenAI ChatGPT.

2. **Dados da Solicitação**: Define o modelo a ser usado e a mensagem de entrada para a API, incluindo as instruções para gerar uma descrição atraente de um produto.

3. **Função `gerar_descricao_produto`**:
   - Informa ao usuário que o processo está em andamento.
   - Envia uma solicitação POST para a API com os dados configurados.
   - Verifica se a resposta foi bem-sucedida e, em caso afirmativo, formata e exibe a descrição do produto gerada.
   - Em caso de erro, exibe o código de status e a mensagem de erro.

4. **Função `formatar_texto`**: Formata o texto gerado para uma largura especificada, facilitando a leitura.

## Como Usar

1. **Instalar Dependências**: Certifique-se de que as bibliotecas necessárias estão instaladas. Você pode instalar o `requests` usando pip:

    ```bash
    pip install requests
    ```

2. **Configurar o Código**: Substitua a chave da API (`Bearer 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`) pelo seu token de autenticação da OpenAI.

3. **Executar o Script**: Execute o script Python para gerar uma descrição de produto. O script irá imprimir a descrição formatada no console.

    ```bash
    python nome_do_arquivo.py
    ```

## Exemplo de Uso

Suponha que você deseja gerar uma descrição para um novo smartphone. O código está configurado para gerar uma descrição para um smartphone com câmera de 108MP, bateria de longa duração e tela AMOLED de 6,5 polegadas. O resultado será exibido no console.

## Observações

- Certifique-se de manter sua chave da API segura e não a compartilhe publicamente.
- A geração de descrições pode levar alguns segundos, dependendo da carga da API e da complexidade do texto solicitado.

## Contribuições

Se você deseja contribuir para este projeto, por favor, entre em contato com os integrantes listados acima.

