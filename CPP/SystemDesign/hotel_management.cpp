#include <iostream>
#include <vector>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

class Admin {
	public:
		void addRoom(vector <int> &rooms, int roomID){
			if (find(rooms.begin(), rooms.end(), roomID) != rooms.end()) {
				cout<<"Already in rooms\n";
			}
			else {
				rooms.push_back(roomID);
				cout<"Room pushed\n";	
			}
		}
		void editRoom(vector <int> &rooms, int roomID, int newRoomID) {
			auto it = find(rooms.begin(), rooms.end(), roomID);
			if (it != rooms.end()) {
				int index = it - rooms.begin();
				rooms[index] = newRoomID;
			}
			else {
				cout<<"RoomID not found\n";
			}
		}
		void deleteRoom(vector <int> &rooms, int roomID) {
			auto it = find(rooms.begin(), rooms.end(), roomID);
			if (it != rooms.end()) {
				rooms.erase(it);
				cout<<"Room "<<roomID<<" deleted\n";
			}
			else {
				cout<<"No such rooms\n";
			}
		}
};

class Receptionist {
	public:
		void searchRoom(vector <int> &rooms, int roomID) {
			if (find(rooms.begin(), rooms.end(), roomID) != rooms.end()) {
				cout<<"At reception, Found room ID "<<roomID<<"\n";
			}
			else {
				cout<<"Room ID not found\n";
			}
		}
		
		void bookRoom(vector<int> &rooms, int roomID, map<string, int> &guest, string guestName) {
			if (find(rooms.begin(), rooms.end(), roomID) != rooms.end()) {
				guest[guestName] = roomID;
				cout<<guest[guestName]<<" booked for "<<guestName<<"\n";
			}
			else {
				cout<<"roomID not found\n";
			}
		}
		
		void cancelRoom(map <string, int> &guest, string guestName) {
			if (guest.find(guestName) != guest.end()){
				guest.erase(guestName);
				cout<<guestName<<" deleted\n";
			}
			else {
				cout<<guestName<<" not booked\n";
			}
		}
		void checkIn(map <string, int> guest, map <string, vector<int>> logBook, string guestName, int time) {
			// your code here
			if (guest.find(guestName) != guest.end()) {
				logBook[guestName].push_back(time);
				cout<<"log added to "<<guestName<<" "<<logBook[guestName][0]<<"\n";
			}
			else {
				cout<<guestName<<" not found in guest list\n";
			}
		}
		void checkOut(map <string, int> guest, map <string, vector<int>> logBook, string guestName, int time) {
			// your code here
			if (guest.find(guestName) != guest.end()) {
				logBook[guestName].push_back(time);
				cout<<"log added to "<<guestName<<" "<<logBook[guestName][0]<<"\n";
			}
			else {
				cout<<guestName<<" not found in guest list\n";
			}
		}
};

class Guest : public Receptionist {
	public:
		// your code here
};

class HouseKeeping {
	public:
		void addTimeToRoom(vector <int> &rooms, map <int, vector <int>> &houseKeepingLog, int roomID, int time) {
			if (find(rooms.begin(), rooms.end(), roomID) != rooms.end()) {
				houseKeepingLog[roomID].push_back(time);
				cout<<roomID<<" was cleaned on "<<time<<"\n";
			}			
		}
};

void print(vector <int> &rooms) {
	for (int i = 0; i < rooms.size(); i++) {
		cout<<rooms[i]<<" ";
	}
	cout<<"\n";
}

void printGuest(map <string, int> &guest) {
	for (auto i = guest.begin(); i != guest.end(); i++) {
		cout<<"guest HashMap "<<i->first<<" "<<i->second;
	}
	cout<<"\n";
}

void printLog(map <string, vector <int>> &logBook) {
	for (auto i = logBook.begin(); i != logBook.end(); i++) {
		cout<<"logbook HashMap "<<i->first<<" "<<i->second[0];
	}
	cout<<"\n";
}

void printHouseKeeping(map <int, vector <int>> &houseKeepingLog) {
	int x = 0;
	for (x = 0; x < 3; x++) {
		for (auto i = houseKeepingLog.begin(); i != houseKeepingLog.end(); i++) {
			cout<<"houseKeepingLog HashMap roomID"<<i->first<<" "<<i->second[x]<<"\n";
		}	
	}
}

int main() {
	vector <int> rooms = {100, 101, 102, 103, 104, 105};
	map <string, int> guest;
	map <string, vector<int>> logBook;
	map <int, vector<int>> houseKeepingLog;
	Admin Obj;
	Guest G;
	Receptionist R;
	HouseKeeping H;
	cout<<"Admin Add 10\n";
	Obj.addRoom(rooms, 10);
	print(rooms);
	cout<<"Admin Edit 10 as 20\n";
	Obj.editRoom(rooms, 10, 20);
	print(rooms);
	cout<<"Admin Delete 20\n";
	Obj.deleteRoom(rooms, 20);
	print(rooms);
	G.searchRoom(rooms, 105);
	G.bookRoom(rooms, 105, guest, "Sai Adarsh");
	printGuest(guest);
	G.cancelRoom(guest, "Sai Adarsh");
	printGuest(guest);
	G.bookRoom(rooms, 102, guest, "Sai Adarsh");
	printGuest(guest);
	R.checkIn(guest, logBook, "Sai Adarsh", 100);
	R.checkIn(guest, logBook, "Sai Adarsh", 103);
	R.checkIn(guest, logBook, "Sai Adarsh", 105);
	printLog(logBook);
	H.addTimeToRoom(rooms, houseKeepingLog, 105, 10);
	H.addTimeToRoom(rooms, houseKeepingLog, 105, 20);
	H.addTimeToRoom(rooms, houseKeepingLog, 105, 30);
	printHouseKeeping(houseKeepingLog);
}
