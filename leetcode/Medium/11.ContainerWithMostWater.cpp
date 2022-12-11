#include <bits/stdc++.h>
#define _GLIBCXX_DEBUG

class Solution {
public:
    int maxArea(std::vector<int>& height) {
        std::vector<std::pair<int, int>> hi;
        const int INF = 100100;
        int mn = INF, mx = -INF, ans = 0;

        for (int i = 0; i < height.size(); i++) {
            hi.push_back({height[i], i});
        }
        sort(hi.rbegin(), hi.rend());
        for (auto &[h, i] : hi) {
            if (mn != INF) {
                ans = std::max(ans, std::abs(i - mn) * h);
            }
            if (mx != -INF) {
                ans = std::max(ans, std::abs(mx - i) * h);
            }
            mn = std::min(mn, i);
            mx = std::max(mx, i);
        }
        return ans;
    }
};

int main(void) {
    Solution s;
    std::vector<int> height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    std::cout << s.maxArea(height) << std::endl;
    height = {1, 1};
    std::cout << s.maxArea(height) << std::endl;
}

// 209ms, 56.29%
