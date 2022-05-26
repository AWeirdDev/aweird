# Routine examples, free to use :)
from aweird.kit import Routine

routine = Routine()

@routine.get("https://discord.com/jobs")
def __jobs(response):
  print("I just hosted https://discord.com/jobs")
  
@routine.get("https://discord.com")
def __main(response):
  print("Discord.com is soo good!")
  
routine.start(seconds=5, forever=True) # in case we get rate limited
