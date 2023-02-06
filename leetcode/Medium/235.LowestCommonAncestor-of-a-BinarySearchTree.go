package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func min(x, y int) int {
	return int(math.Min(float64(x), float64(y)))
}

func max(x, y int) int {
	return int(math.Max(float64(x), float64(y)))
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	mn := min(p.Val, q.Val)
	mx := max(p.Val, q.Val)
	for root != nil {
		if root.Val < mn {
			root = root.Right
		} else if root.Val > mx {
			root = root.Left
		} else {
			break
		}
	}
	return root
}
