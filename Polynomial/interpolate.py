from Polynomial import Polynomial

Poly= Polynomial([])

f=Polynomial([1,2,3])
g=Polynomial([-8,17,0,5])

def interpolate(points):

    if len(points)==0:
        raise ValueError("Must have at least one point")

    x_values = [p[0] for p in points]

    if len(set(x_values))<len(x_values):
        raise ValueError("Not all x values are distinct")

    terms= [single_term(points, i) for i in range(0,len(points))]
    print("terms : ",terms)
    return sum(terms,Poly.getZERO())

def single_term(points, i):
    theTerm = Polynomial([1.])
    print("here",theTerm)
    xi, yi = points[i]

    for j, p in enumerate(points):
        if j==i:
            continue
        print("p:",p)
        xj = p[0]

        theTerm = theTerm* Polynomial(
            [-xj / (xi - xj) , 1.0/ (xi -xj)]
        )


        print("j",xj)
        print("i",xi)
        print(Polynomial(
            [-xj / (xi - xj) , 1.0/ (xi -xj)]
        ))
        print("term ",theTerm)
        print("yi",Polynomial([yi]))

    return theTerm * Polynomial([yi])

print("answer:",interpolate([(5,7),(10,1)]))