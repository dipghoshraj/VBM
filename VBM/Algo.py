
from .scale import get_weight_scale

def calculate_bmi(weight, height):
    height = chnage_height(height)
    _bmi = weight/height
    formatted_bmi = "{:.2f}".format(_bmi)

    _weight_index = get_scale(_bmi)
    return {
        "bmi": float(formatted_bmi),
        "result": _weight_index
    }

def chnage_height(height):
    height = height/100
    return height
    
def get_scale(_bmi):

    if _bmi < 18.4:
        return get_weight_scale(1)
    if 18.4 <= _bmi <= 24.9:
        return get_weight_scale(2)
    if 25 <= _bmi <= 29.9:
        return get_weight_scale(3)
    if 30 <= _bmi <= 34.9:
        return get_weight_scale(4)
    if 35 <= _bmi <= 39.9:
        return get_weight_scale(5)
    if _bmi >= 40:
        return get_weight_scale(6)