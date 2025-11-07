def problem2():
    # Problem Set 2: Extracting Information
    # From Descriptions:
    # Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
    quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
    index = quote.find('John F. Kennedy')
    personality_name = quote[index:]
    print(personality_name)
    # Manipulating Words:
    # Given the string info = "Python is fun. Fun is good. Good is subjective.",
    info = "Python is fun. Fun is good. Good is subjective."
    # a. Extract the word 'subjective' without knowing its exact position.
    Index_info = info.find('subjective')
    Info2 = info[Index_info:]
    print(Info2)
    # b. Extract every third word.
    info_split = info.split()
    print(info_split)
    # c. Reverse the positions of the words, but keep the characters in each word in the same order.
    Info_reversed = info[::-1]
    print(Info_reversed)