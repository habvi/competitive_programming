#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        const int len = s.size();
        set<char> st;
        unsigned int ans = 0; // submit: unsigned long
        int right = 0;
        for (int left = 0; left < len; left++) {
            while (right < len && st.find(s[right]) == st.end()) {
                st.insert(s[right]);
                right++;
            }
            ans = max(ans, st.size());
            st.erase(s[left]);
        }
        return (int)ans;
    }
};

int main(void) {
    Solution s;
    cout << s.lengthOfLongestSubstring("abcabcbb") << endl;
}

// 40ms, 45.4%
