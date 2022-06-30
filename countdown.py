import time

def countdown(t):
  '''
  input: time in seconds
  return: a countdown timer
  '''
  while t:
    min, sec = divmod(t, 60)
    timer = f'{min:02d}:{sec:02d}'
    print(timer, end='\r')
    time.sleep(1)
    t -= 1

  print('Time\'s up!')

t = int(input('Enter time in seconds: '))


