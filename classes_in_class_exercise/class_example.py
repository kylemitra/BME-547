class Person:

    def __init__(self, first_name_arg, last_name_arg,
                 age_arg, gender_arg=None):
        self.first_name = first_name_arg
        self.last_name = last_name_arg
        self.age = age_arg
        self.age_in_ten_years = self.age + 10
        self.gender = gender_arg # setting = None in argument makes it a non-mandatory argument

    def get_fill_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name

    def is_minor(self):
        if self.age < 18:
            return True
        else:
            return False

    def is_minor_in_ten_years(self):
        if self.age_in_ten_years < 18:
            return True
        else:
            return False


def main():
    new_person = Person("Ann", "Ables", 35)
    old_person = Person("Bob", "Boyles", 40)
    x = Person("Chris", "Cunningham", 15)
    print(new_person.get_fill_name())
    print(x.is_minor())
    print(x.is_minor_in_ten_years())
    new_patient = Person("Debra", "Doolittle", 40, "Female")

    db = list()
    db.append(new_patient)
    new_patient = Person("Elliot", "Eisenhower", 30, "Male")
    db.append(new_patient)
    new_patient = Person("Frank", "Fortune", 30, "Male")
    print(db)
    print(db[1].get_fill_name())


if __name__ == "__main__":
    main()
