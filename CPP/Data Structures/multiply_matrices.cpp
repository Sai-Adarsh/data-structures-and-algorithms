#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main() {
  vector <vector<int>> arr1 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
  vector <vector<int>> arr2 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
  vector <vector<int>> arr3;
  for (int i = 0; i < arr1.size(); i++){
    vector <int> temp;
    for (int j = 0; j < arr1[0].size(); j++) {
      temp.push_back(arr1[i][j] * arr2[i][j]);
    }
    arr3.push_back(temp);
  }
  for (int i = 0; i < arr1.size(); i++){
    for (int j = 0; j < arr1[0].size(); j++) {
      cout<<arr3[i][j]<<" ";
    }
    cout<<"\n";
  }
}
