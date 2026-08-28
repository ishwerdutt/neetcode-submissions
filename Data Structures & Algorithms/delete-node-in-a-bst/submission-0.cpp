/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int getMax(TreeNode* root){
        if (root == NULL){
            return -1;
        }
        while (root->right){
            root = root->right;
        }
        return root->val;
    }
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (root == NULL){
            return NULL;
        }

        if (root->val ==  key){
            //there are our four cases

            //case1, the "node to be deleted is a leaf node"
            if(root->left == NULL && root->right == NULL){
                TreeNode* temp = root;
                delete temp;
                return NULL;
            }

            // case2:- if the "node to be deleted is a node with single left child"
            if (root->left != NULL && root->right ==  NULL){
                TreeNode* temp = root;
                TreeNode* leftChild = root->left;
                temp->left = NULL;
                delete temp;
                return leftChild;
            }

            // case3:- if the "node to be deleted is a node with single right child"
            if (root->left == NULL && root->right !=  NULL){
                TreeNode* temp = root;
                TreeNode* rightChild = root->right;
                temp->right = NULL;
                delete temp;
                return rightChild;
            }

            //case4:- if the "node to be deleted is node with two childrens"
            if (root->left != NULL && root->right != NULL){
                int replaceVal = getMax(root->left);
                //now we will replace the root value with the replace value
                root->val = replaceVal;

                //delete the replaceVal
                root->left = deleteNode(root->left, replaceVal);
                return root;
            }
        }
        // but we have basically done is searching on left or right and deleting the node by make use of recursion
        else{
            if(key > root->val){
                root->right = deleteNode(root->right, key);
            }
            else{
                root->left = deleteNode(root->left, key);
            }
        }
        return root;
    }
    
};