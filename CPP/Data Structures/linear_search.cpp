#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
  public:
    string givesPresent(vector <int> &arr, int &target) {
      for(int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) {
          return "true";
        }
      }
      return "false";
    }
};

int main() {
  Solution obj;
  vector<int> arr = {1, 2, 34, 5, 6, 3, 10, 2};
  int target = 3;
  cout<<obj.givesPresent(arr, target);
}
