# Private attributes are created using double underscore (__)

class Account:
    def __init__(self, account_id, account_pass):
        self.account_id = account_id          # public attribute
        self.__account_pass = account_pass    # private attribute

    def reset_pass(self):
        # Private attribute can be accessed inside the class
        print(self.__account_pass)


acc1 = Account("12345", "adsvfnrf")

print(acc1.account_id)     # ✅ Allowed (public)
acc1.reset_pass()          # ✅ Allowed (access through method)

# print(acc1.__account_pass)   ❌ ERROR (private attribute)
