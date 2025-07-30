def format_strings(*name):
    return "".join(name).upper()
result = format_strings("Hello","world","this","is","a","test")
print(result)
result = format_strings("Python","is","fun",)
print(result)
result = format_strings("Concatenate","these","strings","please")
print(result)