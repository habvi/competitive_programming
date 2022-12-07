#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

vector<int> twoSum(vector<int>& nums, int target) {
    const int len = nums.size();
    bool fin = false;
    vector<int> ans;

    for (int i = 0; i < len; i++) {
        for (int j = i + 1; j < len; j++) {
            if (nums[i] + nums[j] == target) {
                ans = {i, j};
                fin = true;
                break;
            }
        }
        if (fin)
            break;
    }
    return ans;
}

int main(void) {
    vector<int> nums = {2, 7, 11, 15};
    vector<int> ans = twoSum(nums, 9);
    cout << ans[0] << " " << ans[1] << endl;
    return 0;
}

// 752ms, 26.68%