# Blog Tagger 1.1.0
# 6 May 2016
# Tagging engine for blog posts

#############################################################################

# enter filename or quit (with default)
fname = raw_input('Enter filename or Q to quit: ')
if fname.lower() == 'q' :
    quit()
elif len(fname) == 0 :         # default on enter
    fname = 'romeo.txt'        # default on enter

# open file or return error message
try:
    fhand = open(fname)
except:
    print 'Filename not found:', fname
    print '++Goodbye++'
    quit()


#############################################################################

# excluded words list
excluded = ['and/or', 'just', 'something', 'wants', 'little', 'looking', 'someone', 'take', 'which', 'various', 'being', 'often', 'maybe', 'may', 'similar', 'up', 'hear', 'already', 'others', 'see', 'look', 'mean', 'good', 'had', 'such', 'so', 'amazing', 'other', 'these', 'along', 'best', 'even', 'here', 'very', 'whilst', 'mostly', 'less', 'also', 'always', 'how', 'means', 'whose', 'all', 'e', 'g', 'via', 'towards', 'across', 'more', 'has','way', 'ways', 'taken', 'into', 'would', 'could', 'should', 'will', 'about', 'only', 'truly', 'will', 'wider', 'mainly', 'overall', 'behind', 'least', 'really', 'both', 'great', 'lot', 'used', 'over', 'want', 'well', 'etc', 'fairly', 'around', 'an', 'have', 'this','that','what','who','as','like','our','us','be','it','to','our','the','on','we','do','can','a','is','are','was','were','or','and','of','for','from','you','your','me','my','we','our','they','their','us','them','at','out','to','this','that','the','those','some','any','no','none','on','within']
excluded1 = ["get","by","where","while","but","its","when","while","make","use","from","in","else","with","without","if","not"]


#############################################################################

# add user-defined excluded words to csv file (using while True loop with break)
inp = raw_input('\n'+'Specify/save exclusions to a CSV file (Y/N): ')
if inp.lower() == 'y' :
    outname = raw_input('Enter output filename: ')
    outname = outname + '.txt'
    print 'Filename:', outname
    fout = open(outname, 'w')
    while True :
        inp = raw_input('\n'+'Specify word or "Done": ')
        if inp.lower() == 'done' : break
        fout.write(inp)
        fout.write(',')
    fout.close()
else :
    print '\n', 'Using existing exclusions only'


#############################################################################

# read file to text
text = fhand.read()

# user-defined: punctuation check
punc = raw_input('\n'+'Does the file contain punctuation? (Y/N): ')
if punc.lower() == 'y' :
    text = text.lower()
    text = text.replace(',',' ')
    text = text.replace('.',' ')
    text = text.replace("(",' ')
    text = text.replace(")",' ')
    text = text.replace("'",' ')
    text = text.replace(':',' ')
elif punc.lower() == 'n' or len(punc) == 0 :
    text = text.lower()
else :
    print 'Entry not recognised:', punc
    print '++Goodbye++'
    quit()

# split all words in file into a list
wordlist = text.split()

# user-defined: excluded words check
excl = raw_input('\n'+'Do you want to exclude small words? (Y/N): ')
if len(excl) == 0 : excl = 'y'

# user-defined exclusions
udfname = raw_input('\n'+'User-defined exclusions? (Enter filename or "None"): ')
if len(udfname) == 0 : udfname = 'exclude101p4.txt'

# open file or return error message
try:
    udfhand = open(udfname)
    udtext = udfhand.read()
    udtext = udtext.lower()
    udexcluded = udtext.split(',')
    print '\n', 'User-defined exclusions:', udexcluded
except:
    print 'Filename not found:', udfname
    print 'Continuing without user-defined exclusions'

# counting all words into a dictionary
words = dict()
for word in wordlist :
    if udfname.lower() == 'none' :
        if excl.lower() == 'y' :
            if word in excluded : continue
            if word in excluded1 : continue
            words[word] = words.get(word,0) + 1
        else :
             words[word] = words.get(word,0) + 1
    elif udfname.lower() <> 'none' :
        if excl.lower() == 'y' :
            if word in excluded : continue
            if word in excluded1 : continue
            if word in udexcluded : continue
            words[word] = words.get(word,0) + 1
        else :
             words[word] = words.get(word,0) + 1


#############################################################################

# list in count,word order; sort by descending count
templist = list()
for word,count in words.items() :
    templist.append( (count,word) )
templist.sort(reverse=True)


#############################################################################

# user-defined: top n words or a for all
n = raw_input('\n'+'Enter a number for "Top n words", or A for ALL: ')
if len(n) == 0 : n = 10
if n.lower() == 'a' : n = len(templist)

try:
    n = int(n)
except:
    print 'Entry not recognised:', n
    print '++Goodbye++'
    quit()
### IMPROVEMENT: RETURN TO RAW_INPUT INSTEAD OF QUIT()

if n == len(templist) : print '\n', 'All words and their counts:'
else : print '\n', 'Top', n, 'words and their counts:'
for count,word in templist[:n] :
    print word, count


#############################################################################

# specify/save tags list
inp = raw_input('\n'+'Specify/save tags to CSV file? (Y/N): ')
if len(inp) == 0 : inp = 'y'
if inp.lower() == 'y' :
    tagname = raw_input('Enter tags filename: ')
    tagname = tagname + '.txt'
    print 'Filename:', tagname
    taghand = open(tagname, 'w')
    for count,word in templist[:n] :
        add = raw_input('Add '+word+' (Y/N)')
        if add.lower() == 'y' :
            print 'Adding', word
            taghand.write(word)
            taghand.write(',')
    taghand.close()
    print '\n', 'File saved:', tagname
    print '++Goodbye++'
else :
    print '\n', '++Goodbye++'


