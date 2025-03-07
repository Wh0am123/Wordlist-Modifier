import argparse
import random
import string

def matches_filter(word, numbers, special, caps, min_length):
    num_count = sum(c.isdigit() for c in word)
    special_count = sum(c in string.punctuation for c in word)
    caps_count = sum(c.isupper() for c in word)
    
    return len(word) >= min_length and num_count >= numbers and special_count >= special and caps_count >= caps

def process_wordlist(file, output_file, numbers, special, caps, min_length):
    words = []
    try:
        try:
            with open(file, "r", encoding="utf-8") as f:
                words = [line.strip() for line in f.readlines()]
        except UnicodeDecodeError:
            # rockyou.txt wouldn't open in utf-8 format (thanks chatGPT:))
            with open(file, "r", encoding="ISO-8859-1") as f:
                words = [line.strip() for line in f.readlines()]
        
        filtered_words = [word for word in words if matches_filter(word, numbers, special, caps, min_length)]
        
        if output_file:
            with open(output_file, "w") as f:
                f.write("\n".join(filtered_words) + "\n")
        else:
            for word in filtered_words:
                print(word)
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def display_help():
    help_text = """
    Usage: python3 wordlist.py <wordlist_file> [options]
    
    Options:
      --numbers, -n <n>   Minimum number of digits required
      --special, -s <n>   Minimum number of special characters required
      --caps, -c <n>      Minimum number of capital letters required
      --min-length, -l <n> Minimum password length
      --output, -o <file> Output file to save filtered words
      --help          Show this help message
    """
    print(help_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter words in a wordlist based on criteria.", add_help=False)
    parser.add_argument("file", type=str, nargs='?', help="Path to the wordlist file")
    parser.add_argument("-n", "--numbers", type=int, default=0, help="Minimum number of digits required")
    parser.add_argument("-s", "--special", type=int, default=0, help="Minimum number of special characters required")
    parser.add_argument("-c", "--caps", type=int, default=0, help="Minimum number of capital letters required")
    parser.add_argument("-o", "--output", type=str, help="Output file to save filtered words")
    parser.add_argument("-l", "--min-length", type=int, default=0, help="Minimum length of words")
    parser.add_argument("--help", action="store_true", help="Display help page")

    args = parser.parse_args()
    
    if args.help or not args.file:
        display_help()
    else:
        process_wordlist(args.file, args.output, args.numbers, args.special, args.caps, args.min_length)
