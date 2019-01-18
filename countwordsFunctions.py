

####################################################
#COUNTING HOW MANY TIMES A WORD SHOWS IN A TEXT FILE
####################################################

def countWords(infile):
    counts = {}
    data = open(infile, 'r')

    for line in data:
        
        words = line.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    return counts

#create a function called countWords with the parameter(infile)
#create an empty dictionary called counts
#create a variable called data that opens the chosen file when called.
#for each line in data:
    #we create a variable called words that equals to splitting the words up.
    #for each words in the line
        #if the word is in the dictionary
            #dictionary[key word] + 1
        #else
            #dictionary[key word] = 1
    #return the dictionary

#THE OUTPUT WILL BE A LIST OF WORDS WITH HOW MANY TIMES THEY SHOW IN THE TEXT FILE

#########################################################
#ORDERING THE AMOUNT OF TIMES THE WORD SHOWS (DESCENDING)
#########################################################
    
def printTop20(counts):
    
    words = list(counts.keys())
    words.sort(reverse=True, key=lambda v:counts[v])
    words = words[:20]
    for word in words:
        print(word, '=', counts[word])

#create a function called printTop20 with the parameter(counts) which is the dictionary
#create a variable called words that creates a list out of all of the keys from the dictionary
#here we reverse sort the values of the list
#on this line we only want to show the top 20 words with the highest values
#for each word in the list of words
        #print the word, then an equals sign and then how many times it has been shown in the text.
        



counts = countWords('mobypara.txt')
printTop20(counts)

