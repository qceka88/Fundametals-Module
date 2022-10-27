class Comment:

    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


# Part below is test code from example

comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)


#################################### TASK CONDITION ############################
'''
                     1.	Comment
Create a class with the name "Comment". The __init__ method should accept 3 parameters:
•	username
•	content
•	likes (optional, 0 by default)
Use the exact names for your variables
Note: there is no input/output for this problem. Test the class yourself and submit only the class

_______________________________________________
Example

Test Code	(no input data in this task)

comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)	


Output
user1
I like this book
0

'''
