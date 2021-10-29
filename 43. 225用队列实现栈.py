#请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。
#实现 MyStack 类：
#void push(int x) 将元素 x 压入栈顶。
#int pop() 移除并返回栈顶元素。
#int top() 返回栈顶元素。
#boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。
#注意：
#你只能使用队列的基本操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
#你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
#示例：
#输入：
#["MyStack", "push", "push", "top", "pop", "empty"]
#[[], [1], [2], [], [], []]
#输出：
#[null, null, null, 2, 2, false]
#解释：
#MyStack myStack = new MyStack();
#myStack.push(1);
#myStack.push(2);
#myStack.top(); // 返回 2
#myStack.pop(); // 返回 2
#myStack.empty(); // 返回 False
class MyStack:

    def __init__(self):
        self.queue_in = collections.deque()
        self.queue_out = collections.deque()


    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return self.queue_out.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.queue_in[-1]

    def empty(self) -> bool:
        return len(self.queue_in) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
