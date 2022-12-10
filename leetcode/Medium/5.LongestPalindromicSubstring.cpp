#include <bits/stdc++.h>
#define _GLIBCXX_DEBUG

class Solution {
private:
    std::string s_copy;
    int len, start, max_len;

    void find_substr(int left, int right) {
        int sub_len;

        while (0 <= left && right < len && s_copy[left] == s_copy[right]) {
            sub_len = right - left + 1;
            if (sub_len > max_len) {
                start = left;
                max_len = sub_len;
            }
            left--;
            right++;
        }
    }
public:
    std::string longestPalindrome(std::string s) {
        s_copy = s;
        len = s.size();
        max_len = 0;

        for (int i = 0; i < len; i++) {
            find_substr(i, i); // odd
            find_substr(i, i + 1); // even
        }
        return s.substr(start, max_len);
    }
};

int main(void) {
    Solution s;
    std::cout << s.longestPalindrome("babad") << std::endl;
    std::cout << s.longestPalindrome("cbbd") << std::endl;
}

// 34ms, 64%


// TLE

// class Solution {
// public:
//     string longestPalindrome(string s) {
//         const size_t len = s.size();
//         size_t max_len = 0;
//         string ans;
//         for (size_t i = 0; i < len; i++) {
//             for (size_t j = 1; j <= len - i; j++) {
//                 string sub_str = s.substr(i, j);
//                 string rev_str = sub_str;
//                 reverse(rev_str.begin(), rev_str.end());
//                 if (sub_str == rev_str && j > max_len) {
//                     ans = sub_str;
//                     max_len = j;
//                 }
//             }
//         }
//         return ans;
//     }
// };
