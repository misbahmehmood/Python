def first_two(str):
  if len(str)<2:
    return str
  return str[:2]
print(first_two("python"))

def extra_end(str):
      return str[-2:]*3
print(extra_end("hello"))

def first_half(str):
      return str[:len(str) //2]
print(first_half("Yellow"))