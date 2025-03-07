# Wordlist-Modifier
A simple python script to filter your wordlist according to a certain password policy.

# Installation

Clone the repository and navigate to the script's directory:

```bash
git clone https://github.com/Wh0am123/Wordlist-Modifier.git
cd password-filter
```

Ensure you have Python 3 installed.

# Usage

Run the script with a wordlist and desired filtering options:

```
python3 wordlist.py <wordlist_file> [options]
```
Options that you can use are:
```
Options:

-n, --numbers <n> : Minimum number of digits required

-s, --special <n> : Minimum number of special characters required

-c, --caps <n> : Minimum number of capital letters required

-l, --min-length <n> : Minimum length of words

-o, --output <file> : Output file to save filtered words

--help : Show help message
```

# Example Commands:

## Filter words with at least 2 numbers and 1 special character:
```bash
python3 wordlist.py /usr/share/wordlists/rockyou.txt -n 2 -s 1
```
## Filter words with at least 1 uppercase letter and save to a file:
```bash
python3 wordlist.py password.txt --caps 1 --output new_passwords.txt
```

## Filter words with at least 1 number and 1 uppercase letter and 1 special charcater and min length of 9 and save to a file:
```bash
python3 wordlist.py pass.txt --numbers 1 --caps 1 --special 1 --min-length 9 --output new.txt
```

