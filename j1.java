private void inOrderTraversal(TreeNode node) {
    if (node==null) {
        return null;
    }
    inOrderTraversal(node.left);
    System.out.printf("%s", node.val);
    inOrderTraversal(node.right);
}


class Miti{
    public  void main(String s) {
        System.out.println("this is crazy!");
    }
}

// Your First Program

class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}