package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dfs_p(node, p *TreeNode, set *map[int]struct{}) bool {
	if node == nil {
		return false
	}
	if node == p {
		return true
	}
	if dfs_p(node.Left, p, set) {
		(*set)[node.Left.Val] = struct{}{}
		return true
	}
	if dfs_p(node.Right, p, set) {
		(*set)[node.Right.Val] = struct{}{}
		return true
	}
	return false
}

func dfs_q(node, q *TreeNode, set map[int]struct{}, ans **TreeNode) bool {
	if node == nil {
		return false
	}
	if node == q {
		if _, ok := set[node.Val]; ok {
			*ans = node
			return false
		}
		return true
	}
	if dfs_q(node.Left, q, set, ans) {
		if _, ok := set[node.Val]; ok {
			*ans = node
			return false
		}
		return true
	}
	if dfs_q(node.Right, q, set, ans) {
		if _, ok := set[node.Val]; ok {
			*ans = node
			return false
		}
		return true
	}
	return false
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	set := make(map[int]struct{})
	set[root.Val] = struct{}{}
	dfs_p(root, p, &set)

	var ans *TreeNode
	dfs_q(root, q, set, &ans)
	return ans
}
