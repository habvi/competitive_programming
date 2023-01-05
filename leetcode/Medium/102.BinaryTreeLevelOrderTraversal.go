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

func PopFrontDeque(deque *list.List) interface{} {
	x := deque.Front()
	if x == nil {
		return nil
	}
	return deque.Remove(x)
}

func levelOrder(root *TreeNode) [][]int {
	var res [][]int
	que := list.New()
	if root != nil {
		que.PushBack(root)
	}
	for que.Len() != 0 {
		var vec []int
		n := que.Len()
		for i := 0; i < n; i++ {
			if node, ok := PopFrontDeque(que).(*TreeNode); ok {
				vec = append(vec, node.Val)
				if node.Left != nil {
					que.PushBack(node.Left)
				}
				if node.Right != nil {
					que.PushBack(node.Right)
				}
			}
		}
		res = append(res, vec)
	}
	return res
}

func main() {
	node := &TreeNode{Val: 3, Left: &TreeNode{Val: 9}, Right: &TreeNode{Val: 20, Left: &TreeNode{Val: 15}, Right: &TreeNode{Val: 7}}}
	fmt.Println(levelOrder(node))
}
