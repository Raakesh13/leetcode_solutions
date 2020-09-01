def addBinary(a: str, b: str) -> str:
    if len(a) < len(b):
        a, b = b, a
        print(a, b)
    out = ""
    carry = "0"
    for i, j in zip(a[::-1], b[::-1]):
        if carry == "1":
            if i == j == "1":
                out = "1"+out
                carry = "1"
            elif i == "0" and j == "1" or i == "1" and j == "0":
                out = "0"+out
                carry = "1"
            elif i == j == "0":
                out = "1"+out
                carry = "0"
        else:
            if i == j == "1":
                out = "0"+out
                carry = "1"
            elif i == "0" and j == "1" or i == "1" and j == "0":
                out = "1"+out
            elif i == j == "0":
                out = "0"+out
        print(out)

    for i in a[-len(b)-1::-1]:
        if carry == "1":
            if i == "1":
                out = "0"+out
                carry = "1"
            elif i == "0":
                out = "1"+out
                carry = "0"
        else:
            if i == "1":
                out = "1"+out
            elif i == "0":
                out = "0"+out
    if carry == "1":
        out = "1" + out
    return out


a = "100"
b = "110010"
print(addBinary(a, b))
