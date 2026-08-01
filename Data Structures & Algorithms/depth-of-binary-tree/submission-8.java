/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution 
{
    public int maxDepth(TreeNode root) 
    {
        if (root == null)
        {
            return 0;
        }
        if (root.right == null && root.left == null)
        {
            return 1;
        }
        return depth(root,0);
    }
    public int depth(TreeNode node, int len)
    {
        int l = 0;
        int r = 0;
        if (node == null)
        {
            return len;
        }
        if (node.left == null && node.right != null)
        {
            r = depth(node.right,len + 1);
        }
        else if (node.right == null && node.left != null)
        {
            l = depth(node.left,len + 1);
        }
        else
        {
            l = depth(node.left,len + 1);
            r = depth(node.right, len + 1);
        }

        return Math.max(l,r);
    }
}
