#include <iostream>
using namespace std;


//mission: 1��~level��° ����� level���� ����
//�̹� ���� �ְ�, �� ��ġ�� �������� cols�� ����Ǿ� �ִٴ� �����Ͽ�,
//�� ���¿��� ����� �� �� �ִ� ���� �ٸ� 
//���� ������ ī��Ʈ�Ͽ� ��ȯ�Ѵ�.


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