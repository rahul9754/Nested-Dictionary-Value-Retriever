# Nested Dictionary Value Retriever

## Overview

This repository contains a Python function `get_value` that allows you to retrieve values from nested dictionaries using a string path. This can be particularly useful for DevOps engineers who need to manage complex configurations, parse API responses, and automate infrastructure setups.

## Pre-requisites

1. **Python Installation**: Ensure Python is installed on your system. You can download Python from the [official website](https://www.python.org/downloads/). During installation, make sure to check the box that says "Add Python to PATH".

## Installation and Usage

### Step 1: Clone the Repository

```sh
git clone https://github.com/rahul9754/nested_value_retriever.git
cd nested_value_retriever
```

### Step 2: Run the script

```
python nested_value_retriever.python
```

## Expected Output

When you run the script, you should see the following output:

```
The value for key 'a/b/c' is: d
The value for key 'x/y/z' is: a
The value for key 'a' is: {'b': {'c': 'd'}}
The value for key 'x/y' is: {'z': 'a'}
```

