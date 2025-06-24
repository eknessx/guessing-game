def swap_words(sentence):
    words = sentence.split()
    if len(words) < 2:
        return sentence  
    words[0], words[-1] = words[-1], words[0]
    return ' '.join(words)

input_sentence = input("Entrez une phrase : ")
result = swap_words(input_sentence)
print("Résultat :", result)