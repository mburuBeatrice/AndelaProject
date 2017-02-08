def words(phrase):
    word_list = phrase.split()
    word_dict = {}
    for word in word_list:
        word = word.strip()
        if word.isdigit():
            word = int(word)
        if not word in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict