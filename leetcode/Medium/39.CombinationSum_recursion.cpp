#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

// 7ms

class Solution {
public:
    vector<vector<int>> res;
    vector<int> cand_cp;
    int target_cp;
    void dfs(vector<int>& v, int total, int i) {
        if (i == cand_cp.size() || total > target_cp) {
            return;
        }
        if (total == target_cp) {
            res.push_back(v);
            return;
        }
        for (int j = i; j < cand_cp.size(); j++) {
            v.push_back(cand_cp[j]);
            dfs(v, total + cand_cp[j], j);
            v.pop_back();
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        cand_cp = candidates;
        target_cp = target;
        vector<int> v;
        dfs(v, 0, 0);
        return res;
    }
};

int main(void) {
    Solution s;
    vector<int> candidates = {2, 3, 6, 7};
    for (auto &v : s.combinationSum(candidates, 7)) {
        for (auto &x : v) {
            cout << x << " ";
        }
        cout << endl;
    }
    return 0;
}
