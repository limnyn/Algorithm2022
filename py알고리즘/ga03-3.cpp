// # 다음은 N-queen 문제를 푸는 순환함수이다.
// # 이 함수를 변형하여 N-queen 문제의 서로 다른 해의 개수를 구하는 함수를 작성하라.
// # promising 함수는 작성할 필요가 없다.


#include <iostream>
using namespace std;

#define N 4
int cols[N+1];
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

bool queens(int level)
{
	if (!promising(level))
		return false;

	else if (level == N) {
		for (int i = 1; i <= N; i++)
			printf("%d ", cols[i]);
		printf("\n");
		countWay++;
		
		if (cols[1] == N)
			return true;
		else
			return false;
	}

	for (int i = 1; i <= N; i++) {
		cols[level + 1] = i;
		if (queens(level + 1))
			return true;
	}
	return false;

}

int main() {
	queens(0);
	
	printf("경우의 수 = %d ", countWay);
}
