#include <iostream>
#include <algorithm>
#include <vector>
#include <bits/stdc++.h>

#define MAX_SIZE 10

using namespace std;

class payment {
	public:
		string printRandom() {
			return "Payment successful\n";
		}
};

class floors : public payment {
	public:
		void addToFloor(string car_type, int time, map <string, vector<int>> &floorData) {
			floorData[car_type].push_back(time);
			if (floorData[car_type].size() <= MAX_SIZE) {
				cout<<"Floor size "<<floorData[car_type].size()<<"\n";	
			}
			else {
				cout<<"Space is full for "<<car_type<<" \n";
			}
		}
		
		void popCar(string car_type, int time, map <string, vector <int>> &floorData) {
			auto indexing = find(floorData[car_type].begin(), floorData[car_type].end(), time);
			payment *P = new payment();
			if (indexing != floorData[car_type].end()) {
				cout<<P->printRandom();
				floorData[car_type].erase(indexing);
			}
		}
};

void printFloor(map <string, vector<int>> &floorData) {
	for (auto i = floorData.begin(); i != floorData.end(); i++) {
		cout<<i->first<<"\n";
		for (int j = 0; j < i->second.size(); j++) {
			cout<<i->second[j]<<"\n";
		}
	}
} 

void printIndividualFloor(string car_type, map <string, vector<int>> &floorData) {
	cout<<"Print "<<car_type<<"\n";
	auto indexing = floorData.find(car_type);
	if (indexing != floorData.end()) {
		for (int i = 0; i < indexing->second.size(); i++) {
			cout<<indexing->second[i]<<"\n";
		}
	}
}

int main() {
	map <string, vector<int>> floorData;
	floors *Obj = new floors();
	cout<<"Adding car to parking\n";
	Obj->addToFloor("Car", 1, floorData);
	Obj->addToFloor("Car", 2, floorData);
	Obj->addToFloor("Car", 3, floorData);
	Obj->addToFloor("Car", 4, floorData);
	cout<<"Popping car at time 1\n";
	Obj->popCar("Car", 1, floorData);
	cout<<"Adding bus to parking\n";
	Obj->addToFloor("Bus", 1, floorData);
	Obj->addToFloor("Bus", 2, floorData);
	Obj->addToFloor("Bus", 3, floorData);
	Obj->addToFloor("Bus", 4, floorData);
	cout<<"Popping bus at time 2\n";
	Obj->popCar("Bus", 2, floorData);
	printFloor(floorData);
	printIndividualFloor("Bus", floorData);
}
