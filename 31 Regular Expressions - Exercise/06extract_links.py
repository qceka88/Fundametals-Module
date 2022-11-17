import re


class Regex:

    def __init__(self, some_text):
        self.some_text = some_text

    def regex_action(self):
        match = re.search(r'(w{3}\.)([A-Za-z0-9\-)]+\.)([a-z]+\.?)+', self.some_text)
        if match:
            return match.group()


class Links:

    def __init__(self, string):
        self.string = string

    def extracting(self):
        extracted_link = Regex(self.string)
        return extracted_link.regex_action()

    def printing(self):
        if self.extracting():
            print(self.extracting())


input_string = input()

while input_string:
    result = Links(input_string)
    result.printing()
    input_string = input()


#################################### TASK CONDITION ############################
"""
                            6.	*Extract the Links
Write a program that extracts links from a given text. The text will come in the form 
of strings, each representing a sentence. You need to extract only the valid links from it. 

Example:

                 "www    .       internet       .            com"
          Sub-Domain			 Domain name		        Domain extension
          
The Sub-Domain must always be "www". The Domain name can consist of English alphabet 
letters (uppercase and lowercase), digits, and dashes ("–"). The Domain extension 
consists of one or more domain blocks, a domain block consists of a dot followed by 
one or more lowercase English alphabet letters, 
a Domain extension must have at least one domain block in order to be valid. 
The Sub-Domain and Domain name must be separated by a single dot. Any link that does 
NOT follow the specified above rules should be treated as invalid.
Example incorrect links:  
•	"ww.justASite.bg"
•	"lel.awesome.com"
•	"www.weird_site.hit.bg"
•	"www.no-symb#^ols-allow%ed.com"
•	"www.mark.12"
•	"www.web-site."
•	"www.example-site._*^#"
Example of correct links:  
•	"Some textwww.softuni.bg"
•	"Just a link in a www.sea-of-text.bg-swimming around"
•	"Instruments www.Instruments.rom.com.trombone2000 Instrument here"
•	"All your ice cream flavors-www.scream.for.ice.cream(We  also have squirrels)"
 The output is all valid links you have found, printed – each on a new line.

____________________________________________________________________________________________
Example_01

Input
Join WebStars now for free, at www.web-stars.com 
You can also support our partners:
Internet - www.internet.com
WebSpiders - www.webspiders101.com
Sentinel - www.sentinel.-ko	

Output
www.web-stars.com
www.internet.com
www.webspiders101.com

____________________________________________________________________________________________
Example_02

Input
Need information about cheap hotels in London?
You can check us at www.london-hotels.co.uk !
We provide the best services in London.
Here are some reviews in some blogs:
London Hotels are awesome! - www.indigo.bloggers.com 
I am very satisfied with their services - ww.ivan.bg
Best Hotel Services! - www.rebel21.sedecrem.moc

Output
www.london-hotels.co.uk
www.indigo.bloggers.com
www.rebel21.sedecrem.moc

"""
