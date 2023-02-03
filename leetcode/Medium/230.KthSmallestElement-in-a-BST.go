package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dfs(nodes *[]int, node *TreeNode) {
	if node == nil {
		return
	}
	dfs(nodes, node.Left)
	*nodes = append(*nodes, node.Val)
	dfs(nodes, node.Right)
}

func kthSmallest(root *TreeNode, k int) int {
	var nodes []int
	dfs(&nodes, root)
	return nodes[k-1]
}

func main() {
	root := TreeNode{Val: 3, Left: &TreeNode{Val: 1, Right: &TreeNode{Val: 2}}, Right: &TreeNode{Val: 4}}
	fmt.Println(kthSmallest(&root, 3))
}
