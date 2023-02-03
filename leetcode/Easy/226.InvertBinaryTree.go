package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dfs(node *TreeNode) {
	if node == nil {
		return
	}
	tmp := node.Left
	node.Left = node.Right
	node.Right = tmp
	dfs(node.Left)
	dfs(node.Right)
}

func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	dfs(root)
	return root
}
