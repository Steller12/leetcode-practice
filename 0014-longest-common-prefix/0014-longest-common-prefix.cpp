class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string s=strs[0];
        int n=s.size();
        for (int i=1; i<strs.size();i++){
            while (s!=strs[i].substr(0,n)){
                n=n-1;
                if(n==0){
                    return "";
                }
                s=s.substr(0,n);
            }
        }
        return s;
    }
};