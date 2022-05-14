import re
wordList = []
line='Anti () A prefix meaning against, opposite or opposed to, contrary, or in place of; -- used in composition in many English words. It is often shortened to ant-; as, antacid, antarctic.\n'
word = re.sub('\s\(.*\n', '', line)
word.strip()
wordExpl = re.sub('.*\s\((.*?)\)\s', '', line)
wordExpl = re.sub('\n',"",wordExpl)
wordClass = line.replace(wordExpl,"")
wordClass = wordClass.replace(word, "")
wordClass = wordClass.replace(" ", "")
wordClass = wordClass.replace("\n", "")
wordClass = wordClass.replace("(", "").replace(")","")
# wordExpl
print(word)
print(wordClass)
print(wordExpl)


wordList=[]
f = open('py알고리즘\프로그래밍_과제2\sd.txt', 'r',encoding='utf_8')
while True:
    line = f.readline()
    if not line or line == '\n':
        break
    word = re.sub('\s\(.*\n', '', line)
    word.strip()
    wordExpl = re.sub('.*\s\((.*?)\)\s', '', line)
    wordExpl = re.sub('\n',"",wordExpl)
    wordClass = line.replace(wordExpl,"")
    wordClass = wordClass.replace(word, "")
    wordClass = wordClass.replace(" ", "")
    wordClass = wordClass.replace("\n", "")
    wordClass = wordClass.replace("(", "").replace(")","")
    wordset=(word,wordClass,wordExpl)
    wordList.append(wordset)

f.close()
wordList.sort(key=lambda x:x[0])
print(wordList)
delList=['Shellfish','Archaeological']

for delWord in delList:
    #search_words 파일에 데이터 오류가 있습니다. 
    try:
        for word in wordList:
            if word[0] == delWord:
                del wordList[wordList.index(word)]
                

    except:
        print('ERR')
        continue
print('Non ERr')
print(wordList)
# import re
# wordList = []
# line='Anti () A prefix meaning against, opposite or opposed to, contrary, or in place of; -- used in composition in many English words. It is often shortened to ant-; as, antacid, antarctic.\n'
# word = re.sub('\s\(.*\n', '', line)
# word.strip()
# pat = re.compile('\((.*?)\)\s')
# tmp = pat.findall(line)
# wordClass= tmp[0]

# wordExpl = re.sub('.*\s\((.*?)\)\s', '', line)
# wordExpl = re.sub('\n',"",wordExpl)

# # wordExpl
# print(word)
# print(wordClass)
# print(wordExpl)


# wordDict={}
# f = open('py알고리즘\프로그래밍_과제2\shuffled_dict.txt', 'r',encoding='utf_8')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     word = re.sub('\s\(.*\n', '', line)
#     word.strip()
#     pat = re.compile('\((.*?)\)\s')
#     wordClass= pat.findall(line)
#     # wordClass=tmp[0]
#     wordExpl = re.sub('.*\s\((.*?)\)\s', '', line)
#     wordExpl = re.sub('\n',"",wordExpl)
#     wordset=(wordClass,wordExpl)
#     wordDict[word]=wordset

# f.close()