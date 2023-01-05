package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func max(x, y int) int {
	return int(math.Max(float64(x), float64(y)))
}

func dfs(node *TreeNode, depth int) int {
	if node == nil {
		return depth
	}
	return max(dfs(node.Left, depth+1), dfs(node.Right, depth+1))
}

func maxDepth(root *TreeNode) int {
	return dfs(root, 0)
}

func main() {
	node := &TreeNode{Val: 3, Left: &TreeNode{Val: 9}, Right: &TreeNode{Val: 20, Left: &TreeNode{Val: 15}, Right: &TreeNode{Val: 7}}}
	fmt.Println(maxDepth(node))
}
