private vid inOrderTraversal(TreeNode node) {
    if (node==null) {
        return null;
    }
    inOrderTraversal(node.left);
    System.out.printf("%s", node.val);
    inOrderTraversal(node.right);
}