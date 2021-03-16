#include <iostream>
#include <vector>
#include <algorithm>
#include <bits/stdc++.h>
#include <string>

using namespace std;

class Music {
    public:
        map <string, string> musicDatabase = {{"Music1", "MovieOne"}, {"Music2", "MovieTwo"}, {"Oru Manam", "MovieOne"}};
        vector <string> getAlbumName(string &inputAlbum) {
            //... 
            vector <string> returnVector;
            for (auto i = musicDatabase.begin(); i != musicDatabase.end(); i++) {
            	if (i->second == inputAlbum) {
            		returnVector.push_back(i->first);
				}
			}
            return returnVector;
        }
};

class User : public Music {
    public:
        string getMusic () {
            Music *Obj = new Music();
            string inputAlbum = "MovieOne";
			vector <string> res;
			res = Obj->getAlbumName(inputAlbum);
			for (auto i = res.begin(); i != res.end(); i++) {
				cout<<*i<<"\n";	
			}
        }
};

int main() {
    User *userObj = new User();
    cout<<userObj->getMusic();
}
