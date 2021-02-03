#include <iostream>
#include <vector>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9};
    int res = 0;
    int length = sizeof(arr) / sizeof(arr[0]);
    int last_good_index = length - 1;
    for (int i = length - 2; i >= 0; i--) {
      if (arr[i] + i <= last_good_index) {
        last_good_index = i;
      }
    }
    cout<<(last_good_index == 0 ? "true" : "false");
}
