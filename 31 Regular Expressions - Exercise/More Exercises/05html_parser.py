##################################### variant 01 #####################################
import re


class Regex:

    def __init__(self, some_pattern, some_text):
        self.some_text = some_text
        self.some_pattern = some_pattern

    def magic_regex(self):
        regex_match = re.findall(self.some_pattern, self.some_text)
        return regex_match


class Extract:
    __content_magic = r'>([^<>]*)<?'
    __title_magic = r'<title>(.+)<\/title>'

    def __init__(self, some_string):
        self.some_string = some_string

    def title_extract(self):
        title_object = Regex(Extract.__title_magic, self.some_string).magic_regex()
        return title_object[0]

    def content_extract(self):
        content_object = Regex(Extract.__content_magic, self.some_string).magic_regex()
        content = ''
        for part in content_object:
            if part != self.title_extract():
                part = part.replace('\\n', '')
                content += part.strip() + ' '
        return content

    def return_to_main(self):
        return (self.title_extract(), self.content_extract())


class Main:

    def __init__(self):
        self.some_input = input()

    def separate_data(self):
        data = Extract(self.some_input)
        separated_data = data.return_to_main()
        return separated_data

    def __repr__(self):
        title, content = self.separate_data()
        return f'Title: {title}\nContent: {content.strip()}'


print(Main())

##################################### variant 02 #####################################
import re

input_line = input()
title_pattern = r'<title>(.+)<\/title>'
match_title = re.search(title_pattern, input_line)
content_pattern = r'>([^<>]*)<?'
match_content = re.findall(content_pattern, input_line)
content = ''

for part in match_content:
    if part != match_title.group(1):
        part = part.replace('\\n', '')
        content += part.strip() + ' '

print(f"Title: {match_title.group(1)}")
print(f'Content: {content.strip()}')


#################################### TASK CONDITION ############################
"""
                            5.	HTML Parser
Write a program that extracts a title and all the content of a HTML file:
•	The title should be between the HTML tags <title> and <\title>. 
•	The content should be between the HTML tags <body> and <\body>.
There might be different HTML tags, which you should ignore: 
•	Each HTML tag is surrounded by the symbols "<" and ">". For example: <body>, <p>, <\html>
•	You also should ignore the HTML tag "\n"

>>>>>>>> Example is on a single line. Here is separated on multiple rows for easy reading <<<<<<<<
 
Example:
"<html>\n<head><title>News</title></head>\n<body><p><a href="https://softuni.bg">SoftUni</a>
aims to provide free real-world practical\n training for young people who want to turn into
\n skillful Python software engineers.</p></body>\n</html>"
In this example the title is "News" and the content is "SoftUni aims to provide free real-world 
practical training for young people who want to turn into skillful Python software engineers."

Input
•	The input will be read from the console. 
•	The input consists of a single line.

Output
•	The content should be a single string. 
•	You should extract only the text without the tags. 
•	When you extract the title and the content, you should print the result in the following format:
o	"Title: {extracted title}"
o	"Content: {extracted content}"

____________________________________________________________________________________________
Example

>>>>>>>> Input must be on a single line. Here is separated on two rows for easy reading <<<<<<<<
Input
<html>\n<head><title>Some title</title></head>\n<body>Here<p> is some 
</p>content <a href="www.somesite.com">\nclick</body>\n</html>

Output (must be on two rows) 
Title: Some title
Content: Here is some content click

Explanation
We take the title and ignore all the tags to get the content

"""
