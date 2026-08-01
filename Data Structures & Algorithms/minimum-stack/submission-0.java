class MinStack 
{
    Stack<Integer> stack;
    Stack<Integer> minStack;
    public MinStack() 
    {
        this.stack = new Stack<>();
        this.minStack = new Stack<>();
    }

    public void push(int val) 
    {   
        if(minStack.isEmpty())
        {
            minStack.add(val);
        }
        else
        {
            minStack.add(Math.min(val,minStack.get(minStack.size()-1)));
        }
        stack.add(val);
    }
    
    public void pop() 
    {
        stack.remove(stack.size() - 1);
        minStack.remove(minStack.size() - 1);
    }
    
    public int top() 
    {
        return stack.get((stack.size() - 1));
    }
    
    public int getMin() 
    {
        return minStack.get((minStack.size() - 1));
    }
}
