from stats import count_words
from stats import count_letters
from stats import ordered_list

def get_text_from_file(file_path):
  file_content = ""
  with open(file_path) as file:
    file_content = file.read()
  return file_content

def main():
  text = get_text_from_file("books/frankenstein.txt")
  num_words = count_words(text)
  letters = count_letters(text)
  ordered_letters = ordered_list(letters)
  print("============ BOOKBOT =============")
  print(f"Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("----------- Character Count ----------")
  for letter in ordered_letters:
    if letter["char"].isalpha():
      print(f"{letter['char']}: {letter['num']}")
  print("============ END =============")

main()