#include <iostream>
using namespace std;



//mission: 1행~level번째 행까지 level개의 말이
//이미 놓여 있고, 그 위치가 전역변수 cols에 저장되어 있다는 가정하에,
//그 상태에서 만들어 낼 수 있는 서로 다른 
//해의 개수를 카운트하여 반환한다.


#define N 4
int cols[N + 1];
bool promising(int level)
{
	for (int i = 1; i < level; i++) {

		if (cols[i] == cols[level])
			return false;
		else if (level - i == abs(cols[level] - cols[i]))
			return false;
	}
	return true;
}

int countWay = 0;

int queens(int level)
{
	if (!promising(level))
		return 0;

	if (level == N) {
		for (int i = 1; i <= N; i++)
			printf("%d ", cols[i]);
		printf("\n");
		return 1;
	}
	int count = 0;
	for (int i = 1; i <= N; i++) {
		cols[level + 1] = i;
		count += queens(level + 1);
	}
	return count;
}

int main() {
	printf("����� �� = %d ", queens(0));
}