#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

// 1031ms

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        const int len = nums.size();
        unordered_map<int, int> head;
        unordered_map<int, int> tail;
        unordered_map<int, int> count_num;
        vector<vector<int>> ans;

        sort(nums.begin(), nums.end());
        for (int i = 0; i < len; i++) {
            int x = nums[i];
            if (head[x] == 0) {
                head[x] = i + 1;
            }
            tail[x] = i + 1;
            count_num[x]++;
        }
        for (int i = 0; i < len; i++) {
            int ni = nums[i];
            for (int j = i + 1; j < len; j++) {
                int nj = nums[j];
                int nk = -(ni + nj);
                if (nk < nj || !count_num[nk] || head[ni] != i + 1 || tail[nj] != j + 1) {
                    continue;
                }
                if (count_num[ni] >= 3 && ni == 0 && nj == 0 && nk == 0) { // 0 0 0 0 0
                    ans.push_back({ni, nj, nk});
                    continue;
                }
                if (count_num[ni] >= 2 && ni == nj && nj != nk) { // -2 -2 -2 4
                    ans.push_back({ni, nj, nk});
                    continue;
                }
                if (count_num[nj] >= 2 && ni != nj && nj == nk) { // -4 2 2 2 2 2
                    ans.push_back({ni, nj, nk});
                    continue;
                }
                if (ni != nj && nj != nk) { // -2 0 2
                    ans.push_back({ni, nj, nk});
                }
            }
        }
        return ans;
    }
};

int main(void) {
    Solution s;
    vector<vector<int>> ans;

    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    ans = s.threeSum(nums);
    for (auto &v : ans) {
        cout << v[0] << " " << v[1] << " " << v[2] << endl;
    }
    nums = {-1, 0, 1, 0};
    ans = s.threeSum(nums);
    for (auto &v : ans) {
        cout << v[0] << " " << v[1] << " " << v[2] << endl;
    }
    return 0;
}
