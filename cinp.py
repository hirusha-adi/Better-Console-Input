__author__ = "@hirushaadi"
__version__ = "v2"
__license__ = "MIT"

import sys
import getpass
import threading

def simple_prompt(prompt_text):
    return input(prompt_text)

def decorated_prompt(prompt_text):
    decorated_text = f"*** {prompt_text} ***"
    return input(decorated_text)

def numbered_prompt(prompt_text, number):
    numbered_text = f"{number}. {prompt_text}"
    return input(numbered_text)

def uppercase_prompt(prompt_text):
    uppercase_text = prompt_text.upper()
    return input(uppercase_text)

def warning_prompt(prompt_text):
    warning_text = f"⚠️  {prompt_text} ⚠️"
    return input(warning_text)

def multiline_prompt(prompt_text, lines=3):
    print(prompt_text)
    inputs = []
    for i in range(lines):
        line_input = input(f"Line {i + 1}: ")
        inputs.append(line_input)
    return "\n".join(inputs)

def confirm_prompt(prompt_text):
    while True:
        response = input(f"{prompt_text} (yes/no): ").strip().lower()
        if response in ['yes', 'no']:
            return response == 'yes'
        else:
            print("Please enter 'yes' or 'no'.")

def hidden_prompt(prompt_text):
    return getpass.getpass(prompt_text)

def choice_prompt(prompt_text, choices):
    choice_text = f"{prompt_text} ({'/'.join(choices)}): "
    while True:
        response = input(choice_text).strip().lower()
        if response in choices:
            return response
        else:
            print(f"Please choose from {', '.join(choices)}.")

def validated_prompt(prompt_text, validation_func, error_message="Invalid input"):
    while True:
        response = input(prompt_text)
        if validation_func(response):
            return response
        else:
            print(error_message)

def timeout_prompt(prompt_text, timeout=10):
    print(f"{prompt_text} (You have {timeout} seconds to respond)")

    def input_with_timeout():
        sys.stdin.flush()
        try:
            response = input()
            return response
        except EOFError:
            return None

    timer = threading.Timer(timeout, lambda: sys.stdin.write("\n"))
    timer.start()
    response = input_with_timeout()
    timer.cancel()

    if response is None:
        print("Timeout!")
    return response

def list_prompt(prompt_text, end_text="done"):
    print(f"{prompt_text} (type '{end_text}' to finish)")
    inputs = []
    while True:
        response = input()
        if response.strip().lower() == end_text:
            break
        inputs.append(response)
    return inputs
