#include <iostream>
#include <algorithm>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main() {
  vector <int> result = {1, 2, 3, 4};
  int res = 0;
  for (int i = 0; i < 4; i++) {
    res += result[i];
  }
  cout<<"Im here: "<<res;
}
