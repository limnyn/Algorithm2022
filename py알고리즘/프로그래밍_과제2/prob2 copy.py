#201812177이문현 2번
# 이번에는 1번과 동일한 사전파일을 읽어서 선형적인 자료구조로 저장한다.
# 예를 들어 배열(array), vector, arraylist, list(python) 등 각 프로그래밍 언어가 제공허는 어떤 자료구조를 이용해도 무방하다.
# 그런 다음 1번의 (b)에서 한 일을 이 자료구조에 대해서 수행하고 걸린 시간을 측정하여 출력한다.


import time
import re

#입력1, 각 단어 품사 설명 추출 후 튜플로 묶어 리스트에 삽입
wordList=[]
f = open('py알고리즘\프로그래밍_과제2\shuffled_dict.txt', 'r',encoding='utf_8')
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

#입력2, 삭제할 단어 한줄씩 리스트에 삽입
start_time = time.perf_counter()

delList=[]
f2 = open('py알고리즘\프로그래밍_과제2\search_words.txt', 'r',encoding='utf_8')
while True:
    line = f2.readline().strip()
    if not line or line == '\n':
        break
    delList.append(line)


#for문을 돌며 각 리스트 안의 단어들을 search해 삭제한다.
for delWord in delList:
        for word in wordList:
            if word[0] == delWord:
                del wordList[wordList.index(word)]
                break
end_time = time.perf_counter()
print('코드 실행 시간: %20ds' % (end_time - start_time))
f2.close()  
#search_words에 데이터 오류가 있습니다. 
#숙어(관용어)가 사전에 등재될 때 -이나 \s 등으로 여러단어가 묶여있는데 앞부분만 저장되어있습니다
#"James's", "Spider's", "Hobson's", 'Brunswick', "Beggar's", "Lion's", 'Comet-', 'Rome', 'Lonis' 처럼
# Lion's foot () A composite plant of the genus Prenanthes, of which several species are found in the United States.
# 같은 경우 search_words에 Lion's로만 저장되어 있습니다.





# #201812177이문현 2번 딕셔너리 사용 코드 
# # 이번에는 1번과 동일한 사전파일을 읽어서 선형적인 자료구조로 저장한다.
# # 예를 들어 배열(array), vector, arraylist, list(python) 등 각 프로그래밍 언어가 제공허는 어떤 자료구조를 이용해도 무방하다.
# # 그런 다음 1번의 (b)에서 한 일을 이 자료구조에 대해서 수행하고 걸린 시간을 측정하여 출력한다.


# import time
# import re

# #입력1, 각 단어 추출 후 bst에 삽입
# wordDict={}
# f = open('py알고리즘\프로그래밍_과제2\shuffled_dict.txt', 'r',encoding='utf_8')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     word = re.sub('\s\(.*\n', '', line)
#     word.strip()
#     wordExpl = re.sub('.*\s\((.*?)\)\s', '', line)
#     wordExpl = re.sub('\n',"",wordExpl)
#     wordClass = line.replace(wordExpl,"")
#     wordClass = wordClass.replace(word, "")
#     wordClass = wordClass.replace(" ", "")
#     wordClass = wordClass.replace("\n", "")
#     wordClass = wordClass.replace("(", "").replace(")","")
#     wordset=(wordClass,wordExpl)
#     wordDict[word]=wordset

# f.close()
# #입력2, 삭제할 단어 한줄씩 리스트에 삽입
# start_time = time.perf_counter_ns()
# delList=[]
# f2 = open('py알고리즘\프로그래밍_과제2\search_words.txt', 'r',encoding='utf_8')
# while True:
#     line = f2.readline().strip()
#     if not line:
#         break
#     delList.append(line)
# f2.close()  

# #for문을 돌며 각 리스트 안의 단어들을 search해 삭제한다.
# for delWord in delList:
#     #search_words 파일에 데이터 오류가 있습니다. 
#     try:
#         del wordDict[delWord]
#     except:
#         continue
# end_time = time.perf_counter_ns()

# print('코드 실행 시간: %20dns' % (end_time - start_time))
