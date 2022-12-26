#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

// 44ms

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> mp;
        for (string &s : strs) {
            string sorted_s = s;
            sort(sorted_s.begin(), sorted_s.end());
            mp[sorted_s].push_back(s);
        }

        vector<vector<string>> res;
        for (auto &[_, vec] : mp) {
            res.push_back(vec);
        }
        return res;
    }
};
