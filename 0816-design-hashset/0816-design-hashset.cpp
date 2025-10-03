class MyHashSet {
private:
    vector<int> v1;
public:
    MyHashSet() {
        
    }
    
    void add(int key) {
        for(int i=0; i<v1.size(); i++){
            if (v1[i]==key){
                return;
            }
        }
        v1.push_back(key);
    }
    
    void remove(int key) {
        for(int i=0;i<v1.size();i++){
            if (v1[i]==key){
                v1.erase(v1.begin()+i);
            }
        }
    }
    
    bool contains(int key) {
        for(int i=0;i<v1.size();i++){
            if(v1[i]==key){
                return true;
            }
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */