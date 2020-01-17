import random
def from_file(file):
    m = ""
    with open(file,'r') as f:
        m+=f.readline()
        m+=" "
    m.rstrip(" ")
    return(m)

def sequence(word_length):
    characters=[chr(i) for i in range(32,123)]
    random.shuffle(characters)
    word = "".join(characters[:word_length])
    return word


def paragraph_generator():
    no_of_words = random.randint(1000,1500)
    para = ""
    for i in range(no_of_words):
        word_length = random.randint(1,10)
        word = sequence(word_length)
        para+=word
        para+=" "
##        para = para[2:]
    return para.encode('utf-8')


print(paragraph_generator())
