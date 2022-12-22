#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

// 7ms

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> vec;
        auto dfs = [&](auto self, vector<int>& vec, int total, int i) {
            if (total > target) {
                return;
            }
            if (total == target) {
                res.push_back(vec);
                return;
            }
            for (int j = i; j < candidates.size(); j++) {
                vec.push_back(candidates[j]);
                self(self, vec, total + candidates[j], j);
                vec.pop_back();
            }
        };
        dfs(dfs, vec, 0, 0);
        return res;
    }
};

int main(void) {
    Solution s;
    vector<int> candidates = {2, 3, 6, 7};
    for (auto &vec : s.combinationSum(candidates, 7)) {
        for (auto &x : vec) {
            cout << x << " ";
        }
        cout << endl;
    }
    return 0;
}
