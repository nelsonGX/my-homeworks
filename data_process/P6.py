def calculate(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return 0

n = int(input("Please input N (number of tuples):"))

data_tuples = []

for i in range(n):
    print(f"{i+1}th tuple:")
    op_string = input("+ OPString:")
    number_a = int(input("+ NumberA:"))
    number_b = int(input("+ NumberB:"))
    
    data_tuples.append((op_string, number_a, number_b))

dataTP = tuple(data_tuples)

results = []
for op, a, b in dataTP:
    result = calculate(op, a, b)
    results.append(result)

print(f"dataTP is {dataTP}.")
print(f"answerTP is {tuple(results)}")