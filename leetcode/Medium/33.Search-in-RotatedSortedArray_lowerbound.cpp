#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

// 6ms

class Solution {
public:
    vector<int> nums_copy;
    int target_copy;
    bool is_ok(int right) {
        return (nums_copy[0] > nums_copy[right]);
    }
    int bisect(int ng, int ok) {
        while (abs(ok - ng) > 1) {
            int middle = (ok + ng) / 2;
            if (is_ok(middle)) {
                ok = middle;
            } else {
                ng = middle;
            }
        }
        return ok;
    }
    int search(vector<int>& nums, int target) {
        int len = nums.size();
        nums_copy = nums;
        target_copy = target;

        int start = bisect(-1, len);
        auto end = nums.begin() + start;
        auto itr = lower_bound(nums.begin(), end, target);
        if (itr != end && *itr == target) {
            return itr - nums.begin();
        }
        itr = lower_bound(nums.begin() + start, nums.end(), target);
        if (itr != nums.end() && *itr == target) {
            return itr - nums.begin();
        }
        return -1;
    }
};

int main(void) {
    Solution s;
    vector<int> nums = {4, 5, 6, 7, 0, 1, 2};
    // cout << s.search(nums, 3) << endl;
    // cout << s.search(nums, 1) << endl;
    nums = {5, 1, 3};
    cout << s.search(nums, 1) << endl;
    return 0;
}
