#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  vector <int> arr = {1, 24, 45, 2, 3, 43, 5};
  int result = *max_element(arr.begin(), arr.end());
  cout<<result;
}
