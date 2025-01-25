
class Solution {
public:
    bool isIsomorphic(std::string s, std::string t) {
        if (s.length() != t.length()) {
            return false;
        }

       unordered_map<char, char> mp; 
       unordered_map<char, char> reverseMp; 

        for (int i = 0; i < s.length(); i++) {
            
            if (mp.find(s[i]) != mp.end()) {
                if (mp[s[i]] != t[i]) {
                    return false;
                }
            } else {
                mp[s[i]] = t[i];
            }

            if (reverseMp.find(t[i]) != reverseMp.end()) {
                if (reverseMp[t[i]] != s[i]) {
                    return false;
                }
            } else {
                reverseMp[t[i]] = s[i];
            }
        }
        return true; 
    }
};
