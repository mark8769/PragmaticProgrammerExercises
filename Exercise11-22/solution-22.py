import re

def is_camel_case(string):
    pattern = r'^[a-zA-Z]+([A-Z][a-z]+)+$'
    return bool(re.match(pattern, string))


def generate_report(filepath):
    print("Generating report...")
    pass
    
    
if __name__ == "__main__":
    print("Hello world")
