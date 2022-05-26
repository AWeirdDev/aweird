# AWeirdKit
A weird, but useful python routine, text-detecting kit, all-in-one.


## Installation
```sh
pip install -U git+https://github.com/AWeirdScratcher/aweird
```
or
```sh
python -m pip install git+https://github.com/AWeirdScratcher/aweird
```

## Basic Usage
> *Hey, are you looking for `Routine`?* Click here: [Jump!](#Routine)

Terminal (Console) colors:
```py
from aweird.kit import bcolors
print(bcolors.fail + "Red colors usually mean something is wrong" + bcolors.end) # end the color
```
> And you should see the text becomes `red`

Markdown Link Detector:
> *BETA*: We're planning to release `custom detectors`
```py
from aweird.kit import detect_format
result = detect_format("[markdown links like this](https://discord.com/jobs)")
print(result)
```
> And the result will be: `True`

Add Something in the text:
```py
from aweird.kit import add_at
result = add_at("I'm a bad person", "not ", 6)
print(result)
```
> And the result will be: `I'm not a bad person`

## Routine
Routine (object) - Tasks & Routines function

## Basic
```py
from aweird.kit import Routine

routine = Routine()

@routine.routine
def yay():
  print("A: I like chocolate")
  
@routine.routine
def wow():
  print("B: I like chocolate, too!")

routine.start(seconds=1) # run a task every 1 second
```
And the console will be like this in 1 second:
```
A: I like chocolate
B: I like chocolate, too!
```
If you want to run this routine forever, just simply add `forever=True` in `routine.start()` function:
```py
routine.start(seconds=1, forever=True)
```
For discord bot hosting:
> Note: this will run with `routine.start()`, but it's executed in a `Thread`.
```py
@routine.get("https://discord.com/jobs")
def hosted(response) -> None:
  print("I just hosted discord.com/jobs!")
```
To receive hosting errors:
```py
from .aweirdkit import Routine, HostError
routine = Routine()

@routine.get("???.com")
def __RandomWebsite():
  print("Will you print this?")

@routine.error(HostError)
def _hostError():
  print("Something went wrong!")
```
> Info: If the `@routine.error` was not set, by default it just prints a failing message.

## Events
If you want to trigger events, try this out:
```py
from aweird.kit import Routine

routine = Routine()

@routine.event
def on_ready(something: str) -> None: # on_[EVENT NAME]
  print("Wow, this is cool! And I received: " + something)

routine.emit("ready", something="I like chocolate")
```
To make it run `async` functions, just add `async_mode=True` in `routine.emit()` function.

Example usage for `async` functions:
```py
from aweird.kit import Routine

routine = Routine()

@routine.event
async def on_ready(something: str) -> None: # on_[EVENT NAME]
  print("Wow, this is cool! And I received: " + something)

routine.emit("ready",  async_mode=True, something="I like chocolate")
```


