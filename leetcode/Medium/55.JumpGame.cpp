#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

// 78ms

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int len = nums.size();
        vector<bool> reachable(len, false);
        reachable[0] = true;

        int right = 0;
        for (int i = 0; i < len; i++) {
            if (!reachable[i]) {
                continue;
            }
            for (int j = max(i, right); j < min(len, i + nums[i] + 1); j++) {
                reachable[j] = true;
            }
            right = min(len, max(right, i + nums[i]));
        }
        return reachable[len - 1];
    }
};
