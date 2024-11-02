# ------------------ PESSOA -----------------------#
url = 'https://api.irancho.com.br/api/pessoa'
response = requests.get(url, headers=headers)
pessoa_list = response.json()
df_pessoa = pd.json_normalize(pessoa_list)
print(f'pessoa {response.status_code}')

# criar df com colunas/objeto dentro de DF principal extraido
df = pd.DataFrame(df_pessoa['fazendas'])
df_non_empty = df[df['fazendas'].str.len() > 0]
df_fazendas = pd.json_normalize(df_non_empty['fazendas'].explode())

# criar df com colunas/objeto dentro de DF principal extraido
df = pd.DataFrame(df_pessoa['Categorias'])
df_non_empty = df[df['Categorias'].str.len() > 0]
df_categorias = pd.json_normalize(df_non_empty['Categorias'].explode())

df_pessoa.drop(columns=['Categorias', 'fazendas', 'contatos'], inplace=True)

# -------------------- FAZENDA ---------------------------------------#
url = 'https://api.irancho.com.br/api/fazenda'
response = requests.get(url, headers=headers)
fazenda_list = response.json()
df_fazenda = pd.json_normalize(fazenda_list)
print(f'fazenda {response.status_code}')

# criar df com colunas/objeto dentro de DF principal extraido
df = pd.DataFrame(df_fazenda['programas'])
df_non_empty = df[df['programas'].str.len() > 0]
df_programas = pd.json_normalize(df_non_empty['programas'].explode())

# criar df com colunas/objeto dentro de DF principal extraido
df = pd.DataFrame(df_fazenda['subdivisoes'])
df_non_empty = df[df['subdivisoes'].str.len() > 0]
df_subdivisoes = pd.json_normalize(df_non_empty['subdivisoes'].explode())

# criar df com colunas/objeto dentro de DF principal extraido
df = pd.DataFrame(df_programas['json_racas_utilizadas'])
df_non_empty = df[df['json_racas_utilizadas'].str.len() > 0]
df_racas_utilizadas = pd.json_normalize(
    df_non_empty['json_racas_utilizadas'].explode())

df_programas.drop(columns=['json_racas_utilizadas',
                  'json_categorias_registro_utilizadas'], inplace=True)
df_fazenda.drop(columns=['programas', 'subdivisoes'], inplace=True)

# -------------------- localidades ---------------------------------------#
url = 'https://api.irancho.com.br/api/localidades/estado'
response = requests.get(url, headers=headers)
localidades_list = response.json()
df_localidades = pd.json_normalize(localidades_list)
print(f'localidades {response.status_code}')

# ----------------------- DF PARA SQLITE------------------------------#
df_categorias.to_sql('Categorias', con=engine,
                     if_exists='replace', index=False)
df_fazendas.to_sql('Pessoa_Fazendas', con=engine,
                   if_exists='replace', index=False)
df_pessoa.to_sql('Pessoa', con=engine, if_exists='replace', index=False)
df_fazenda.to_sql('Fazenda', con=engine, if_exists='replace', index=False)
df_programas.to_sql('Fazenda_programa', con=engine,
                    if_exists='replace', index=False)
df_subdivisoes.to_sql('Fazenda_subdivisoes', con=engine,
                      if_exists='replace', index=False)
df_localidades.to_sql('Localidades', con=engine,
                      if_exists='replace', index=False)
'''

dados_reproducao = []
for id_animal in idanimal_list:
    url = f'https://api.irancho.com.br/api/animal/{id_animal}/reproducao'
    response = requests.get(url, headers=headers)
    i = 0
    if response.status_code == 200:  # Verifica se a requisição foi bem-sucedida
        dados_animal = response.json()  # Extrai o conteúdo da resposta
        dados_reproducao.append(dados_animal)  # Adiciona os dados na lista
df_reproducao = pd.json_normalize(dados_reproducao)
print(f'reproducao {response.status_code}')

url = 'https://api.irancho.com.br/api/nutricao'
response = requests.get(url, headers=headers)
nutricao_list = response.json()
df_nutricao = pd.json_normalize(nutricao_list)
print(f'nutricao {response.status_code}')
save_to_sqlite(df_nutricao, 'nutricao')

url = 'https://api.irancho.com.br/api/venda-animais'
response = requests.get(url, headers=headers)
venda_animais_list = response.json()
df_venda_animais = pd.json_normalize(venda_animais_list)
print(f'venda_animais {response.status_code}')
save_to_sqlite(df_venda_animais, 'venda_animais')

url = 'https://api.irancho.com.br/api/produto'
response = requests.get(url, headers=headers)
produto_list = response.json()
df_produto = pd.json_normalize(produto_list)
print(f'produto {response.status_code}')
save_to_sqlite(df_produto, 'produto')

idproduto_list = df_produto['id_produto']

dados_movimentacao = []
for id_produto in idproduto_list:
    url = f'https://api.irancho.com.br/api/produto/{id_produto}/movimentacao'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        dados_produto = response.json()
        dados_movimentacao.append(dados_produto)
df_reproducao = pd.json_normalize(dados_movimentacao)
print(f'movimentacao {response.status_code}')
'''
