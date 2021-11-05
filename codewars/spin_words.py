def spin_words(sentence):
    words = sentence.split()

    result_words = []
    for w in words:
        if len(w) >= 5:
            result_words.append(w[::-1])
        else:
            result_words.append(w)
    
    return " ".join(result_words)

def main():
    print(spin_words("Welcome"))
    print(spin_words("Hey fellow warriors"))
    print(spin_words("This is a test"))

if __name__ == "__main__":
    main()