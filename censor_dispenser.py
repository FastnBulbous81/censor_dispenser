# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
#email_one = open("email_one.txt", "r").read()
#email_two = open("email_two.txt", "r").read()
#email_three = open("email_three.txt", "r").read()
#email_four = open("email_four.txt", "r").read()

#====To do:====
#Create functionality that can censor all words from a list.
#proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

class Email:
#.__init__ opens text file using self.file variable
    def __init__(self, file):
        self.file = file
        self.email = open(self.file, "r").read()
# method makes string from email available
    def to_string(self):
        email_string = ""
        email_string += self.email
        return email_string

class Censor:
    def __init__(self, censor_txt):
        self.censor_txt = censor_txt

    def to_censor(self, email):
        censor_string = email.to_string()
        print(censor_string.replace(self.censor_txt, "**********"))


email_one = Email("email_one.txt")
censor_txt1 = Censor("learning algorithms")

censor_txt1.to_censor(email_one)
