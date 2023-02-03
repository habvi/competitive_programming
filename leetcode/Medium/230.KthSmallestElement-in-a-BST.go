package main

import (
	"fmt"
	"sort"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func get_all_nodes(nodes *[]int, node *TreeNode) {
	if node == nil {
		return
	}
	*nodes = append(*nodes, node.Val)
	get_all_nodes(nodes, node.Left)
	get_all_nodes(nodes, node.Right)
}

func kthSmallest(root *TreeNode, k int) int {
	var nodes []int
	get_all_nodes(&nodes, root)
	sort.Sort(sort.IntSlice(nodes))
	return nodes[k-1]
}

func main() {
	root := TreeNode{Val: 3, Left: &TreeNode{Val: 1, Right: &TreeNode{Val: 2}}, Right: &TreeNode{Val: 4}}
	fmt.Println(kthSmallest(&root, 3))
}
