#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
  public:
    float getFloor(float a);
    float getCeil(float a);
};

float Solution::getFloor(float a) {
  return floor(a);
}

float Solution::getCeil(float a) {
  return ceil(a);
}

int main() {
  Solution obj;
  int a = 5.5;
  cout<<obj.getFloor(a);
  cout<<obj.getCeil(a);
}
