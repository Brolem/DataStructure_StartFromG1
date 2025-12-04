"""简单栈（使用 Python 列表模拟数组）"""

MAX_SIZE = 101  # 模拟固定大小数组

class Stack:
	def __init__(self):
		# 使用列表保存元素，top_index 指示栈顶位置，-1 表示空栈
		self.A = [0] * MAX_SIZE
		self.top = -1

	def push(self, x):
		"""将 x 放到栈顶；如果已满则打印错误（不抛异常）。"""
		if self.top >= MAX_SIZE - 1:
			print("Error: stack overflow")
			return
		self.top += 1
		self.A[self.top] = x

	def pop(self):
		"""弹出栈顶元素（不返回值），为空时打印错误。"""
		if self.top == -1:
			print("Error: No element to pop")
			return
		self.top -= 1

	def top_value(self):
		"""返回栈顶元素（不移除）。调用前应确保栈非空。"""
		if self.top == -1:
			print("Error: Stack is empty")
			return None
		return self.A[self.top]

	def print(self):
		"""从底到顶打印栈内容"""
		if self.top == -1:
			print("Stack is empty")
			return
		print("Stack:", end=' ')#不回车
		for i in range(0, self.top + 1):
			print(self.A[i], end=' ')
		print()

if __name__ == '__main__':
	stack = Stack()
	stack.push(5); stack.print()
	stack.push(10); stack.print()
	stack.pop(); stack.print()
	stack.push(12); stack.print()
	print(stack.top_value())