text = "escribe el texto aqui!"
binary_text = ' '.join(format(ord(i), 'b') for i in text)
print(binary_text)