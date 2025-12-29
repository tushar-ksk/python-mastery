class person:
    job = "programing"
    salary = 50000
    def info(self):
        print(f"{self.name} get ${self.salary} per year because he uses {self.lang} for {self.job}")
    @staticmethod
    def greet():
        print("good morning")

    def greet2(self):
        print(f"good morning {self.name}")


ramfal = person()
ramfal.name = "Ramfal"
ramfal.lang = "Assembly"

ramfal.info()
ramfal.greet()
ramfal.greet2()