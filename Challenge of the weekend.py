def comma_seperated(sequence):
    word= sequence.sort()
    return ','.join(sequence)
inp= input("Enter comma seperated words: ").split(',')
print(comma_seperated(inp))