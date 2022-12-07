#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        const int len = nums.size();
        bool fin = false;
        vector<int> ans;
        for (int i = 0; i < len && !fin; i++) {
            for (int j = i + 1; j < len && !fin; j++) {
                if (nums[i] + nums[j] == target) {
                    ans = {i, j};
                    fin = true;
                }
            }
        }
        return ans;
    }
};

int main(void) {
    Solution s;
    vector<int> nums = {2, 7, 11, 15};
    vector<int> ans = s.twoSum(nums, 9);
    cout << ans[0] << " " << ans[1] << endl;
    return 0;
}

// 752ms, 26.68%