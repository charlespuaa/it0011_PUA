def word_counter():
    statement = input("Enter a string statement:\n")

    exclude_words = ['a', 'an', 'the', 'and', 'but', 'or', 'nor', 'for', 'so', 'yet']

    # split words 
    words = statement.replace(',', '').replace('.', '').split()

    # Filter out excluded words
    filtered_words = []
    for word in words:
        if word.lower() not in exclude_words:
            filtered_words.append(word)

    # word counter function
    word_count = {}
    for word in filtered_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # separate lowercase and uppercase words
    lower_case_words = []
    upper_case_words = []

    for word in word_count.keys():
        if word.islower():
            lower_case_words.append(word)
        else:
            upper_case_words.append(word)

    # sort alphabetically
    lower_case_words.sort()
    upper_case_words.sort()

    # print word counts lowercase first
    for word in lower_case_words + upper_case_words:
        print(word.ljust(10), "-", word_count[word])

    # print total count of filtered words
    print("Total words filtered:", len(filtered_words))

# run
word_counter()
