class MyHashMap {
private:
    vector<vector<int>> myMap;

public:
    MyHashMap() {}

    void put(int key, int value) {
        vector<int> tempV = {key, value};
        for (int i = 0; i < myMap.size(); i++) {
            if (myMap[i][0] == key) {
                myMap[i][1] = value;
                return;
            }
        }
        myMap.push_back(tempV);
    }

    int get(int key) {
        for (int i = 0; i < myMap.size(); i++) {
            if (myMap[i][0] == key) {
                return myMap[i][1];
            }
        }
        return -1;
    }

    void remove(int key) {
        for (int i = 0; i < myMap.size(); i++) {
            if (myMap[i][0] == key) {
                myMap.erase(myMap.begin() + i);
            }
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */