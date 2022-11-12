class TitleContent:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def title(self):
        title = f'<h1>\n{self.first}\n</h1>'
        return title

    def content(self):
        content = f'<article>\n{self.second}\n</article>'
        return content

    def __repr__(self):
        return f'{self.title()}\n{self.content()}'


class HtmlComments:

    def __init__(self, text):
        self.text = text

    def forming(self):
        return f'<div>\n{self.text}\n</div>'

    def __repr__(self):
        return self.forming()


first_line = input()
second_line = input()

title_article = TitleContent(first_line, second_line)

print(title_article)

while True:
    command = input()
    if command == 'end of comments':
        break
    comments = HtmlComments(command)
    print(comments)

#################################### TASK CONDITION ############################
"""
                         5.	HTML
You will receive lines of input:
•	On the first line, you will receive a title of an article
•	On the second line, you will receive the content of that article
•	On the following lines, until you receive "end of comments" you will get the comments about the article
Print the whole information in html format:
•	The title should be in "h1" tag (<h1></h1>)
•	The content in article tag (<article></article>)
•	Each comment should be in div tag (<div></div>)
For more clarification see the example below.


____________________________________________________________________________________________
Example

Input
SoftUni Article
Some content of the SoftUni article
some comment
more comment
last comment
end of comments

Output
<h1>
    SoftUni Article
</h1>
<article>
    Some content of the SoftUni article
</article>
<div>
    some comment
</div>
<div>
    more comment
</div>
<div>
    last comment
</div>

"""
