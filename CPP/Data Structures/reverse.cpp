#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
class Solution {
	public:
		void returnReverse(int &arr, int n) {
			return reverse(arr, arr + n);
		}	
};

int main() {
	Solution Obj;
	int arr[] = {1, 2, 3, 4, 5};
	int n = sizeof(arr) / sizeof(arr[0]);
	Obj.returnReverse(arr, n);
	for (int i = 0; i < 5; i++) {
		cout<<arr[i];
	}
}
