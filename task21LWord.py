def find_longest_word(word_list):  
    longest_word = ''  
    for word in word_list:    
          print(word, len(word))  


words = input('Введите предложение из несколких слов: ')  
word_list = words.split()  
find_longest_word(word_list)