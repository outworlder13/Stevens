import sys
from decimal import Decimal

maxPrecision = Decimal("1E-14")

def roundNearest(num, maxDelta=-1):
    dNum = Decimal(str(num))
    maxDelta = Decimal(str(maxDelta))
    if maxDelta<0:
        maxDelta = maxPrecision
    if maxDelta>Decimal("0.00001"):
        maxDelta = maxDelta / 10
    rez = dNum.quantize(Decimal("1"))
    if abs(dNum - rez) < maxDelta:
        return rez
    for i in range(6):
        rez = dNum.quantize(Decimal("1.0"+("0"*i)))
        if abs(dNum - rez) < maxDelta:
            return rez
    return dNum

def classifyTriangle(strA, strB, strC):
    dA = roundNearest(strA)
    dB = roundNearest(strB)
    dC = roundNearest(strC)
    dA2 = roundNearest(dA**2)
    dB2 = roundNearest(dB**2)
    dC2 = roundNearest(dC**2)

    if dA == dB == dC:
        return "equilateral triangle"
    elif dA == dB:
        if abs(dC2 - dA2 - dB2) < maxPrecision:
            return "right isosceles triangle"
        else:
            return "isosceles triangle"
    elif dA == dC:
        if abs(dB2 - dA2 - dC2) < maxPrecision:
            return "right isosceles triangle"
        else:
            return "isosceles triangle"
    elif dC == dB:
        if abs(dA2 - dC2 - dB2) < maxPrecision:
            return "right isosceles triangle"
        else:
            return "isosceles triangle"
    else:
        if abs(dC2 - dA2 - dB2) < maxPrecision:
            return "right scalene triangle"
        elif abs(dB2 - dA2 - dC2) < maxPrecision:
            return "right scalene triangle"
        elif abs(dA2 - dC2 - dB2) < maxPrecision:
            return "right scalene triangle"
        else:
            return "scalene triangle"


if __name__ == '__main__':
    if len(sys.argv) > 3:
        print( classifyTriangle(sys.argv[1], sys.argv[2], sys.argv[3]) )
    else:
        print("Please provide the 3 triangle side lengths")