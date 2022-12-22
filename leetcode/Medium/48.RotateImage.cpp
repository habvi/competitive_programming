#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

// 0ms(?)

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n - i - 1; j++) {
                vector<int> tmp(4);
                tmp[0] = matrix[i][j];
                tmp[1] = matrix[j][n - i - 1];
                tmp[2] = matrix[n - i - 1][n - j - 1];
                tmp[3] = matrix[n - j - 1][i];

                matrix[j][n - i - 1] = tmp[0];
                matrix[n - i - 1][n - j - 1] = tmp[1];
                matrix[n - j - 1][i] = tmp[2];
                matrix[i][j] = tmp[3];
            }
        }
    }
};

int main(void) {
    Solution s;
    vector<vector<int>> matrix = {{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}};
    s.rotate(matrix);
    int n = matrix.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
