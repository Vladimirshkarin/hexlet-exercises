class PasswordValidator():
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
        }
    # BEGIN (write your solution here)


    # END

    # BEGIN reference solution


    # END reference solution

    def _has_number(self, password):
        return any(char.isdigit() for char in password)
