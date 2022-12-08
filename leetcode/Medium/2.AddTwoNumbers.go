package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func set_val(node *ListNode) int {
	if node != nil {
		return node.Val
	}
	return 0
}

func move_next(node *ListNode) *ListNode {
	if node != nil {
		return node.Next
	}
	return node
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	ans := new(ListNode)
	head := true
	var carry int

	node := ans
	for l1 != nil || l2 != nil || carry != 0 {
		num1 := set_val(l1)
		num2 := set_val(l2)
		total := num1 + num2 + carry
		if head == true {
			node.Val = total % 10
			head = false
		} else {
			node.Next = &ListNode{Val: total % 10, Next: nil}
			node = node.Next
		}
		carry = total / 10
		l1 = move_next(l1)
		l2 = move_next(l2)
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

// 19ms, 47.9%
