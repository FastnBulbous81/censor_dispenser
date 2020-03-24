# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
#email_one = open("email_one.txt", "r").read()
#email_two = open("email_two.txt", "r").read()
#email_three = open("email_three.txt", "r").read()
#email_four = open("email_four.txt", "r").read()

#====To do:====
#Using the list of "negative" words. Censor all occurances of "negative" words after any of the words in the "negative_words" list has been used twice.  Also censor using the "proprietary_terms" list.

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

# Converts email to list of each word if needed
    def to_list(self):
        email_list1 = [word for word in self.email.split(" ")]
        email_list2 = []
        email_list3 = []
        for element in email_list1:
            new_str = element.splitlines(keepends=True)
            email_list2.append(new_str)
        for element in email_list2:
            for sub in element:
                email_list3.append(sub)
        return email_list3

#Censors with individual string as input
class Censor:
    def __init__(self, censor_txt):
        self.censor_txt = censor_txt

    def to_censor(self, email):
        email_string = email.to_string()
        print(email_string.replace(self.censor_txt, "**********"))

#Censors with list of strings as input
class MultiCensor:
    def __init__(self, censor_list):
        self.censor_list = censor_list

#Censors words taken from list of strings
    def list_censor(self, email):
        email_string = email.to_string()
        for string in self.censor_list:
            email_string = email_string.replace(string, "************")
        print(email_string)

#Censors words taken from list of strings but misses the first x occurances of a word
    def delayed_censor(self, email):
        email_list = email.to_list()
        #print("Censoring " + str(email_list))
        new_email = []
        censored_words = []
        skipped_words = []
        delay = 2
        for word in email_list:
            if delay > 0:
                #print("Checking if " + str(word).lower() + " in censor_list")
                if word.lower() in self.censor_list:
                    delay -= 1
                    skipped_words.append(word)
                new_email.append(word)
            elif delay == 0:
                if str(word).lower() in self.censor_list:
                    new_email.append("***********")
                    censored_words.append(word)
                elif str(word).lower() not in self.censor_list:
                    new_email.append(word)
        print("Skipped the words: " + str(skipped_words))
        print("Censored the words: " + str(censored_words))
        print(new_email)



        #final_email = email_string
        #print(final_email)

email_one = Email("email_one.txt")
email_two = Email("email_two.txt")
email_three = Email("email_three.txt")
email_four = Email("email_four.txt")

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
censor_list1 = MultiCensor(negative_words)
censor_list1.delayed_censor(email_three)

#email_three.to_list()

#censor_txt1 = Censor("learning algorithms")
#censor_txt1.to_censor(email_one)

#proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms", "her", "herself"]
#censor_list1 = MultiCensor(proprietary_terms)
#censor_list1.list_censor(email_two)
