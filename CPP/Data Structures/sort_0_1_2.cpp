#include <iostream>
#include <algorithm>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

class Solution {
  public:
    void letsGetItSorted(vector <int> &arr) {
      sort(arr.begin(), arr.end());
    }
};

int main() {
  vector <int> arr = {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1};
  Solution obj;
  obj.letsGetItSorted(arr);
  for (int i = 0; i < arr.size(); i++) {
    cout<<arr[i];
  }
}
