# TODO решите задачу
import json
import os.path
def task(file_path) -> float:
    with open(file_path,'rt') as file:
        numb =json.load(file)
    total=round(sum(item['score']*item['weight'] for item in numb),3)
    return total
path = os.path.abspath('input.json')

print(task(path))
