# -*- coding: utf-8 -*-
"""
Spyder Editor
@author: nbrady
"""

from collections import deque

# Stores student info as well as it's left and right children
class Node:
    def __init__(self, studentID, name, major):
        self.studentID = studentID
        self.name = name
        self.major = major
        self.left = None
        self.right = None
        
# Stores the students in a binary search tree
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    # Add student based on ID
    def insert(self, studentID, name, major):
        newNode = Node(studentID, name, major)

        if self.root is None:
            self.root = newNode
            return True

        current = self.root
        
        # move left  or right until there is an open spot
        while True:
            if studentID == current.studentID:
                print("Student ID already exists.")
                return False
    
            elif studentID < current.studentID:
                if current.left is None:
                    current.left = newNode
                    return True
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = newNode
                    return True
                else:
                    current = current.right

    # search for student and store the path
    def search(self, studentID):
        current = self.root
        path = []
        count = 0

        while current is not None:
            path.append(str(current.studentID))
            count += 1
            
            if studentID == current.studentID:
                print("Student found:")
                print(current.studentID, current.name, current.major)
                break
            
            elif studentID < current.studentID:
                current = current.left
            else:
                current = current.right

        if current is None:
            print("Student was not found.")
            
        print("Path:", "->".join(path))
        print("Nodes checked: ", count)

    # root, left, right
    def preOrder(self, node):
        if node is not None:
            self.showStudent(node)
            self.preOrder(node.left)
            self.preOrder(node.right)

    # left, root, right
    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            self.showStudent(node)
            self.inOrder(node.right)

    # left, right, root
    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            self.showStudent(node)

    # displays the student
    def showStudent(self, node):
        print("ID:", node.studentID, "Name:", node.name, "Major:", node.major)

    # prints tree one level at a time
    def bfs(self):
        if self.root is None:
            print("The tree is empty.")
            return
        
        queue = deque()
        queue.append(self.root)
        level = 1

        while len(queue) > 0:
            levelSize = len(queue)
            
            print("level", level, end=": ")
            
            for i in range(levelSize):
                current = queue.popleft()
                print(current.studentID, current.name, "(" + current.major + ")", end = "  ")
                
                if current.left is not None:
                    queue.append(current.left)
                    
                if current.right is not None:
                    queue.append(current.right)
                    
            print()
            level += 1

    # count the nodes using recursion 
    def countStudents(self, node):
        if node is None:
            return 0
        
        return 1 + self.countStudents(node.left) + self.countStudents(node.right)

    # find longest path down the tree
    def treeHeight(self, node):
        if node is None:
            return 0
        
        leftHeight = self.treeHeight(node.left)
        rightHeight = self.treeHeight(node.right)
        
        return 1 + max(leftHeight, rightHeight)

    # smallest id is on the left
    def smallest(self):
        current = self.root
        
        while current.left is not None:
            current = current.left
            
        return current


    # largest id is on the right
    def largest(self):
        current = self.root
        
        while current.right is not None:
            current = current.right
            
        return current


# keep asking until they enter a whole number
def getID():
    while True:
        studentID = input("Enter student ID: ")
        try:
            return int(studentID)
        except ValueError:
            print("Invalid. Enter a whole number")


# ask for students information then add it
def addStudent(tree):
    studentID = getID()
    name = input("Enter student name: ")
    major = input("Enter student major: ")
    
    if tree.insert(studentID, name, major):
        print("Student added.")


# ask which student to search for
def searchStudent(tree):
    if tree.root is None:
        print("The tree is empty.")
        return
    
    studentID = getID()
    tree.search(studentID)


# choose 1 of 3 DFS orders
def displayDFS(tree):
    if tree.root is None:
        print("The tree is empty.")
        return
    
    print("1. Pre Order")
    print("2. In Order")
    print("3. Post Order")
    
    choice = input("Choose a traversal: ")
    
    if choice == "1":
        tree.preOrder(tree.root)
    elif choice == "2":
        tree.inOrder(tree.root)
    elif choice == "3":
        tree.postOrder(tree.root)
    else:
        print("Invalid choice.")

# show the students by level
def displayBFS(tree):
    if tree.root is None:
        print("The tree is empty.")
        return
    
    tree.bfs()

# show the number of students and tree height
def showStats(tree):
    if tree.root is None:
        print("The tree is empty.")
        return
    
    print("Total students:", tree.countStudents(tree.root))
    print("Tree height:", tree.treeHeight(tree.root))


# display students with lowest and highest ids
def showSmallestLargest(tree):
    if tree.root is None:
        print("The tree is empty.")
        return
    
    print("Smallest ID student: ")
    tree.showStudent(tree.smallest())
    
    print("Largest ID student:")
    tree.showStudent(tree.largest())

# display menu until the user exits (7)
def main():
    tree = BinarySearchTree()
    while True:
        print("Student Directory")
        print("1. Add new student")
        print("2. Search student by ID")
        print("3. Display students using DFS")
        print("4. Display students using BFS")
        print("5. Display Tree Stats")
        print("6. Display Smallest and largest IDs")
        print("7. Exit")

        choice = input("Choose an option (1 to 7): ")
        
        if choice == "1":
            addStudent(tree)
        elif choice == "2":
            searchStudent(tree)
        elif choice == "3":
            displayDFS(tree)
        elif choice == "4":
            displayBFS(tree)
        elif choice == "5":
            showStats(tree)
        elif choice == "6":
            showSmallestLargest(tree)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Enter a number from 1 to 7 ")

# run main
if __name__ == "__main__":
    main()
    
    
"""
Time complexity questions:
1.
For the first tree, if we search for 80 it checks 3 nodes.
For the second tree searching for 70 checks 7 nodes.
A balanced BST is O(log n) because it can skip parts of the tree, 
and an unbalanced BST can be O(n) because it might have to check every node.

2.
Adding one student to a balanced BST is O(log n) and adding n students
is O(n log n) because we just repeat that process n times. For 1000 students
it would take about 10000 steps.
"""