sentence = input("Please enter a sentence ")
counter = 0
count_a = sentence.count("a")
count_e = sentence.count("e")
count_i = sentence.count("i")
count_o = sentence.count("o")
count_u = sentence.count("u")
total = (count_a + count_e +count_i + count_o + count_u)
print ("total number of vowels...",total)


sentence = input("please enter a sentence :")
length = len(sentence)
sentence_rev = ""
while length>0:
   sentence_rev += sentence[length-1]
   length = length-1
print (sentence_rev)
