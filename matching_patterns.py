"""
* Entrada:
* - words  (list)
* - patterns (list)
* 
* Saída: list
"""
def wordsPatternsMatch(words, patterns):
    import re

    matching_patterns = []

    for pattern in patterns:
        matched = False
        regex = re.compile(pattern.replace(".", "."))
        for word in words:
            if regex.match(word):
                matching_patterns.append(pattern)
                print(f'"{pattern}" matches "{word}".')
                matched = True
                break
        if not matched:
            print(f'"{pattern}" does not match any words.')

    return matching_patterns

# Teste da função
words = ["grape", "banana", "melon", "apple"]
patterns = ["a..le", ".anana", "x..", "..ape", "m.lon"]
resultado = wordsPatternsMatch(words, patterns)
print(resultado)
