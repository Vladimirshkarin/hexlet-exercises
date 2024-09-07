class PasswordValidator():
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
        }
    ERRORS = {

    }
    # BEGIN (write your solution here)

    def __init__(self, **options):
        self.options = {**self.OPTIONS, **options}

    def validate(self, password):
        self.ERRORS = {}
        if self.options['min_len'] > len(password):
            self.ERRORS['min_len'] = 'too small'

        if self.options['contain_numbers'] and not self._has_number(password):
            self.ERRORS['contain_numbers'] = (
                'should contain at least one number'
            )

        return self.ERRORS
    # END

    # BEGIN reference solution
    # def __init__(self, **options):
    #     self.options = PasswordValidator.OPTIONS | options

    # def validate(self, password):
    #     errors = {}
    #     if len(password) < self.options['min_len']:
    #         errors['min_len'] = 'too small'
    #     if self.options['contain_numbers'] and not self._has_number
    # (password):
    #         errors['contain_numbers'] = 'should contain at least one number'
    #     return errors
    # END reference solution

    def _has_number(self, password):
        return any(char.isdigit() for char in password)
