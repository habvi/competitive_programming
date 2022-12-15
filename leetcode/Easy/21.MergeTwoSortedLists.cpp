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
    void listAddBack(ListNode **node, ListNode **list) {
        if (!*node) {
            *node = new ListNode{ (*list)->val };
        } else {
            (*node)->next = new ListNode{ (*list)->val };
            *node = (*node)->next;
        }
        if (*list) {
            *list = (*list)->next;
        }
    }
    void set_head(ListNode **head, ListNode *node, bool *is_head) {
        if (*is_head) {
            *head = node;
            *is_head = false;
        }
    }
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *head = nullptr, *node = nullptr;
        bool is_head = true;
        while (list1 && list2) {
            cout << list1->val << " " << list2->val << endl;
            if (list1->val <= list2->val) {
                listAddBack(&node, &list1);
            } else {
                listAddBack(&node, &list2);
            }
            set_head(&head, node, &is_head);
        }
        while (list1) {
            listAddBack(&node, &list1);
            set_head(&head, node, &is_head);
        }
        while (list2) {
            listAddBack(&node, &list2);
            set_head(&head, node, &is_head);
        }
        return head;
    }
};
