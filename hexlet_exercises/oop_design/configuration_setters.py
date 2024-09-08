# BEGIN (write your solution here)
class Truncater:
    OPTIONS = {
        "separator": "...",
        "length": 200,
    }

    def __init__(self, **options):
        self.OPTIONS = {**self.OPTIONS, **options}

    def truncate(self, string, **options):
        local_OPTIONS = {**self.OPTIONS, **options}
        if len(string) > local_OPTIONS["length"]:
            return string[: local_OPTIONS["length"]] + (
                local_OPTIONS["separator"]
            )
        else:
            return string
# END


# BEGIN reference solution
class Truncater_ref:
    OPTIONS = {
        "separator": "...",
        "length": 200,
    }

    def __init__(self, **options):
        self.options = {**self.OPTIONS, **options}

    def truncate(self, text, **options):
        current_options = {**self.options, **options}
        if len(text) <= current_options["length"]:
            return text
        substr = text[: current_options["length"]]
        return f"{substr}{current_options['separator']}"
# END reference solution
