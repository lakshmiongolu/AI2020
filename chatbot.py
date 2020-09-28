# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string
import random


def eliza():
    print('Hi, I am Eliza. How may I help you today?')
    while 1:
        sentence = input("> ")
        sentence = preprocess(sentence)
        # to check until it conjugates or not
        # sentence = keyword(sentence)
        # sentence = conjugate(sentence) // called inside keyword function
        # build reply and get reply are performed inside Keyword method itself.
        # to check emotions part
        sentence = emotions(sentence)
        print(sentence)


def preprocess(statement):
    result = ""
    for word in statement:
        for char in word:
            if char not in string.punctuation:
                result += word
                result = result.lower()
    return result


def keyword(statement):
    listofwords = statement.split()
    Flag = False
    keywords = ["can you", "can i", "you are", "youre", "i dont", "i feel", "why dont you", "why cant i", "are you",
                "i cant", "i am", "im", "you", "i want", "what", "how", "who", "where", "when", "why", "name",
                "cause",
                "sorry", "dream", "hello", "hi ", "maybe", "no", "your", "always", "think", "alike", "yes", "friend",
                "computer"]
    replies = {
        "-1": "What does that suggest to you? I see. I'm not sure I understand you fully. Come, come, elucidate your "
              "thoughts. Can you elaborate on that? That is quite interesting.",
        "0": "Don't you believe that I can *. Perhaps you would like me to be able to *. You want me to be able to *",
        "1": "Perhaps you don't want to *. Do you want to be able to *",
        "2": "What makes you think I am *. Does it please you to believe I am *. Perhaps you would like to be *. Do "
             "you sometimes wish you were *",
        "3": "What makes you think I am *. Does it please you to believe I am *. Perhaps you would like to be *. Do "
             "you sometimes wish you were *",
        "4": "Don't you really *. Why don't you *. Do you wish to be able to *. Does that trouble you?",
        "5": "Tell me more about such feelings. Do you often feel *. Do you enjoy feeling *",
        "6": "Do you really believe I don't *. Perhaps in good time I will *. Do you want me to *",
        "7": "Do you think you should be able to *. Why can't you *",
        "8": "Why are you interested in whether or not I am *. Would you prefer if I were not *. Perhaps in your "
             "fantasies I am *",
        "9": "How do you know you can't *. Have you tried?. Perhaps you can now *",
        "10": "Did you come to me because you are *. How long have you been *. Do you believe it is normal to be *. "
              "Do you enjoy being *",
        "11": "Did you come to me because you are *. How long have you been *. Do you believe it is normal to be *. "
              "Do you enjoy being *",
        "12": "We were discussing you, not me. Oh, I *. You're not really talking about me, are you?",
        "13": "What would it mean to you if you got *? Why do you want *? Suppose you got *, What if you never got *? "
              " I sometimes also want *",
        "14": "Why do you ask? Does that question interest you? What answer would please you the most? What do you "
              "think? Are such questions on your mind often? What is it that you really want to know? Have you "
              "asked anyone else? Have you asked such questions before? What else comes to your mind when you ask "
              "that?",
        "15": "Why do you ask? Does that question interest you? What answer would please you the most? What do you "
              "think? Are such questions on your mind often? What is it that you really want to know? Have you "
              "asked anyone else? Have you asked such questions before? What else comes to your mind when you ask "
              "that?",
        "16": "Why do you ask? Does that question interest you? What answer would please you the most? What do you "
              "think? Are such questions on your mind often? What is it that you really want to know? Have you "
              "asked anyone else? Have you asked such questions before? What else comes to your mind when you ask "
              "that?",
        "17": "Why do you ask? Does that question interest you? What answer would please you the most? What do you "
              "think? Are such questions on your mind often? What is it that you really want to know? Have you "
              "asked anyone else? Have you asked such questions before? What else comes to your mind when you ask "
              "that?",
        "18": "Why do you ask? Does that question interest you? What answer would please you the most? What do you "
              "think? Are such questions on your mind often? What is it that you really want to know? Have you "
              "asked anyone else? Have you asked such questions before? What else comes to your mind when you ask "
              "that?",
        "19": "Why do you ask? Does that question interest you? What answer would please you the most? What do you "
              "think? Are such questions on your mind often? What is it that you really want to know? Have you "
              "asked anyone else? Have you asked such questions before? What else comes to your mind when you ask "
              "that?",
        "20": "Names don't interest me. I don't care about names.  Please go on.",
        "21": "Is that the real reason? Don't any other reasons come to mind? Does that reason explain anything else? "
              "What other reasons might there be?",
        "22": "Please don't apologize! Apologies are not necessary.",
        "23": "What does that dream suggest to you? Do you dream often? What persons appear in your dreams? Are you "
              "disturbed by your dreams?",
        "24": "How do you do.  Please state your problem.",
        "25": "How do you do.  Please state your problem.",
        "26": "You don't seem quite certain. Why the uncertain tone? Can't you be more positive? You aren't sure? "
              "Don't you know?",
        "27": "Are you saying no just to be negative? You are being a bit negative. Why not? Are you sure? Why no?",
        "28": "Why are you concerned about my *? What about your own *",
        "29": "Can you think of a specific example? When? What are you thinking of? Really, always?",
        "30": "Do you really think so? But you are not sure you *. Do you doubt *",
        "31": "In what way? What resemblence do you see? What does the similarity suggest to you? What other "
              "connections do you see? Could there really be some connection? How?",
        "32": "You seem quite positive. Are you sure? I see. I understand.",
        "33": "Why do you bring up the topic of friends? Do your friends worry you? Do your friends pick on you? Are "
              "you sure you have any friends? Do you impose on your friends? Perhaps your love for your friends "
              "worries you.",
        "34": "Do computers worry you? Are you frightened by machines? Why do you mention computers? What do you "
              "think machines have to do with your problem? Don't you think computers can help people? What is it "
              "about machines that worries you? "
    }
    emotionkeywords = ["hate you", "dont like", "drowsy", "tired", "sleepy", "not interested", "dance", "sing", "happy",
                       "love", "care", "like you", "play ", "playing", "games", "vacation", "festivals"]

    for key in keywords:
        if Flag:
            break
        wordkeylist = key.split()
        for i in range(0, (len(listofwords) - len(wordkeylist) + 1)):
            element = listofwords[i:(i + len(wordkeylist))]
            if wordkeylist == element:
                remainingstring = " ".join(listofwords[i + len(wordkeylist):])
                conjugatedline = conjugate(remainingstring)
                joinkey = " ".join(wordkeylist)
                print(joinkey)
                index = str(keywords.index(joinkey))
                reply = replies[index]
                finalsentence = reply.replace("*", conjugatedline)
                Flag = True
                break

            else:
                finalsentence = replies['-1']
    return finalsentence


def conjugate(statement):
    conjugatepairs = {"are": "am",
                      "am": "are",
                      "were": "was",
                      "was": "were",
                      "you": "I",
                      "i": "you",
                      "your": "my",
                      "my": "your",
                      "ive": "you've",
                      "youve": "I've",
                      "im": "you're",
                      "youre": "I'm",
                      "me": "you"
                      }
    statementlist = statement.split()
    for eachword in statementlist:
        for eachkey in conjugatepairs.keys():
            if eachkey == eachword:
                # print("each key is ", eachkey)
                # print("eachword is ", eachword)
                value = conjugatepairs[eachkey]
                # print("value is ", value)
                statementlist[statementlist.index(eachword)] = value
                statement = " ".join(statementlist)
                # print(statement)
    return statement


def emotions(statement):
    listofwords = statement.split()
    Flag = False
    emotion = False
    finalsentence = ""
    keywords = ["can you", "can i", "you are", "youre", "i dont", "i feel", "why dont you", "why cant i", "are you",
                "i cant", "i am", "im", "you", "i want", "what", "how", "who", "where", "when", "why", "name",
                "cause",
                "sorry", "dream", "hello", "hi", "maybe", "no", "your", "always", "think", "alike", "yes", "friend",
                "computer"]
    replies = {
        "-1": "What does that suggest to you? I see. I'm not sure I understand you fully. Come, come, elucidate your "
              "thoughts. Can you elaborate on that? That is quite interesting.",
        "0": "Don't you believe that I can *. Perhaps you would like me to be able to *. You want me to be able to *",
        "1": "Perhaps you don't want to *. Do you want to be able to *",
        "2": "What makes you think I am *. Does it please you to believe I am *. Perhaps you would like to be *. Do "
             "you sometimes wish you were *",
        "3": "What makes you think I am *. Does it please you to believe I am *. Perhaps you would like to be *. Do "
             "you sometimes wish you were *",
        "4": "Don't you really *. Why don't you *. Do you wish to be able to *. Does that trouble you?",
        "5": "Tell me more about such feelings. Do you often feel *. Do you enjoy feeling *",
        "6": "Do you really believe I don't *. Perhaps in good time I will *. Do you want me to *",
        "7": "Do you think you should be able to *. Why can't you *",
        "8": "Why are you interested in whether or not I am *. Would you prefer if I were not *. Perhaps in your "
             "fantasies I am *",
        "9": "How do you know you can't *. Have you tried?. Perhaps you can now *",
        "10": "Did you come to me because you are *. How long have you been *. Do you believe it is normal to be *. "
              "Do you enjoy being *",
        "11": "Did you come to me because you are *. How long have you been *. Do you believe it is normal to be *. "
              "Do you enjoy being *",
        "12": "We were discussing you, not me. Oh, I *. You're not really talking about me, are you?",
        "13": "What would it mean to you if you got *? Why do you want *? Suppose you got *, What if you never got *? "
              " I sometimes also want *",
        "14": "Why do you ask? Does that question interest you? What answer would please you the most? What do you "
              "think? Are such questions on your mind often? What is it that you really want to know? Have you "
              "asked anyone else? Have you asked such questions before? What else comes to your mind when you ask "
              "that?",
        "15": "Why do you ask? Does that question interest you? What answer would please you the most? What do you "
              "think? Are such questions on your mind often? What is it that you really want to know? Have you "
              "asked anyone else? Have you asked such questions before? What else comes to your mind when you ask "
              "that?",
        "16": "Why do you ask? Does that question interest you? What answer would please you the most? What do you "
              "think? Are such questions on your mind often? What is it that you really want to know? Have you "
              "asked anyone else? Have you asked such questions before? What else comes to your mind when you ask "
              "that?",
        "17": "Why do you ask? Does that question interest you? What answer would please you the most? What do you "
              "think? Are such questions on your mind often? What is it that you really want to know? Have you "
              "asked anyone else? Have you asked such questions before? What else comes to your mind when you ask "
              "that?",
        "18": "Why do you ask? Does that question interest you? What answer would please you the most? What do you "
              "think? Are such questions on your mind often? What is it that you really want to know? Have you "
              "asked anyone else? Have you asked such questions before? What else comes to your mind when you ask "
              "that?",
        "19": "Why do you ask? Does that question interest you? What answer would please you the most? What do you "
              "think? Are such questions on your mind often? What is it that you really want to know? Have you "
              "asked anyone else? Have you asked such questions before? What else comes to your mind when you ask "
              "that?",
        "20": "Names don't interest me. I don't care about names.  Please go on.",
        "21": "Is that the real reason? Don't any other reasons come to mind? Does that reason explain anything else? "
              "What other reasons might there be?",
        "22": "Please don't apologize! Apologies are not necessary.",
        "23": "What does that dream suggest to you? Do you dream often? What persons appear in your dreams? Are you "
              "disturbed by your dreams?",
        "24": "How do you do.  Please state your problem.",
        "25": "How do you do.  Please state your problem.",
        "26": "You don't seem quite certain. Why the uncertain tone? Can't you be more positive? You aren't sure? "
              "Don't you know?",
        "27": "Are you saying no just to be negative? You are being a bit negative. Why not? Are you sure? Why no?",
        "28": "Why are you concerned about my *? What about your own *",
        "29": "Can you think of a specific example? When? What are you thinking of? Really, always?",
        "30": "Do you really think so? But you are not sure you *. Do you doubt *",
        "31": "In what way? What resemblence do you see? What does the similarity suggest to you? What other "
              "connections do you see? Could there really be some connection? How?",
        "32": "You seem quite positive. Are you sure? I see. I understand.",
        "33": "Why do you bring up the topic of friends? Do your friends worry you? Do your friends pick on you? Are "
              "you sure you have any friends? Do you impose on your friends? Perhaps your love for your friends "
              "worries you.",
        "34": "Do computers worry you? Are you frightened by machines? Why do you mention computers? What do you "
              "think machines have to do with your problem? Don't you think computers can help people? What is it "
              "about machines that worries you? "
    }

    emotion = isemotion(statement)
    print(emotion)
    for key in keywords:
        if Flag:
            break
        wordkeylist = key.split()
        for i in range(0, (len(listofwords) - len(wordkeylist) + 1)):
            element = listofwords[i:(i + len(wordkeylist))]

            if wordkeylist == element and not emotion:
                emotion = False
                remainingstring = " ".join(listofwords[i + len(wordkeylist):])
                conjugatedline = conjugate(remainingstring)
                joinkey = " ".join(wordkeylist)
                index = str(keywords.index(joinkey))
                reply = replies[index]
                finalsentence = reply.replace("*", conjugatedline)
                Flag = True
                break
            elif emotion:
                # print("Debuuuuuuuuuuuuuuug")
                finalsentence = checkforemotion(statement)
                Flag = True
                break
            else:
                finalsentence = replies['-1']
    return finalsentence


def isemotion(statement):
    print("insiiiiiiiiiiiiiiiiiiiide")
    emotiondetected = ""
    listofwords = statement.split()
    emotionkeywords = ["hate you", "dont like", "drowsy", "tired", "sleepy", "not interested", "dance", "sing", "happy",
                       "love", "care", "like", "play ", "playing", "games", "vacation", "festivals"]

    for emotion in emotionkeywords:
        emotionkeylist = emotion.split()
        for i in range(0, (len(listofwords) - len(emotionkeylist) + 1)):
            element = listofwords[i:(i + len(emotionkeylist))]
            if emotionkeylist == element:
                print("emotionkeeeeeey ", element)
                print("----------", emotionkeylist)
                emotiondetected = True
                break
            else:
                emotiondetected = False
    print(emotiondetected)
    return emotiondetected


def checkforemotion(statement):
    emotionkeywords = ["hate you", "dont like", "drowsy", "tired", "sleepy", "not interested", "dance", "sing", "happy",
                       "love", "care", "like", "play ", "playing", "games", "vacation", "festivals"]
    emotionreplies = {
        "0": "May I know the reason for hating me.",
        "1": "Why do you feel like you dont like *",
        "2": "Get some rest and you will be fine",
        "3": "Get some rest and you will be fine",
        "4": "Get some rest and you will be fine",
        "5": "Try again. May be it will interest you this time",
        "6": "I love to dance. Why do you feel like dancing?",
        "7": "I love singing. Why do you feel like singing?",
        "8": "Great! What made you feel so happy today?",
        "9": "I love * too",
        "10": "Why do you care them the most?",
        "11": "Why do you feel like you like *",
        "12": "Really? I like to play * as well",
        "13": "How many hours can you keep on playing?",
        "14": "Great! what type of games you like the most? Indoor or outdoor?",
        "15": "What is your favourite vacation spot? Why do you like it?",
        "16": "What is the most recent festival you celebrated? Do you celebrate every festival?"
    }
    listofwords = statement.split()
    for emotion in emotionkeywords:
        emotionkeylist = emotion.split()
        for i in range(0, (len(listofwords) - len(emotionkeylist) + 1)):
            element = listofwords[i:(i + len(emotionkeylist))]
            if emotionkeylist == element:
                emotion = True
                remainingstring = " ".join(listofwords[i + len(emotionkeylist):])
                conjugatedline = conjugate(remainingstring)
                joinkey = " ".join(emotionkeylist)
                indexkey = str(emotionkeywords.index(joinkey))
                reply = emotionreplies[indexkey]
                finalsentence = reply.replace("*", conjugatedline)
    return finalsentence


def main():
    eliza()


main()
