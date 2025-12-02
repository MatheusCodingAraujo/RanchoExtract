import requests
import pandas as pd

headers = {
    'accept': 'application/json',
    'x-access-token-ws': 'd1bf4238656c2167c5997e4081b549eedd0a25622a18740d8ad1a8a31ee22b15'
}

# --------------------- FAZENDA --------------------------------------#
url = 'https://api.irancho.com.br/api/fazenda'
response = requests.get(url, headers=headers)
fazenda_list = response.json()
df_fazenda = pd.json_normalize(fazenda_list)
print(f'fazenda {response.status_code}')

df_fazenda.drop(columns=['programas', 'subdivisoes'], inplace=True)

# -------------------- ANIMAL ---------------------------------------#
url = 'https://api.irancho.com.br/api/animal'
response = requests.get(url, headers=headers)
animal_list = response.json()
print(f'animal {response.status_code}')
for animal in animal_list:
    animal['no_categoria_animal'] = animal.get(
        'categoria_atual', {}).get('no_categoria_animal', None)
    animal['no_sexo'] = animal.get('sexo', {}).get('no_sexo', None)

df_animal = pd.json_normalize(animal_list)
df_animal = df_animal.filter(items=['id_animal', 'id_animal_fazenda',
                             'idade_meses', 'no_categoria_animal', 'no_sexo', 'peso', 'id_fazenda'])
