def count_words(text):
  return (len(text.split()))

def count_letters(text):
  text = text.lower()
  letters = {}
  for letter in text:
    if letter in letters:
      letters[letter] += 1
    else:
      letters[letter] = 1
  return letters

def ordered_list(dict):
  list = []
  for item in dict:
    list.append({"char": item, "num": dict[item]})
  list.sort(key=lambda x: x["num"], reverse=True)
  return list