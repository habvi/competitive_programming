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
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        ListNode *ans = new ListNode;
        bool head = true;
        int carry = 0;

        ListNode *node = ans;
        while (l1 || l2 || carry) {
            int num1 = l1 ? l1->val : 0;
            int num2 = l2 ? l2->val : 0;
            int total = num1 + num2 + carry;
            if (head) {
                node->val = total % 10;
                head = false;
            } else {
                node->next = new ListNode(total % 10);
                node = node->next;
            }
            carry = total / 10;
            if (l1) {
                l1 = l1->next;
            }
            if (l2) {
                l2 = l2->next;
            }
        }
        return ans;
    }
};

void print_list(ListNode *list) {
    while (list) {
        cout << list->val << " ";
        list = list->next;
    }
    cout << endl;
}

int main(void) {
    ListNode *l1 = new ListNode(2);
    l1->next = new ListNode(4);
    l1->next->next = new ListNode(3);
    print_list(l1);

    ListNode *l2 = new ListNode(5, new ListNode(6, new ListNode(4)));
    print_list(l2);

    Solution s;
    ListNode *ans = s.addTwoNumbers(l1, l2);
    print_list(ans);

    delete[] ans;
    delete[] l1;
    delete[] l2;
    return (0);
}

// 70ms, 41.58%
