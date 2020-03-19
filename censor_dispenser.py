# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
#email_one = open("email_one.txt", "r").read()
#email_two = open("email_two.txt", "r").read()
#email_three = open("email_three.txt", "r").read()
#email_four = open("email_four.txt", "r").read()

#=====Censor "learning algorithms" from email_one.txt======

#Things to watch out for:
# - When censor_txt is more than one word, the program will need to be able to skip past accurances of individual the words in censor_txt.
# - Program needs to work on words that have puntuation at the end

class Email:
#.__init__ opens text file using self.file variable
    def __init__(self, file):
        self.file = file
        self.email = open(self.file, "r").read()

class Censor:
    def __init__(self):
        
    def to_censor(self, email):
        self.email = email




email_one = Email("email_one.txt")

censor_txt1 = Censor("learning algorithms")
censor_txt1.to_censor(email_one)
