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

class Solution {
public:
    void listAddBack(ListNode **node, ListNode **list) {
        (*node)->next = new ListNode{ (*list)->val };
        *node = (*node)->next;
        if (*list) {
            *list = (*list)->next;
        }
    }
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode head;
        ListNode *node = &head;
        while (list1 && list2) {
            if (list1->val <= list2->val) {
                listAddBack(&node, &list1);
            } else {
                listAddBack(&node, &list2);
            }
        }
        while (list1) {
            listAddBack(&node, &list1);
        }
        while (list2) {
            listAddBack(&node, &list2);
        }
        return head.next;
    }
};
