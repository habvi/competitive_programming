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

func max_n(nums ...int) int {
	res := nums[0]
	for i := 1; i < len(nums); i++ {
		res = max(res, nums[i])
	}
	return res
}

const inf = 1001001001

func dfs(node *TreeNode, ans int) int {
	if node == nil {
		return ans
	}
	ans = max_n(ans, dfs(node.Left, ans), dfs(node.Right, ans))
	l, r := -inf, -inf
	now := node.Val
	if node.Left != nil {
		l = node.Left.Val
	}
	if node.Right != nil {
		r = node.Right.Val
	}
	ans = max_n(ans, now, l, r, l+now, r+now, l+r+now)
	node.Val = max_n(now, l+now, r+now)
	return ans
}

func maxPathSum(root *TreeNode) int {
	return dfs(root, -inf)
}

func main() {
	node := &TreeNode{Val: -10, Left: &TreeNode{Val: 9}, Right: &TreeNode{Val: 20, Left: &TreeNode{Val: 15}, Right: &TreeNode{Val: 7}}}
	fmt.Println(maxPathSum(node))

	node = &TreeNode{Val: -3}
	fmt.Println(maxPathSum(node)) // -3

	node = &TreeNode{Val: 5, Left: &TreeNode{Val: 4, Left: &TreeNode{Val: 11, Left: &TreeNode{Val: 7}, Right: &TreeNode{Val: 2}}}, Right: &TreeNode{Val: 8, Left: &TreeNode{Val: 13}, Right: &TreeNode{Val: 4, Right: &TreeNode{Val: 1}}}}
	fmt.Println(maxPathSum(node)) // 48
}
