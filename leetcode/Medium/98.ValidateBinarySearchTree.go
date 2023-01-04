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

func dfs(root *TreeNode, l, r int64) bool {
	ret := true
	if root.Left != nil {
		x := int64(root.Left.Val)
		r64 := int64(root.Val)
		if !(l < x && x < r64) {
			return false
		}
		ret = ret && dfs(root.Left, l, r64)
	}
	if root.Right != nil {
		x := int64(root.Right.Val)
		l64 := int64(root.Val)
		if !(l64 < x && x < r) {
			return false
		}
		ret = ret && dfs(root.Right, l64, r)
	}
	return ret
}

func isValidBST(root *TreeNode) bool {
	inf := int64(math.Pow(2, 31)) + 1
	return dfs(root, -inf, inf)
}

func main() {
	root := &TreeNode{Val: 2, Left: &TreeNode{Val: 1}, Right: &TreeNode{Val: 3}}
	fmt.Println(isValidBST(root))

	root = &TreeNode{Val: 2, Left: &TreeNode{Val: 2}, Right: &TreeNode{Val: 2}}
	fmt.Println(isValidBST(root))

	root = &TreeNode{Val: 0, Left: &TreeNode{Val: -1}}
	fmt.Println(isValidBST(root))
}
