import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Category, Task

categories = [
    {'name': 'Algorithms', 'description': 'Sorting, searching, and classic algorithm problems', 'icon': 'Alg'},
    {'name': 'Data Structures', 'description': 'Arrays, trees, graphs, and more', 'icon': 'DS'},
    {'name': 'SQL', 'description': 'Database queries and optimization', 'icon': 'SQL'},
    {'name': 'Python', 'description': 'Python-specific coding challenges', 'icon': 'Py'},
]

for c in categories:
    cat, _ = Category.objects.get_or_create(name=c['name'], defaults=c)

tasks = [
    # Algorithms
    {'category': 'Algorithms', 'title': 'Two Sum', 'difficulty': 'easy',
     'description': 'Given an array of integers nums and an integer target, return indices of two numbers that add up to target.',
     'examples': 'Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]'},
    {'category': 'Algorithms', 'title': 'Binary Search', 'difficulty': 'easy',
     'description': 'Given a sorted array and a target, return the index of the target or -1.',
     'examples': 'Input: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4'},
    {'category': 'Algorithms', 'title': 'Merge Sort', 'difficulty': 'medium',
     'description': 'Implement the merge sort algorithm.',
     'examples': 'Input: [38, 27, 43, 3]\nOutput: [3, 27, 38, 43]'},
    {'category': 'Algorithms', 'title': 'Longest Common Subsequence', 'difficulty': 'hard',
     'description': 'Given two strings, find the length of their longest common subsequence.',
     'examples': 'Input: text1 = "abcde", text2 = "ace"\nOutput: 3'},
    {'category': 'Algorithms', 'title': 'Valid Parentheses', 'difficulty': 'easy',
     'description': 'Given a string containing just (), {}, [], determine if valid.',
     'examples': 'Input: s = "()[]{}" \nOutput: true'},
    # Data Structures
    {'category': 'Data Structures', 'title': 'Implement Stack', 'difficulty': 'easy',
     'description': 'Implement a stack with push, pop, top, and empty operations.',
     'examples': 'stack.push(1)\nstack.top() -> 1\nstack.pop() -> 1'},
    {'category': 'Data Structures', 'title': 'LRU Cache', 'difficulty': 'hard',
     'description': 'Design and implement a data structure for Least Recently Used cache.',
     'examples': 'cache = LRUCache(2)\ncache.put(1, 1)\ncache.get(1) -> 1'},
    {'category': 'Data Structures', 'title': 'Binary Tree Traversal', 'difficulty': 'medium',
     'description': 'Implement inorder, preorder, and postorder traversals.',
     'examples': 'Input: root = [1,null,2,3]\nOutput: [1,3,2]'},
    {'category': 'Data Structures', 'title': 'Graph BFS', 'difficulty': 'medium',
     'description': 'Implement Breadth First Search on a graph.',
     'examples': 'Input: graph = {1:[2,3], 2:[4]}, start=1\nOutput: [1,2,3,4]'},
    {'category': 'Data Structures', 'title': 'Linked List Reverse', 'difficulty': 'easy',
     'description': 'Reverse a singly linked list.',
     'examples': 'Input: 1->2->3->4->5\nOutput: 5->4->3->2->1'},
    # SQL
    {'category': 'SQL', 'title': 'Select All Employees', 'difficulty': 'easy',
     'description': 'Write a query to select all employees from the Employees table.',
     'examples': 'SELECT * FROM Employees;'},
    {'category': 'SQL', 'title': 'Join Tables', 'difficulty': 'medium',
     'description': 'Write a query to join Employees and Departments tables.',
     'examples': 'SELECT e.name, d.name FROM Employees e JOIN Departments d ON e.dept_id=d.id'},
    {'category': 'SQL', 'title': 'Group By Salary', 'difficulty': 'medium',
     'description': 'Find the average salary per department.',
     'examples': 'SELECT dept_id, AVG(salary) FROM Employees GROUP BY dept_id'},
    {'category': 'SQL', 'title': 'Subquery', 'difficulty': 'hard',
     'description': 'Find employees with salary above the company average.',
     'examples': 'SELECT * FROM Employees WHERE salary > (SELECT AVG(salary) FROM Employees)'},
    {'category': 'SQL', 'title': 'Window Functions', 'difficulty': 'hard',
     'description': 'Rank employees by salary within each department.',
     'examples': 'SELECT name, RANK() OVER (PARTITION BY dept ORDER BY salary DESC) as rank FROM Employees'},
    # Python
    {'category': 'Python', 'title': 'List Comprehension', 'difficulty': 'easy',
     'description': 'Use list comprehension to return squares of even numbers from a list.',
     'examples': 'Input: [1,2,3,4,5]\nOutput: [4, 16]'},
    {'category': 'Python', 'title': 'Decorator Pattern', 'difficulty': 'medium',
     'description': 'Write a timing decorator that measures function execution time.',
     'examples': '@timer\ndef slow_function():\n    time.sleep(1)'},
    {'category': 'Python', 'title': 'Generator Function', 'difficulty': 'medium',
     'description': 'Write a generator that yields Fibonacci numbers.',
     'examples': 'gen = fibonacci()\nnext(gen) -> 0\nnext(gen) -> 1'},
    {'category': 'Python', 'title': 'Context Manager', 'difficulty': 'hard',
     'description': 'Implement a custom context manager using __enter__ and __exit__.',
     'examples': 'with MyContextManager() as cm:\n    pass'},
    {'category': 'Python', 'title': 'String Manipulation', 'difficulty': 'easy',
     'description': 'Reverse words in a string.',
     'examples': 'Input: "hello world"\nOutput: "world hello"'},
]

for t in tasks:
    cat = Category.objects.get(name=t['category'])
    Task.objects.get_or_create(
        title=t['title'],
        defaults={
            'category': cat,
            'description': t['description'],
            'examples': t['examples'],
            'difficulty': t['difficulty'],
        }
    )

print(f"Seeded {Category.objects.count()} categories and {Task.objects.count()} tasks!")
