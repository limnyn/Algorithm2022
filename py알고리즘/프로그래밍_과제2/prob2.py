#201812177이문현 2번
# 이번에는 1번과 동일한 사전파일을 읽어서 선형적인 자료구조로 저장한다.
# 예를 들어 배열(array), vector, arraylist, list(python) 등 각 프로그래밍 언어가 제공허는 어떤 자료구조를 이용해도 무방하다.
# 그런 다음 1번의 (b)에서 한 일을 이 자료구조에 대해서 수행하고 걸린 시간을 측정하여 출력한다.


import time
import re

#입력1, 각 단어 추출 후 bst에 삽입
wordList=[]
f = open('py알고리즘\프로그래밍_과제2\shuffled_dict.txt', 'r',encoding='utf_8')
while True:
    line = f.readline()
    if not line:
        break
    text_filtered = re.sub('\s\(.*\n', '', line)
    text_filtered.strip()
    wordList.append(text_filtered) 
f.close()

#입력2, 삭제할 단어 한줄씩 리스트에 삽입
start_time = time.perf_counter_ns()
delList=[]
f2 = open('py알고리즘\프로그래밍_과제2\search_words.txt', 'r',encoding='utf_8')
while True:
    line = f2.readline()
    if not line:
        break
    text_filtered = re.sub('\n', '', line)
    text_filtered.strip()
    delList.append(text_filtered)
f2.close()  

#for문을 돌며 각 리스트 안의 단어들을 search해 삭제한다.
for delWord in delList:
    #search_words 파일에 데이터 오류가 있습니다. 
    try:
        wordList.remove(delWord)
    except:
        continue
end_time = time.perf_counter_ns()

print('코드 실행 시간: %20dns' % (end_time - start_time))
#search_words에 데이터 오류가 있습니다. 
#숙어(관용어)가 사전에 등재될 때 -이나 \s 등으로 여러단어가 묶여있는데 앞부분만 저장되어있습니다
#"James's", "Spider's", "Hobson's", 'Brunswick', "Beggar's", "Lion's", 'Comet-', 'Rome', 'Lonis' 처럼
# Lion's foot () A composite plant of the genus Prenanthes, of which several species are found in the United States.
# 같은 경우 search_words에 Lion's로만 저장되어 있습니다.