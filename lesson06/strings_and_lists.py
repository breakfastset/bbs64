
text = "Hello world"

characters = list(text)
# ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

print(characters)

words = text.split(" ")  # delimiter

print(words)
# ['Hello', 'world']

line = "hello,good,bye,see,you"
print(line.split(","))