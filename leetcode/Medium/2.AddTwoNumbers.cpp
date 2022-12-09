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
        int num1, num2, carry = 0;

        ListNode *node = ans;
        while (l1 || l2 || carry) {
            num1 = 0;
            num2 = 0;
            if (l1) {
                num1 = l1->val;
                l1 = l1->next;
            }
            if (l2) {
                num2 = l2->val;
                l2 = l2->next;
            }
            int total = num1 + num2 + carry;
            if (head) {
                node->val = total % 10;
                head = false;
            } else {
                node->next = new ListNode(total % 10);
                node = node->next;
            }
            carry = total / 10;
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

// 32ms, 95.57%
