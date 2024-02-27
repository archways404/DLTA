# DLTA

DLTA is a language designed to be transpiled into various shell scripts such as Bash, PowerShell, etc. This document serves as a guide to the syntax of the custom scripting language.

# Scripting Language Syntax Guide

This document serves as a guide to the syntax of the custom scripting language designed to be transpiled into various shell scripts such as Bash, PowerShell, etc.

## Comments

Comments are non-executable parts of the code meant for documentation and explanation.

### Single Line Comment
- Syntax: `COMMENT: This is a single-line comment`
- Example:
  ```plaintext
  COMMENT: This is a single-line comment
  ```

### Multi-Line Comment
- Syntax:
  ```plaintext
  COMMENT: {
    This is a multi-line comment
  }
  ```
- Example:
  ```plaintext
  COMMENT: {
    This is a multi-line comment
    that spans multiple lines.
  }
  ```

## Commands

Commands are executable instructions that will be translated into the appropriate syntax for the target shell.

- Syntax:
  ```plaintext
  COMMAND: {
    echo "HELLO WORLD"
  }
  ```
- Example:
  ```plaintext
  COMMAND: {
    echo "HELLO WORLD"
  }
  ```

## Variables

Variables store data that can be referenced and manipulated by the script.

### Constant Variable
- Syntax: `VARIABLE: VAR(C, TYPE) = VALUE`
- Example:
  ```plaintext
  VARIABLE: VAR(C, INT) = 10
  ```

### Modifiable Variable
- Syntax: `VARIABLE: VAR(M, TYPE) = 'VALUE'`
- Example:
  ```plaintext
  VARIABLE: VAR(M, STRING) = 'HELLO WORLD'
  ```

- Note: "VAR" is the name of the variable. The type can be INT for integers, STRING for string values, etc.

## Paths

Paths define the navigation through directories and files in the filesystem.

- Syntax: `PATH: ROOT -> FOLDER -> FILE.EXE`
- Example:
  ```plaintext
  PATH: C: -> Users -> Documents -> report.docx
  ```

## Functions

Functions are reusable blocks of code that take input, process it, and return an output.

- Syntax:
  ```plaintext
  FUNCTION: FUNCTION_NAME(ARG1, ARG2, ARG3) {
    VARIABLE: FUNCTION_VARIABLE(M, INT) = ARG1 + ARG2 + ARG3
    RETURN => FUNCTION_VARIABLE
  }
  ```
- Example:
  ```plaintext
  FUNCTION: ADD_THREE_NUMBERS(NUM1, NUM2, NUM3) {
    VARIABLE: SUM(M, INT) = NUM1 + NUM2 + NUM3
    RETURN => SUM
  }
  ```

## Folders & Files

Scripts can create or modify files and directories.

### Create File
- Syntax: `CREATE: FILE <FILENAME>`
- Example:
  ```plaintext
  CREATE: FILE <report.txt>
  ```

### Create Folder
- Syntax: `CREATE: FOLDER <FOLDER_NAME>`
- Example:
  ```plaintext
  CREATE: FOLDER <Reports>
  ```

### Modify File
- Syntax: `MODIFY: FILENAME <ACTION> "CONTENT"`
- Actions: `<WRITE>` to add content, `<REMOVE>` to delete content.
- Example:
  ```plaintext
  MODIFY: report.txt <WRITE> "HELLO WORLD"
  MODIFY: report.txt <REMOVE> "HELLO WORLD"
  ```

This syntax guide provides a foundational understanding of the custom scripting language. The language is designed to be compiled into native shell scripts, making it versatile and adaptable to various operating systems and environments.

