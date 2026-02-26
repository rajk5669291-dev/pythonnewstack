class school:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.SSLC_Mark = int(input("Enter your 10th Mark: "))
        self.stream = None   # default value

    def group(self):
        if self.SSLC_Mark > 400:
            print("You are going to Group1")
            self.stream = "Group1"

        elif self.SSLC_Mark > 300:
            print("You are going to Group2")
            self.stream = "Group2"

        elif self.SSLC_Mark >= 200:
            print("You are going to Group3")
            self.stream = "Group3"

        else:
            print("Marks too low for group allocation")

        self.HSC_Mark = int(input("Enter your 12th Mark: "))


class college(school):
    def courses(self):
        if self.stream == "Group1" and self.HSC_Mark > 500:
            print("You are eligible to become a Doctor or Engineer")

        elif self.stream == "Group2" and self.HSC_Mark > 500:
            print("You are eligible to become a Nurse or Teacher")

        elif self.stream == "Group3" and self.HSC_Mark > 500:
            print("You are eligible to become a Manager or Accountant")

        elif self.stream == "Group3" and 400 < self.HSC_Mark <= 500:
            print("You are eligible to become a Sales Executive or Clerk")

        elif self.stream == "Group2" and 400 < self.HSC_Mark <= 500:
            print("You are eligible to become a Pharmacy or Bio Technician")

        elif self.stream == "Group1" and 400 < self.HSC_Mark <= 500:
            print("You are eligible to become a Microbiology or Biotechnology student")

        else:
            print("Not eligible for listed courses")


ramesh = college()
ramesh.group()
ramesh.courses()
