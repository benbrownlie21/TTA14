# a float is a number with a decimal point e.g. 1.2
# the difference between an integer and a float is the decimal point - an integer doesn't have a decimal point

start_value = 1.5
end_value = 5
step_value = 0.5

sequence = []

current_value = start_value
while current_value <= end_value:
    sequence.append(current_value)
    current_value += step_value

print(sequence)
