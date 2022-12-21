#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

// 20ms

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<vector<int>>> dp(target + 1, vector<vector<int>> {});
        dp[0].push_back({0});
        for (int &x : candidates) {
            for (int i = 0; i < target + 1; i++) {
                if (i + x <= target) {
                    for (auto &v : dp[i]) {
                        vector<int> tmp = v;
                        tmp.push_back(x);
                        dp[i + x].push_back(tmp);
                    }
                }
            }
        }

        vector<vector<int>> res;
        for (auto &v : dp[target]) {
            vector<int> tmp;
            copy(v.begin() + 1, v.end(), back_inserter(tmp));
            res.push_back(tmp);
        }
        return res;
    }
};

int main(void) {

    return 0;
}
