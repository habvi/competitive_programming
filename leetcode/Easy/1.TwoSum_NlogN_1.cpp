#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

vector<int> twoSum(vector<int>& nums, int target) {
    const int len = nums.size();

    set<pair<int, int>> st;
    for (int i = 0; i < len; i++) {
        st.insert({nums[i], i});
    }

    vector<int> ans;
    for (int i = len - 1; i >= 0; i--) {
        int x = target - nums[i];
        auto itr = st.lower_bound({x, 0});
        if (itr != st.end() && itr->second != i) {
            if (x == itr->first) {
                ans = {itr->second, i};
                break;
            }
        }
    }
    return ans;
}

int main(void) {
    vector<int> nums = {2, 4, 11, 3};
    vector<int> ans = twoSum(nums, 6);
    cout << ans[0] << " " << ans[1] << endl;
    return 0;
}

// 33ms, 55.27%