입력 = 사전파일
구조 = 단어\t설명

1. 딕셔너리 생성
2. 문장에서 단어 읽고 노드 생성, 딕셔너리에 삽입 (단어:next노드(초기값 null))
3. 2번문장 eof까지 반복
->단어 목록 생성됨


출력
1. 그래프의 정점의 개수와 에지의 개수 출력
2. 최대 차수를 가지는 정점을 찾고 단어와 차수 출력
3. 가장 큰 연결요소를 찾고, 연결요소의 크기를 출력
4. 하나의 단어 x와 탐색깊이k 를 입력받고 단어 x로부터 떨어진 거리가 k 이하인 모든 단어를 찾아 한줄에 하나씩 출력한다.
    이때 단어 x 자체를 맨 처음 출력하고, 나머지 단어들의 출력 순서는 마음대로 한다.
    