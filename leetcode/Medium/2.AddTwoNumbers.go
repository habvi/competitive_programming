package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	ans := new(ListNode)
	head := true
	var carry int

	node := ans
	for l1 != nil || l2 != nil || carry != 0 {
		var num1, num2 int
		if l1 != nil {
			num1 = l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			num2 = l2.Val
			l2 = l2.Next
		}
		total := num1 + num2 + carry
		if head == true {
			node.Val = total % 10
			head = false
		} else {
			node.Next = &ListNode{Val: total % 10, Next: nil}
			node = node.Next
		}
		carry = total / 10
	}
	return ans
}

func print_list(node *ListNode) {
	for node != nil {
		fmt.Print(node.Val, " ")
		node = node.Next
	}
	fmt.Println()
}

func main() {
	l1 := ListNode{Val: 2, Next: &ListNode{Val: 4, Next: &ListNode{Val: 3, Next: nil}}}
	print_list(&l1)
	l2 := ListNode{Val: 5, Next: &ListNode{Val: 6, Next: &ListNode{Val: 4, Next: nil}}}
	print_list(&l2)

	print_list(addTwoNumbers(&l1, &l2))
}

// 17ms, 55.21%
