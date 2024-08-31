import openai

def configure_openai_api(api_key):
    openai.api_key = api_key

def generate_prompt(product_name, features, audience):
    prompt = (
        f"Você é um especialista em marketing de produtos. "
        f"Seu trabalho é criar uma descrição detalhada e otimizada para SEO "
        f"para o seguinte produto:\n\n"
        f"Nome do Produto: {product_name}\n"
        f"Características: {', '.join(features)}\n"
        f"Público-Alvo: {audience}\n\n"
        f"Por favor, escreva uma descrição que seja persuasiva, clara, e inclua palavras-chave relevantes para SEO."
    )
    return prompt

def generate_product_description(api_key, product_name, features, audience):
    configure_openai_api(api_key)
    
    prompt = generate_prompt(product_name, features, audience)
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um especialista em marketing de produtos."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    description = response.choices[0].message['content'].strip()
    return description

if __name__ == "__main__":
    api_key = "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"
    product_name = "Tênis de Corrida"
    features = ["leve", "respirável", "sola antiderrapante", "disponível em várias cores"]
    audience = "corredores de longa distância"

    description = generate_product_description(api_key, product_name, features, audience)
    print("Descrição Gerada:")
    print(description)