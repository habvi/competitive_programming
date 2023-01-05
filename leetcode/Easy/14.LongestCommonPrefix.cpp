#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

int find_idx(vector<string>& strs) {
    int word = strs.size();
    int minlen = 205;

    for (int i = 0; i < word; i++) {
        minlen = min(minlen, (int)strs[i].size());
    }
    for (int i = 0; i < minlen; i++) {
        for (int j = 1; j < word; j++) {
            if (strs[j - 1][i] != strs[j][i])
                return i;
        }
    }
    return minlen;
}

string longestCommonPrefix(vector<string>& strs) {
    return strs[0].substr(0, find_idx(strs));
}

int main(void) {
    vector<string> strs;
    strs.push_back("ab");
    strs.push_back("a");
    cout << longestCommonPrefix(strs) << endl;
    return 0;
}
