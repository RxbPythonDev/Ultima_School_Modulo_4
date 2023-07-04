# Importar a lib requests-html
from requests_html import HTMLSession
import sqlite3

conexao = sqlite3.connect('db')
cursor = conexao.cursor()


# Criar uma sessão HTTP usando a classe HTMLSession
sessao = HTMLSession()

# Escolher a URL que vamos trabalhar
url = 'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone'

# Fazer uma requisição Get à página web usando a sessão criada
resposta = sessao.get(url)

# Usar o método find do objeto html para encontrar a informação que preciso
# Usaremos a estrutura da página:
'''
# -> Selecionar o seletor css id ou inicializar o scrap
ad-list -> o que diferencia a tag <ul> das demais tags
li -> está dentro da tag ul (ad-list)
a -> contém todas as informações que precisamos
'''
dados = resposta.html.find('#ad-list li a')
# print(dados)

for mineirando_dados in dados:
    # Extrai o título de cada anúncio atráves do atributo title
    titulo = mineirando_dados.attrs['title']
    print(titulo)
    
    # Extrai o link do anúncio
    url_anuncio = mineirando_dados.attrs['href']
    print(url_anuncio)

    # Dentro do href, irei buscar a informação do preço assim como fizemos dentro do site olx
    # Pegaremos na posição h2[0] pois na posição h2[2] existem anúncios que não possuem o preço informado ,gerando estouro da lista (list index error)
    response_preco = sessao.get(url_anuncio)
    preco = response_preco.html.find('h2')[0].text
    print(preco)

    # Inserindo informações dentro do banco de dados

    query = 'insert into anuncios (produto, preco, href) values (?, ?, ?)'
    valores = [titulo, preco, url_anuncio]

    cursor.execute(query,valores)


conexao.commit()
conexao.close()