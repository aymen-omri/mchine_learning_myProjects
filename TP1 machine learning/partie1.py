import math
def delta(a,b,c):
    return b*b-4*a*c

def solution(a,b,c):
    deltaC = delta(a,b,c)
    if deltaC>0:
        racineDelta = math.sqrt(deltaC)
        retour = [(-b*b-racineDelta)/(2*a),(-b*b+racineDelta)/(2*a)]
        
    elif deltaC<0:
        retour = []
    else : 
        retour = [-b/(2*a)]
    return retour

def occ(ch,c):
    nb = 0
    for i in ch:
        if i == c : 
            nb = nb+1
    return nb



