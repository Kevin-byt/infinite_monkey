import random, string, difflib, time

i=0

def generate():
    length = 28
    letters = string.ascii_lowercase
    gen_string = ''.join(random.choice(letters + ' ') for i in range(length))
    print(gen_string)
    return gen_string

def score():
    goal = "me thinks it is like a weasel"
    print(goal)
    global generated
    generated = generate()
   # generated = "me thinks it iw like a seasel"
    #print(generated)
    score = difflib.SequenceMatcher(None, goal, generated).ratio()
    print(score)
    return(score)

oldScore = 0
bestgenString = " "
 
while True:
    scor = score()
    if scor > oldScore:
        bestScore = scor
        bestgenString = generated
        oldScore = scor
    if i < 1000:
        print(i)
        i = i+1

    else:
        print("1000 cycles complete")
        print("Best string was :", bestgenString, " with a score of : ", bestScore)
        i = 0
        time.sleep(5)
