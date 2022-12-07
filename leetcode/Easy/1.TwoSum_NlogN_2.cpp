#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        const int len = nums.size();

        unordered_map<int, int> seen;
        vector<int> ans;
        for (int i = 0; i < len; i++)
        {
            int x = target - nums[i];
            if (seen.find(x) != seen.end()) {
                ans = {seen[x], i};
                break;
            }
            seen[nums[i]] = i;
        }
        return ans;
    }
};

int main(void) {
    Solution s;
    vector<int> nums = {2, 4, 11, 3};
    vector<int> ans = s.twoSum(nums, 6);
    cout << ans[0] << " " << ans[1] << endl;
    return 0;
}

// 32ms, 56.93%