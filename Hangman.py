import random
listOfWords = ["doubt", "Pointless", "meetinG", "Robin", "makeshift", "Abundant", "squeak"]
PreviousLetters = []
wordChosen = random.choice(listOfWords)
wrong = 0
def RemakeWord():
  Word = ""
  for looper in range(0,len(wordChosen)):
    if wordChosen[looper] in map(str.lower,PreviousLetters):
      Word = Word + wordChosen[looper]
    elif wordChosen[looper] in map(str.upper,PreviousLetters):
       Word = Word + wordChosen[looper]
    else:
      Word = Word + "_"
  return Word
while True:
  valid = False
  while valid == False:
    letter = input("Choose a letter: ")
    if letter.lower() not in PreviousLetters:
      PreviousLetters.append(letter.lower())
      valid = True
    else:
      print("Already used letter")
  outputWord = RemakeWord()
  print(outputWord)
  counter = 0
  for loop in range(0,len(wordChosen)):
    if letter != wordChosen[loop].upper() and letter != wordChosen[loop].lower():
      counter = counter + 1
  if counter == len(wordChosen):
    wrong = wrong + 1
    print(f"{5-wrong} attempts left")
  print(f"Used Letters: {PreviousLetters}")
  if wrong == 5:
    print("GAME OVER")
    break
  if "_" not in outputWord:
    print("GAME WON!")
    break