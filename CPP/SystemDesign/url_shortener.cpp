#include <iostream>
#include <vector>
#include <algorithm>
#include <bits/stdc++.h>
#include <stdlib.h>

using namespace std;

class urlShortner {
  public:
    void shortenThat(map <int, string> &urlDatabase, string &url) {
      int temp = rand();
      urlDatabase[temp] = url;
      string return_string = urlDatabase[temp];
      cout<<"String shortened\n";
    }
};

void print(map <int, string> &urlDatabase) {
  for (auto i = urlDatabase.begin(); i != urlDatabase.end(); i++) {
    cout<<i->first<<" "<<i->second<<"\n";
  }
}

int main() {
  urlShortner Obj;
  string url = "https://leetcode.com/sai-adarsh/";
  map <int, string> urlDatabase;
  Obj.shortenThat(urlDatabase, url);
  print(urlDatabase);
  int shortenedUrl;
  cout<<"Enter shortenedUrl: \n";
  cin>>shortenedUrl;
  cout<<"Expanded URL is: "<<urlDatabase[shortenedUrl]<<"\n";
}
