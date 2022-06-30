import time

def countdown():
  '''
  input: time in seconds
  return: a countdown timer
  '''
  t = int(input('Enter time in seconds: '))
  while t:
    min, sec = divmod(t, 60)
    timer = f'{min:02d}:{sec:02d}'
    print(timer, end='\r')
    time.sleep(1)
    t -= 1

  print('Time\'s up!')




