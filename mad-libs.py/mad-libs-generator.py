"""     
    Mad Libs Generator 
        Utilize a base story.txt file and update the <words> to 
        the user input choices. 
        Create an updated file with the users version of the story.
        Save the file under a unique file name in same folder.
        Print the story for the user.
"""

print('Welcome to Story Time')
print('With a little help and a few questions, you will generate your own story and save it to a uniquely named file. \n')

def start_game() :
  print('Would you like to start the game? ')
  start = input('Press `y` ').lower()
  if start == 'y' :

      with open('story.txt', 'r') as f:
          story = f.read()

      words = set()
      start_of_word = -1
      target_start = '<'
      target_end = '>'
      story_name = None

      for i, char in enumerate(story):
          if char == target_start:
              start_of_word = i
          elif char == target_end and start_of_word != -1:
              word = story[start_of_word:i + 1]
              words.add(word)
              start_of_word = -1

      answers = dict()
      for word in words :
          answer = input('Type word for ' + word  + ':  ')
          answers[word] = answer
          story_name = answers[word] + '_updated_story.txt'
          
      print('Your story is saved as filename: ', story_name)
      print()

      for word in words :
          story = story.replace(word, answers[word])

      with open(story_name, 'a') as f :
          f.write(story)

      print(story)

  else :
      print()
      quit()  

start_game()
