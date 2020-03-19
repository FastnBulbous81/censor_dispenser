# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
#email_one = open("email_one.txt", "r").read()
#email_two = open("email_two.txt", "r").read()
#email_three = open("email_three.txt", "r").read()
#email_four = open("email_four.txt", "r").read()

#Censor "learning algorithms" from email_one.txt


class Email:
#.__init__ opens text file using self.file variable
    def __init__(self, file):
        self.file = file
        self.email = open(self.file, "r").read()

#splits email into list with each word as an element
    def to_list(self):
        to_split = ""
        to_split += self.email
        splitted = to_split.split()
        return splitted

class Censor:
#.init takes string variable of words to censor and splits into list
    def __init__(self, censor_txt):
        self.censor_txt = censor_txt.split()

#Counts number of consecutive words to censor and iterates through list to get indexs of text to censor
    def to_censor(self, email):
        self.email = email
        word_count = len(self.censor_txt)
        while word_count > 0:
            indexs = []
            for i in range(len(email)):
                if email[i] == self.censor_txt[0]:
                    indexs.append(i)
            print(indexs)
            word_count = 0



email_one = Email("email_one.txt")

censor_txt1 = Censor("learning algorithms")
censor_txt1.to_censor(email_one.to_list())