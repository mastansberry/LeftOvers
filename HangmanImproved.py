
def hangman(guess,secret):
    letters = ''
    found = False
    for s in secret:
        for g in guess:
            print (g,":",s)
            if g == s :
                found = True
            if s == ' ':
                found = True
        if found == True:
            letters += s
        else:
            letters += '-'
        found = False
    print (letters)
