import random

'''
    字彙訓練器:
    使用集合
    {word: {0: <definition>, 1: <part of speech>}
    
    填滿該單元單字
'''

words = { # edit this table
    "word" : {0: ["definition"], 1: "pos."},
}

class modes:
    def EtoC():
        corrects = 0
        answered = 0
        wordsAnsed = []
            
        while len(wordsAnsed) < len(words):
            word = random.choice(list(words))
            
            if word in wordsAnsed:
                continue
            
            wordsAnsed.append(word)
            ansWord = input(f"{word}: ")
            answered += 1
         
            if ansWord in words[word][0]:
                print("答對了!")
                corrects += 1
            else:
                print(f"答錯了... 中文意思有: {'；'.join(words[word][0])}")
                continue
        
        print(f"""
        ---總單字量: {len(words)}
        ---總答對題數: {corrects}
        ---總答題數: {answered}
        ---正確率: {round(corrects*100/answered, 2)}%
        """) 
        
    def CtoE():
        corrects = 0
        answered = 0
        wordsAnsed = []
            
        while len(wordsAnsed) < len(words):
            word = random.choice(list(words))
            
            if word in wordsAnsed:
                continue
            
            wordsAnsed.append(word)
            ansWord = input(f"{'；'.join(words[word][0])} ({words[word][1]}): ")
            answered += 1
            
            if str.lower(ansWord) == word:
                print("答對了!")
                corrects += 1
            else:
                print(f"答錯了... 英文是: {word}")
                continue
        print(f"""
        ---總單字量: {len(words)}
        ---總答對率: {corrects}
        ---總答題數: {answered}
        ---正確率: {round(corrects*100/answered, 2)}%
        """) 

def ques():
    print("\t這個標題也可以改\t") # here title
    mode = int(input("簡介(0)；中翻英(1)；英翻中(2)；單字表(3) --> "))
    
    if mode == 0:
        print("聊發明的東西，你可以自己加入新的補充單字\n英翻中的時候中文意思字要全部一樣，答對其中一個意思即可\n中翻英大小寫不計。")
    elif mode == 1:
        modes.CtoE()
    elif mode == 2:
        modes.EtoC()
    elif mode == 3:
        print(f"""
        ---總單字量: {len(words)}
        """)
        for i in words:
            print(f"{i}({words[i][1]}): {'；'.join(words[i][0])}")
    else:
        ques()
        
ques()
