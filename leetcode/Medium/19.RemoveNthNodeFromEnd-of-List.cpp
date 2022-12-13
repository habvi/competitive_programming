#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// 3ms

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *node = head;
        ListNode *left = head;
        ListNode *right = nullptr;
        int len = 0, target;

        while (node) {
            len++;
            node = node->next;
        }
        target = len - n;
        node = head;
        for (int i = 0; i < len; i++) {
            if (i == target - 1) {
                left = node;
            }
            if (i == target + 1) {
                right = node;
                break;
            }
            node = node->next;
        }
        if (left->next == right) { // L,  L R n n n
            delete head;
            head = right;
        } else {                   // n n L n R n n,  n n L n
            delete left->next;
            left->next = right;
        }
        return head;
    }
};
