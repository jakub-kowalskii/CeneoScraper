import os
import pandas as pd

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")
item_id = input(str("Input your item id from the site link (numbers between .pl/ and #tab): "))

opinions = pd.read_json("opinions/"+item_id+".json")
print(opinions)