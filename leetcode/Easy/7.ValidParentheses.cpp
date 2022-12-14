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
        deque<char> stack;

        for (int i = 0; i < s.size(); i++) {
            if (stack.empty()) {
                stack.emplace_back(s[i]);
            } else {
                if (is_pair(stack.back(), s[i])) {
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
