#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

// 4ms

class Solution {
public:
    bool is_pair(char l, char r) {
        return (l == '(' && r == ')' || l == '{' && r == '}' || l == '[' && r == ']');
    }

    bool isValid(string s) {
        int len = s.size();
        deque<char> stack;
        for (int i = 0; i < len; i++) {
            if (stack.empty()) {
                stack.emplace_back(s[i]);
            } else {
                char l = stack.back();
                char r = s[i];
                if (is_pair(l, r)) {
                    stack.pop_back();
                } else {
                    stack.emplace_back(s[i]);
                }
            }
        }
        return (stack.empty());
    }
};

int main(void) {
    Solution s;
    string str = "(()){}[[]]";
    printf("%d\n", s.isValid(str));
    return 0;
}
