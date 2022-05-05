import json
import re


def main():
    print("Welcome to the main menu!")
    print("1. Create a new file")
    print("2. Sort a file")
    print("3. Exit")
    input_option = input("Please enter your option: ")
    if input_option == "1":
        create_file()
    elif input_option == "2":
        sort()
    elif input_option == "3":
        exit()

def create_file():
    words = []
    amount = int(input("Enter the amount of words you need to filter by: "))
    file = input("Enter the name of the file you want to filter: ")
    with open(f'{file}', "r") as f:
        for line in f:
            if has_number(line) == False:
                word = remove_special_characters(line)
                if amount == 0:
                    words.append(word)
                elif len(word) == amount:
                    words.append(word)
            else:
                print("Skipping line: " + line.strip())
                
    output = file.replace(".txt", ".json")
    out_file = open(f'{amount} - {output}', "w", encoding='utf8')
    json.dump(words, out_file, indent=4, sort_keys=False, ensure_ascii=False)
    out_file.close()
    process_completed()

def sort():
    words = []
    file = input("Enter the name of the file you want to sort: ")
    amount = int(input("Enter the amount of words you need to filter by: "))
    with open(f'{file}', "r") as f:
        for line in f:
            word = re.sub(r'^\d+[. ]+|;.*', '', line)
            word = remove_char(word)
            if "'" in word or " " in word or '.' in word:
                print("Skipping line: " + line.strip())
            elif amount == 0:
                words.append(word)
            elif len(word) == amount:
                words.append(word)
    output = file.replace(f".{file.split('.')[-1]}", ".json")
    out_file = open(f'{amount} - {output}', "w")
    json.dump(words, out_file, indent=4, sort_keys=False, ensure_ascii=False)
    out_file.close()
    process_completed()
    
def remove_char(word):
    if '\n' in word:
        return word.replace('\n', '')


def remove_special_characters(line):
    if '/' in line:
        return line.split('/')[0]
    elif '\\' in line:
        return line.split('\\')[0]
    else:
        return line.strip()


def has_number(string):
    return any(char.isdigit() for char in string)

def process_completed():
    print("Process completed!")
    input("Press enter to go back to the main menu.")
    main()


main()
