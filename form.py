class Form:
    def __init__(self, json):
        """ Create a form with the given JSON structure. """
        self.json = json
        self.done = False

    def _print_tag(self, function_name: str):
        text = f"Calling function '{function_name}' ..."
        print(f"\033[1;34m{text}\033[0m")

    def read(self):
        """ Return the current JSON structure of the form. """
        
        text = "read"
        self._print_tag(text)
        return self.json
    
    def write(self, path, value):
        """ Write a value to the form at the given JSON path. Pass both the dictionary path and the new value as arguments. """
        
        
        text = "write"
        self._print_tag(text)

        keys = path.split('.')
        d = self.json
        for key in keys[:-1]:
            if key not in d or not isinstance(d[key], dict):
                d[key] = {}
            d = d[key]
        d[keys[-1]] = value
        return f"Successfully wrote {value} to {path}."
    
    def mark_done(self):
        """ Mark the form as done. """

        text = "mark_done"
        self._print_tag(text)

        self.done = True
        return "Form marked as done."