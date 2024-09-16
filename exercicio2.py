import random
import string

def senha(t):
    caracters = string.ascii_letters + string.digits
    if t == 0:
        return ""
    caractersal = random.choice(caracters)
    if caractersal in caracters:
        i = caracters.index(caractersal) 
        caracterscrip = caracters[i +3]

    

    return caracterscrip + senha(t-1)

res = senha(8)
print(res)