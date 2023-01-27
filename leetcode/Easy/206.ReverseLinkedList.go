package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	var lists []*ListNode
	for head != nil {
		lists = append(lists, head)
		head = head.Next
	}
	n := len(lists)
	tail := lists[n-1]
	for i := n - 2; i >= 0; i-- {
		tail.Next = lists[i]
		tail = tail.Next
	}
	tail.Next = nil
	return lists[n-1]
}
