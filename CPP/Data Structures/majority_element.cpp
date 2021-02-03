#include <iostream>
#include <algorithm>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main() {
  vector <int> arr = {1, 2, 2, 4, 4, 4, 5, 3, 3};
  map <int, int> hash_map;
  for (int i = 0; i < arr.size(); i++) {
    if (hash_map.find(arr[i]) != hash_map.end()) {
      hash_map[arr[i]] = hash_map[arr[i]] + 1;
    }
    else{
      hash_map[arr[i]] = 1;
    }
  }
  int 
  for (int i = 1; i < arr.size(); i++) {
    cout<<arr[i]<<" "<<hash_map[arr[i]]<<"\n";
  }
}
