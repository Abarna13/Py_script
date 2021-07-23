# Python Program for count the words from file using Command line arguments

while True:
    print("Enter 'X' for exit")
    st = str(input("Enter any string: "))
    if st == 'x':
        break
    else:
        word_length = len(st.split())
    print("Number of words=",word_length,"\n")
    wordfreq = [] 
    st1 = st.split()
for w in st1:
    wordfreq.append(st1.count(w))
print("Word Frequencies",str(wordfreq))
print("Pairs of word and its frequencies",list(zip(wordfreq,st1)))