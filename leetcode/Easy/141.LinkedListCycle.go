package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return false
	}
	var nodes []*ListNode
	for head != nil {
		for _, p := range nodes {
			if p == head {
				return true
			}
		}
		nodes = append(nodes, head)
		head = head.Next
	}
	return false
}

func main() {
	cycled_node := ListNode{Val: 5}
	node := &ListNode{Val: 3, Next: &cycled_node}
	node = &cycled_node
	node.Next = &ListNode{Val: 8, Next: &ListNode{Val: 1, Next: &cycled_node}}
	fmt.Println(hasCycle(node))
}
