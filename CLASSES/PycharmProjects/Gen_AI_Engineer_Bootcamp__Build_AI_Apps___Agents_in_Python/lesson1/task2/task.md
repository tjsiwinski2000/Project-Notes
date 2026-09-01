# Read a File and Ask AI

This script reads a list of coffee types from a text file and sends them to an AI model, asking which one is best for making espresso. It then prints the model's recommendation.

The starter code already has the import, the model setup, and the print statement. You need to complete two missing pieces:

1. Open the file `coffee.txt` and read its contents into a variable called `coffee`.
2. Invoke the model with the prompt `f"Which of these is best for making espresso: {coffee}"` and store the result in a variable called `response`.

The file `coffee.txt` is already included in this task — you do not need to create it.

**Important:** Replace `"YOUR_GOOGLE_API_KEY"` with your actual Google API key before running the code. Without a valid key the program will not be able to connect to the model.

<div class="hint">

Use a `with open('coffee.txt') as file:` block and call `file.read()` to get the contents.

</div>

<div class="hint">

Call `model.invoke(...)` and pass the f-string as the argument. Store the return value in `response`.

</div>
