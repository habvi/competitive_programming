#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

// 3ms

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* set_val_and_move_next(ListNode *node, ListNode **list) {
        if (!node) {
            node = new ListNode{ (*list)->val };
        } else {
            node->next = new ListNode{ (*list)->val };
            node = node->next;
        }
        if (*list) {
            *list = (*list)->next;
        }
        return node;
    }
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *head = nullptr, *node = nullptr;
        bool is_head = true;
        while (list1 && list2) {
            cout << list1->val << " " << list2->val << endl;
            if (list1->val <= list2->val) {
                node = set_val_and_move_next(node, &list1);
            } else {
                node = set_val_and_move_next(node, &list2);
            }
            if (is_head) {
                head = node;
                is_head = false;
            }
        }
        while (list1) {
            node = set_val_and_move_next(node, &list1);
            if (is_head) {
                head = node;
                is_head = false;
            }
        }
        while (list2) {
            node = set_val_and_move_next(node, &list2);
            if (is_head) {
                head = node;
                is_head = false;
            }
        }
        return head;
    }
};
