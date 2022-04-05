import requests
import json

with open("data.json", "w") as fi:
    data = []
    for i in range(1, 152):
        print(f"fetch pokemon {i}")
        url = f"https://pokeapi.co/api/v2/pokemon/{i}"
        pokemon = requests.get(url).json()

        types = []
        for t in pokemon["types"]:
            types.append({"slot": t["slot"], "type": {"name": t["type"]["name"]}})

        stats = []
        for s in pokemon["stats"]:
            stats.append({"base_stat": s["base_stat"], "stat":{"name": s["stat"]["name"]}})

        pokemon_data = {
            "id": pokemon["id"],
            "name": pokemon["name"],
            "types": types,
            "stats": stats
        }
        data.append(pokemon_data)
    
    json.dump(data, fi, indent=4)

