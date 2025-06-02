def get_num_words(input_text):
    words=input_text.split()
    return f"{len(words)}"

def get_num_chars(input_text):
    alphabet = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,  
    }
    lowered_text = input_text.lower()

    for c in lowered_text:
        if c in alphabet:
            alphabet[c] +=1
    
    return alphabet

def sort_chars(dictionary):
    list = []    
    for letter in dictionary:
        list.append({"char": letter, "num":dictionary[letter]})
    list.sort(reverse=True, key=sort_on)
    
    return list

def sort_on(dict):
    return dict["num"]
