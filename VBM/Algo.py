# BMI_data = [
#     {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, 
#     {"Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, 
#     {"Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, 
#     {"Gender": "Female", "HeightCm": 166, "WeightKg": 62}, 
#     {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, 
#     {"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
# ]

def calculate_bmi(weight, height):
    height = chnage_height(height)
    bmi = weight/height
    return bmi

def chnage_height(height):
    height = height/100
    return height
