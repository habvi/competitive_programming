#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

// 9ms

class Solution {
public:
    vector<int> nums_copy;
    int target_copy;
    bool is_ok(int left, int right) {
        return (nums_copy[left] > nums_copy[right - 1]);
    }
    bool is_ok2(int left, int right) {
        return (nums_copy[left] <= target_copy && target_copy <= nums_copy[right - 1]);
    }
    int bisect(int ng, int ok, int border) {
        while (abs(ok - ng) > 1) {
            int middle = (ok + ng) / 2;
            if (border ? is_ok(ng, middle) : is_ok2(ng, middle)) {
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

        int start = bisect(0, len, 1);
        int idx = bisect(0, start, 0);
        if ((nums[idx - 1]) == target) {
            return idx - 1;
        }
        idx = bisect(start, len, 0);
        if ((nums[idx - 1]) == target) {
            return idx - 1;
        }
        return -1;
    }
};

int main(void) {
    Solution s;
    vector<int> nums = {4, 5, 6, 7, 0, 1, 2};
    cout << s.search(nums, 3) << endl;
    cout << s.search(nums, 1) << endl;
    return 0;
}
