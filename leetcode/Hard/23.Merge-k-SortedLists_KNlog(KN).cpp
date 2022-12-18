#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

// 45ms

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<pair<int, ListNode *>> vec;
        ListNode head;
        ListNode *node = &head;

        for (auto node : lists) {
            while (node) {
                vec.push_back({node->val, node});
                node = node->next;
            }
        }
        sort(vec.begin(), vec.end());
        node = &head;
        for (auto [_, ptr] : vec) {
            node->next = ptr;
            node = node->next;
        }
        return head.next;
    }
};
