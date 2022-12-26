#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

// 123ms

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        const int INF = 1001001001;
        int mx = 0, ans = -INF;
        for (int &x : nums) {
            mx = max(mx + x, x);
            ans = max(ans, mx);
        }
        return ans;
    }
};
