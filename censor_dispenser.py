import re

class Email:
    def __init__(self, file):
        self.file = file
        self.email = open(self.file, "r").read()

#-------Makes string from email available
    def to_string(self):
        email_string = ""
        email_string += self.email
        return email_string

#-------Converts email to list of each word, \n and puntuation
    def to_list(self):
        email_list1 = [word for word in self.email.split(" ")]
        email_list2 = []
        for element in email_list1:
            p_split = re.findall(r"[\w]+|[().,?!''\n]", element)
            email_list2.append(p_split)
        email_list3 = []
        for element in email_list2:
            for sub in element:
                email_list3.append(sub)
        return email_list3

#-------Censors with individual string as input
class Censor:
    def __init__(self, censor_txt):
        self.censor_txt = censor_txt

    def to_censor(self, email):
        email_string = email.to_string()
        print(email_string.replace(self.censor_txt, "**********"))

#------Censors with list of strings as input
class MultiCensor:
    def __init__(self, censor_list):
        self.censor_list = censor_list

#------Censors words taken from list of strings
    def list_censor(self, email):
        email_string = email.to_string()
        for string in self.censor_list:
            email_string = email_string.replace(string, "************")
        print(email_string)

#-----Censors words taken from list of strings but misses the first x occurances of a word
    def delayed_censor(self, email):
        email_list = email.to_list()
        new_email_list = []
        skipped_words = []
        censored_words = []
        delay = 2
        for word in email_list:
            if delay > 0:
                if word.lower() in self.censor_list:
                    delay -= 1
                    skipped_words.append(word)
                    new_email_list.append(word)
                else:
                    new_email_list.append(word)
            elif delay == 0:
                if word.lower() in self.censor_list:
                    censored_words.append(word)
                    new_email_list.append("***********")
                else:
                    new_email_list.append(word)
        new_email = " ".join(email_list).replace(" .", ".").replace(" ,", ",")\
            .replace(" !", "!").replace(" ?", "?").replace("\n ", "\n")\
            .replace(" \' ", "\'").replace(" * ", "*")
        print(new_email)
#Uncomment to show words being skipped:
#        print("Skipped the words: " + str(skipped_words))
#Uncomment to show words that have been censored:
#       print("Censored the words: " + str(censored_words))

#------Censors words in list including words before and after the censored words
    def before_after(self, email):
        email_list = email.to_list()
        punc_idxs = []
        censor_idxs = []
        for i in range(len(email_list)):
            if email_list[i] in [".", ",", "!", "?", "\n"]:
                punc_idxs.append(i)
            elif email_list[i].lower() in self.censor_list:
                censor_idxs.append(i)
                email_list[i] = "**********"
                if email_list[i+1] in "\'":
                    email_list[i+1] = "*"
                    email_list[i+2] = "*"
                    email_list[i+3] = " *********"
        for idx in censor_idxs:
            right_idx = idx + 1
            left_idx = idx - 1
            while right_idx in punc_idxs:
                right_idx += 1
            email_list[right_idx] = "**********"
            if email_list[right_idx+1] in "\'":
                email_list[right_idx+1] = "*"
                email_list[right_idx+2] = "*"
            while left_idx in punc_idxs:
                left_idx -= 1
            email_list[left_idx] = "**********"
        new_email = " ".join(email_list).replace(" .", ".").replace(" ,", ",")\
            .replace(" !", "!").replace(" ?", "?").replace("\n ", "\n")\
            .replace(" \' ", "\'").replace(" * ", "*")
        print(new_email)
#Uncomment below to see indices used by funtion
#        print("censor_idxs = " + str(censor_idxs))
#        print("punc_idxs = " + str(punc_idxs))

#-----Lists of strings used as inputs for censoring
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
combined_censor_list = proprietary_terms + negative_words

#To view censored email_four
email_four = Email("email_four.txt")
censor_list3 = MultiCensor(combined_censor_list)
censor_list3.before_after(email_four)
#Original email
print(email_four.to_string())


#To view censored email_three using delayed sensor that skips the first 2 occurences
#email_three = Email("email_three.txt")
#censor_list2 = MultiCensor(negative_words)
#censor_list2.delayed_censor(email_three)
#Original email
#print(email_three.to_string())


#Calls for email_two which is censored using a list of strings
#email_two = Email("email_two.txt")
#censor_list1 = MultiCensor(proprietary_terms)
#censor_list1.list_censor(email_two)
#Original email
#print(email_two.to_string())

#Email_one that uses a single string to censor
#email_one = Email("email_one.txt")
#censor_txt1 = Censor("learning algorithms")
#censor_txt1.to_censor(email_one)
#Original email
#print(email_one.to_string())
