# Better console input

cinp.py is a Python module that provides a collection of customizable prompt functions for interactive console input. With cinp.py, you can easily prompt users for input in various styles, from simple text prompts to decorated prompts with warnings and validations.

### Usage

1. **Installation**:
   - Download the `cinp.py` file or clone the repository.
   - Place the `cinp.py` file in your project directory.

2. **Import**:
   - Import the required prompt functions into your Python script using:
     ```python
     from cinp import simple_prompt, decorated_prompt, numbered_prompt, uppercase_prompt, warning_prompt, multiline_prompt, confirm_prompt, hidden_prompt, choice_prompt, validated_prompt, timeout_prompt, list_prompt
     ```

3. **Usage**:
   - Use the imported prompt functions to interact with the user and collect input data.

### Features

1. **Simple Prompt**:
   - Prompt the user for input with basic text.

2. **Decorated Prompt**:
   - Add decorative characters around the prompt text for emphasis.

3. **Numbered Prompt**:
   - Number prompts for sequence or context.

4. **Uppercase Prompt**:
   - Display prompts in uppercase letters.

5. **Warning Prompt**:
   - Display prompts with a warning symbol for attention.

6. **Multiline Prompt**:
   - Allow users to input multiple lines of text.

7. **Confirm Prompt**:
   - Ask for yes or no confirmation from the user.

8. **Hidden Prompt**:
   - Hide user input (useful for passwords).

9. **Choice Prompt**:
   - Offer a selection of choices for the user to pick from.

10. **Validated Prompt**:
    - Ensure the input meets specific criteria with custom validation functions.

11. **Timeout Prompt**:
    - Limit the time the user has to provide input.

12. **List Prompt**:
    - Collect multiple inputs until the user indicates they are done.

### Example

```python
from cinp import simple_prompt, decorated_prompt, numbered_prompt, uppercase_prompt, warning_prompt, multiline_prompt, confirm_prompt, hidden_prompt, choice_prompt, validated_prompt, timeout_prompt, list_prompt

# Example usage:
print("Simple Prompt:")
print(simple_prompt("Enter your name: "))

print("\nDecorated Prompt:")
print(decorated_prompt("Enter your age: "))

print("\nNumbered Prompt:")
print(numbered_prompt("Enter your email: ", 1))

print("\nUppercase Prompt:")
print(uppercase_prompt("Enter your city: "))

print("\nWarning Prompt:")
print(warning_prompt("Enter your phone number: "))

print("\nMultiline Prompt:")
print(multiline_prompt("Describe yourself:", 3))

print("\nConfirm Prompt:")
print(confirm_prompt("Do you accept the terms and conditions?"))

print("\nHidden Prompt:")
print(hidden_prompt("Enter your password: "))

print("\nChoice Prompt:")
print(choice_prompt("Choose your favorite color", ["red", "blue", "green"]))

print("\nValidated Prompt (only numbers):")
print(validated_prompt("Enter a number: ", lambda x: x.isdigit(), "Please enter a valid number."))

print("\nTimeout Prompt:")
print(timeout_prompt("You have limited time to answer: ", 5))

print("\nList Prompt:")
print(list_prompt("Enter items for your list: "))
```

README.md file generated with ChatGPT on `6/7/2024`
