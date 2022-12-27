#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

// 0ms!?

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        int h = matrix.size(), w = matrix[0].size();
        const int FIN = 200;
        int i = 0, j = 0;
        bool is_spiral = true;

        while (is_spiral) {
            is_spiral = false;
            while (j < w && matrix[i][j] != FIN) {
                res.push_back(matrix[i][j]);
                matrix[i][j] = FIN;
                is_spiral |= true;
                j++;
            }
            i++; j--;
            while (i < h && matrix[i][j] != FIN) {
                res.push_back(matrix[i][j]);
                matrix[i][j] = FIN;
                is_spiral |= true;
                i++;
            }
            i--; j--;
            is_spiral = false;
            while (j >= 0 && matrix[i][j] != FIN) {
                res.push_back(matrix[i][j]);
                matrix[i][j] = FIN;
                is_spiral |= true;
                j--;
            }
            j++; i--;
            while (i >= 0 && matrix[i][j] != FIN) {
                res.push_back(matrix[i][j]);
                matrix[i][j] = FIN;
                is_spiral |= true;
                i--;
            }
            i++; j++;
        }
        return res;
    }
};
