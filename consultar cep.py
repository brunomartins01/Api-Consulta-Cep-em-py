import requests

# Loop para solicitar o CEP até que um valor numérico válido seja fornecido
while True:
    try:
        cep = int(input("Digite o CEP: "))
        break
    except ValueError:
        print("Por favor, digite apenas números para o CEP.")

# URL da API de CEP
url = f"https://viacep.com.br/ws/{cep}/json/"

# Enviar o pedido GET para a API
response = requests.get(url)

# Exibir a resposta da API
print("Resposta da API:", response.text)

# Verifica a resposta da API e traz os dados
try:
    resultado = response.json()
    print("CEP:", resultado.get("cep"))
    print("Logradouro:", resultado.get("logradouro"))
    print("Complemento:", resultado.get("complemento"))
    print("Bairro:", resultado.get("bairro"))
    print("Cidade:", resultado.get("localidade"))
    print("UF:", resultado.get("uf"))

# Exibir mensagem de erro
except requests.exceptions.JSONDecodeError as e:
    print("Erro ao decodificar JSON. Resposta da API:", response.text)
    print("Exceção:", e)

# Dados do CEP digitado
print("Cep: {}".format(cep))
