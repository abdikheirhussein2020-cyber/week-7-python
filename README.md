# Week 7 Python Assignment — Lists

## Overview

This assignment demonstrates how to create, access, modify, and process lists in Python. It covers list indexing, adding and removing elements, loops, conditional statements, membership checks, counting items, and finding the longest item name.

## Files Included

### 1. `list_warmup.py`

This file demonstrates basic Python list operations.

- Creates a list containing four fruits.
- Prints the first and last items using indexes.
- Uses `append()` to add a fifth fruit.
- Uses `remove()` to remove a fruit.
- Uses `len()` to count the remaining fruits.

### 2. `shopping_list.py`

This file implements an interactive shopping list manager.

- Starts with an empty list.
- Uses a `while` loop to display a menu repeatedly.
- Allows users to add items using `append()`.
- Allows users to remove items from the list.
- Uses the `in` operator to check whether an item exists before removing it.
- Displays a helpful message when an item is not on the list.
- Uses a `for` loop to display every item on its own line.
- Exits the loop and displays a goodbye message when the user enters `done`.
- Handles invalid menu choices and empty item names without crashing.

### 3. `list_report.py`

This file generates a report from a predefined shopping list.

- Creates the list `["bread", "avocado", "milk", "sweet potatoes", "tea"]`.
- Prints each item with a number using a loop.
- Counts item names with more than four characters using a loop and an `if` statement.
- Finds the longest item name using a loop and a length comparison.

## Concepts Practiced

This assignment helped me practice the following Python concepts:

- Creating and modifying lists.
- Accessing list elements using positive and negative indexes.
- Using `append()`, `remove()`, and `len()`.
- Using `while` loops and `for` loops.
- Applying conditional statements with `if`, `elif`, and `else`.
- Checking whether an item exists using the `in` operator.
- Counting items that meet a condition.
- Comparing string lengths to find the longest item.
- Accepting user input and handling invalid choices.

## Error Handling and List Safety

In Python, calling the `remove()` method on a list with an item that does not exist raises a `ValueError`, which can cause the program to stop unexpectedly. In my `shopping_list.py` program, I use the `in` statement to check whether the item exists in the list before removing it. If the item is present, it is removed successfully; otherwise, the program displays the message "That item is not on your list." This check prevents the `ValueError` and allows the program to continue running safely.

## Expected Results

### Part A — List Warmup

The program should print the first and last fruits, display the list after adding and removing a fruit, and show the number of remaining fruits.

### Part B — Shopping List Manager

The program should allow users to add at least three items, remove an existing item, attempt to remove an item that is not on the list, display the remaining items, and quit with a goodbye message.

When a missing item is entered, the program should display:

`That item is not on your list.`

The program should continue running without crashing.

### Part C — List Report

The program should display the numbered shopping list, count the item names with more than four characters, and identify `sweet potatoes` as the longest item name.

Expected count:

`Items with more than 4 letters: 3`

Expected longest item:

`Longest item name: sweet potatoes`

## How to Run the Programs

Open the VS Code terminal in the assignment folder and run each program separately.

Run Part A:

```bash
py list_warmup.py
```

Run Part B:

```bash
py shopping_list.py
```

Run Part C:

```bash
py list_report.py
```

## Screenshots

The following screenshots should be included with the assignment:

- `list_warmup_output.png` — shows the output of Part A.
- `shopping_list_output.png` — shows the test session for Part B, including adding items, removing an existing item, attempting to remove a missing item, displaying the list, and quitting.
- `list_report_output.png` — shows the numbered list, item count, and longest item from Part C.

## Conclusion

This assignment improved my understanding of Python lists and how to manipulate and process list data. I learned how to use indexes, built-in list methods, loops, conditional statements, and membership checks. I also learned how checking whether an item exists before removing it helps prevent a `ValueError` and makes an interactive program more reliable.