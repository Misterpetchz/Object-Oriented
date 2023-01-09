
hr1,m1,hr2,m2 = [int(x) for x in input("Enter your In and Out: ").split()]
dhr = hr2 - hr1
dm = m2 - m1
time = (hr2 * 60 - m2) - (hr1 * 60 + m1)
if time < 15:
    print("0 bant")
    exit()
if dm > 0:
    dhr += 1
if dhr <= 3:
    paid = dhr * 10
elif dhr <= 6:
    paid = 30 + ((dhr - 3) * 20)
elif dhr > 6:
    paid = 200
print(paid ,"bant")