from stats import count_words
from stats import count_letters

def get_text_from_file(file_path):
  file_content = ""
  with open(file_path) as file:
    file_content = file.read()
  return file_content

def main():
  text = get_text_from_file("books/frankenstein.txt")
  num_words = count_words(text)
  letters = count_letters(text)

  print(f"{num_words} words found in the document")
  print(letters)
main()