def word_counter():
    userInput = input("Enter a string statement:\n")
    
    ignore_words = ['a', 'an', 'the', 'and', 'but', 'or', 'of', 'nor', 'for', 'so', 'yet']
    
    # remove punctuation (commas and periods) and split text into words
    words = userInput.replace(',', '').replace('.', '').split()
    
    # ito---creates a new list with only words not in the ignore list
    valid_words = []
    for word in words:
        if word.lower() not in ignore_words:
            valid_words.append(word)
    
    # actual words counter
    word_count = {}
    for word in valid_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    # separate lowercase and uppercase letters
    lower_words = []
    upper_words = []
    for word in word_count.keys():
        if word.islower():
            lower_words.append(word)
        else:
            upper_words.append(word)
    
    # sort alphabetically
    lower_words.sort()
    upper_words.sort()
    
    # print word count lowercase first
    for word in lower_words + upper_words:
        print(word.ljust(10), "-", word_count[word])
    
    #print total
    print("Total words:", len(valid_words))

word_counter()
