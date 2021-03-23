from VBM import get_bmi
from pprint import pprint

data = [
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, 
    { "Gender": "Male", "HeightCm": 161, "WeightKg":85 }, 
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, 
    { "Gender": "Female", "HeightCm": 166,"WeightKg": 62}, 
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, 
    {"Gender": "Female","HeightCm": 167, "WeightKg": 82},
]

result = []
for sequence in data:
    # print (sequence)
    resp = get_bmi(sequence.get('WeightKg'), sequence.get('HeightCm'))
    sequence.update(resp) 
    result.append(sequence)
pprint(result)
