#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

// 600ms

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
        ListNode head;
        ListNode *min_ptr, *tmp, *node = &head;
        int min_num, min_idx, i;
        while (1) {
            min_num = 10005;
            min_ptr = nullptr;
            i = 0;
            for (auto tmp : lists) {
                if (tmp) {
                    if (tmp->val <= min_num) {
                        min_num = tmp->val;
                        min_ptr = tmp;
                        min_idx = i;
                    }
                }
                i++;
            }
            if (!min_ptr) {
                break;
            }
            node->next = min_ptr;
            node = node->next;
            if (min_ptr->next) {
                lists[min_idx] = lists[min_idx]->next;
            } else {
                lists[min_idx] = nullptr;
            }
        }
        return head.next;
    }
};
