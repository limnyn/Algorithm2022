#include <iostream>
#include <stdlib.h>
using namespace std;


int N = 0;

int* cols;
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
		/*for (int i = 1; i <= N; i++)
			printf("%d ", cols[i]);
		printf("\n");*/
		countWay++;
		
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
	cin >> N;
	cols = (int*)malloc(sizeof(int) * (N + 1));

	queens(0);
	cout << countWay;
	free(cols);
}