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

// 8ms

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *left = head;
        ListNode *right = head;

        int i = 0;
        while (i < n) {
            right = right->next;
            i++;
        }
        if (!right) {
            if (head->next) {
                head = head->next;
            } else {
                head = nullptr;
            }
            return head;
        }
        while (right->next) {
            left = left->next;
            right = right->next;
        }
        if (left->next->next) {
            left->next = left->next->next;
        } else {
            left->next = nullptr;
        }
        return head;
    }
};
