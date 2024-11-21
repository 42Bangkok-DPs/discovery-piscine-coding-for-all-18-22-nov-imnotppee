def swap_case(text):

  new_text = ""
  for char in text:
    if char.isupper():
      new_text += char.lower()
    else:
      new_text += char.upper()
  return new_text

text = input("Enter a text: ")
result = swap_case(text)
print(result)