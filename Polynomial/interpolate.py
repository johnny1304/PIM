from ExamplesTest.Polynomial import Polynomial

zero= Polynomial([])

f=Polynomial([1,2,3])
g=Polynomial([-8,17,0,5])

def interpolate(points):

    if len(points)==0:
        raise ValueError("Must have at least one point")

    x_values = [p[0] for p in points]

    if len(set(x_values))<len(x_values):
        raise ValueError("Not all x values are distinct")

    terms= [single_term(points, i) for i in range(0,len(points))]
    return sum(terms,Polynomial.ZERO)

def single_term(points, i):
    theTerm = Polynomial([1.])
    xi, yi = points[i]

    for j, p in enumerate(points):
        if j==i:
            continue

        xj = p[0]
        theTerm = theTerm* Polynomial(
            [-xj / (xi - xj) , 1.0/ (xi -xj)]
        )

    return theTerm * Polynomial([yi])