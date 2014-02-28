/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSym(TreeNode *a, TreeNode *b)
    {
        if (a == NULL || b == NULL)
        {
            if (a == NULL && b == NULL)
                return true;
            return false;
        }
        if (a->val != b->val)
            return false;
    
        if (!isSym(a->left, b->right))
            return false;
        if (!isSym(a->right, b->left))
            return false;
    
        return true;
    }
    bool isSymmetric(TreeNode *root) {
        return (root == NULL || isSym(root->left, root->right));
    }
};