#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
class Solution {
	public:
		int* returnCopy(int *arr) {
			int newArr[5];
			copy_n(arr, 5, newArr);
			return newArr;
		}
};

int main() {
	Solution Obj;
	int arr[] = {1, 2, 3, 4, 5};
}
