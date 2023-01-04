package main

import (
	"container/list"
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func deque_print_all(deque *list.List) {
	for e := deque.Front(); e != nil; e = e.Next() {
		fmt.Print(e.Value, " ")
	}
	fmt.Println()
}

func PopFrontDeque(deque *list.List) interface{} {
	x := deque.Front()
	if x == nil {
		return nil
	}
	return deque.Remove(x)
}

func orderTree(p *TreeNode) []int {
	var num []int
	const inf = 10005
	que := list.New()
	que.PushBack(p)
	for que.Len() != 0 {
		if node, ok := PopFrontDeque(que).(*TreeNode); ok {
			if node == nil {
				num = append(num, inf)
				continue
			}
			num = append(num, node.Val)
			que.PushBack(node.Left)
			que.PushBack(node.Right)
		}
	}
	return num
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	p_num := orderTree(p)
	q_num := orderTree(q)
	if len(p_num) != len(q_num) {
		return false
	}
	for i := 0; i < len(p_num); i++ {
		if p_num[i] != q_num[i] {
			return false
		}
	}
	return true
}

func main() {
	p := &TreeNode{Val: 1, Left: &TreeNode{Val: 2}, Right: &TreeNode{Val: 3}}
	fmt.Println(isSameTree(p, p))
}
