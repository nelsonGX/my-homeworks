ae,rl=[float(x) for x in input("Please input a~e(separated by ,):").split(",")],[int(x) for x in input("Please input the range and NoD(separated by ,):").split(",")];[print(f"f({x})="+str(ae[0]*x**4+ae[1]*x**3+ae[2]*x**2+ae[3]*x+ae[4])) for x in range(rl[0],rl[1],rl[2])]