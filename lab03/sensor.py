
threshold = float(input())
n = int(input())

errors = 0
exceedances = 0
count = 0
total = 0.0
maximum = 0.0

for i in range(n):
    value = input()

    if value == 'error':
        errors += 1
    else:
        temperature = float(value)
        count += 1
        total += temperature

        if temperature > threshold:
            exceedances += 1

        if count == 1 or temperature > maximum:
            maximum = temperature

average = total / count

print(n)
print(errors)
print(exceedances)
print(f'{maximum:.1f}')
print(f'{average:.1f}')
