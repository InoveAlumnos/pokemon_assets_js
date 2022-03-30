import requests
import shutil

for i in range(152):
    pkid = i
    pkid_str = str(pkid).rjust(3, '0')
    url = f"https://assets.pokemon.com/assets/cms2/img/pokedex/detail/{pkid_str}.png"

    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(f'./assets/{pkid_str}.png', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)  