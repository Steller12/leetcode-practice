class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> myMap;
        for(int i=0; i<strs.size();i++){
            string s=strs[i];
            sort(s.begin(),s.end());
            myMap[s].push_back(strs[i]);  
        }
        vector<vector<string>> ans;
        for(auto& entry:myMap){
            ans.push_back(entry.second);
        }
        return ans;
    }
};