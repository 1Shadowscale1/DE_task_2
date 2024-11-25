import json
import msgpack
import os

data = []
with open('./resources/third_task.json') as json_file:
    data = json.load(json_file)

aggregated_data = {}
for item in data:
    name = item["name"]
    price = item["price"]
    if name not in aggregated_data:
        aggregated_data[name] = {"prices": []}
    aggregated_data[name]["prices"].append(price)

results = []
for name, item_data in aggregated_data.items():
    prices = item_data["prices"]
    results.append({
        "name": name,
        "avg_price": sum(prices) / len(prices),
        "max_price": max(prices),
        "min_price": min(prices)
    })


with open("./aggregated_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

with open("./aggregated_data.msgpack", "wb") as f:
    msgpack.pack(results, f)

file_sizes = {}
for filename in ["./aggregated_data.json", "./aggregated_data.msgpack"]:
    file_sizes[filename] = os.path.getsize(filename)

print("Размеры файлов:")
for filename, size in file_sizes.items():
    print(f"{filename}: {size} bytes ({size / 1024:.2f} KB)")