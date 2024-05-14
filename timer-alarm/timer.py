"""
      Timer with Alarm Sound
            User can set a timer via minutes and seconds and
            an alarm will sound when the timer reaches 00:00.
            Can start another timer afterwards or quit timer.

            Royalty-free sound effects for dl:
            https://pixabay.com/sound-effects/search/alarm%20clock/
  
            Utilize playsound methods for Python:
            pip install playsound or pip3 install playsound==1.2.2

"""
from playsound import playsound
import time

CLEAR = '\033[2J'
CLEAR_AND_RETURN = '\033[H' 

print('\nNeed a Timer? Set the Timer (minutes:seconds)! \n')
def set_timer() :
      mins_set = input('Set the minutes:  ')
      if mins_set.isdigit() :
            mins_set = int(mins_set)
      else :
            print('Your time must be numeric for seconds.  ')

      secs_set = input('Set the seconds:  ')
      if secs_set.isdigit() :
            secs_set = int(secs_set)
      else :
            print('Your time must be numeric for seconds.')

      total_seconds = (mins_set * 60) + secs_set
      alarm(total_seconds, mins_set, secs_set)

def alarm(seconds, mins, secs) :
      time_elapsed = 0
      print(CLEAR)
      print('Timer Started:')
      print(f'Timer set:y
       alarm sounds after {mins:02d}:{secs:02d} (minutes:seconds) equaling {seconds} total seconds --has passed.')
      while time_elapsed < seconds :
            time.sleep(1)
            time_elapsed += 1
            time_left = seconds - time_elapsed
            minutes_left = time_left // 60 
            seconds_left = time_left % 60 
            print(f'{CLEAR_AND_RETURN} {minutes_left:02d}:{seconds_left:02d}') 

      playsound('alarm-sound.mp3')
      repeat = input('Do you need another Timer? Press `y` ').lower()
      if repeat == 'y' :
            set_timer()
      else :
            print('Thank you for using the Timer')


start_timer = input('Press `y` to set and start timer: ').lower()
if start_timer == 'y' :
      set_timer()
else :
      print('Thank you for using the Timer')