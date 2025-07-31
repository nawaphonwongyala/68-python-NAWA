def format_strings(*name):
    return "".join(name).upper()
text = format_strings("Hello","-world","-this","-is","-a","-test")
print(text)
text = format_strings("Python","-is","-fun",)
print(text)
text = format_strings("Concatenate","-these","-strings","-please")
print(text)