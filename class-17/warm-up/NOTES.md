# Find Age Range in Tree

```python
from codefellows.dsa.binary_tree import BinaryTree


def get_age_range(people_tree):
    
    if not people_tree.root: 
        return 0

    def walk(root, youngest=0, oldest=0):
        if not root:
            return youngest, oldest

        if root.value.age < youngest:
            youngest = root.value.age
        elif root.value.age > oldest:
            oldest = root.value.age

        youngest, oldest = walk(root.left, youngest, oldest)
        youngest, oldest = walk(root.right, youngest, oldest)

        return youngest, oldest

    first_person = people_tree.root.value

    youngest,oldest = walk(people_tree.root, first_person.age, first_person.age)

    return oldest - youngest

class Person:
    def __init__(self, age):
        self.age = age

tree = BinaryTree(values=[
    Person(12),
    Person(33),
    Person(44),
    Person(98),
])

assert get_age_range(tree) == 86
assert get_age_range(BinaryTree()) == 0

print("TESTS PASSED")
```

