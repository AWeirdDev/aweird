from .colors import bcolors
import requests # pip install requests
import asyncio # pip install asyncio
import time
from threading import Thread
from .errors import HostError


def detect_format(content):
  """
  *Still in BETA*
  Detects [markdown](link) format
  Returns `True` if detected
  """
  #print("ALL: " + str(len(content)))
  _list = [""]
  main = ["[", "](", ")"]
  now = 1
  
  reach = len(content)
  for word in content:
    now += 1
    if word in main:
      _list.append(word)
    
    elif now != reach:
        # is dubble sussy baka

      try:
        content[now-1]
      except:
        break
      if word + content[now-1] in main:
        _list.append("](")

  return "".join(_list) == "[]()"

def add_at(content: str, new: str, at: int):
  """Add a word at somewhere
  Example:
  add_at("I'm a bad person", "not ", 5) # 6th => 5, 1st => 0
  """
  main = []
  now = 0
  for w in content:
    if now == at:
      main.append(new)
    main.append(content[now])
    now += 1
  return "".join(main)


class Routine(object):
  def __init__(self):
    """AWeirdKit Routine Manager
    aweird.kit.Routine
    Usage:
    ```py
    from aweird.kit import Routine
    r = Routine()
    ...
    ```
    """
    self.routes = []
    self.events = {}
    self.urls = []
    self.URLfunc = []
    self.errors = {}

  def emit(self, event: str, async_mode: bool=False,*args, **send: any):
    """Trigger an event
    =======================
    Emit an event
    `event`:str
    *args **send:any Send something
    =======================
    Example: routine.emit("chocolate", uwu=True)
    To receive the event and do something, use:
    @routine.event
    def on_EVENT():
      ...
    """
    if not event in self.events:
      return None
    
    func = self.events[event]
    
    if send:
      if async_mode:
        asyncio.run(func(**send))
      else:
        func(**send)
    else:
      if async_mode:
        asyncio.run(func())
      else:
        func()
  
  def event(self, func):
    """
    Routine events.
    Usage:
    routine = Routine()
    @routine.event
    def on_EVENT(parameters):
    ...
    """
    name = func.__name__.replace("on_", "")
    #print(name)
    self.events[name] = func
    return func
  
  def error(self, error_type) -> callable:
    def decorator(func) -> callbale:
      self.errors[error_type] = func
      return func
  

  def routine(self, func) -> callable:
    """
    Routine registering.
    Usage:
    routine = Routine()
    @routine.routine
    ...
    """
    self.routes.append(func)
    return func
  
  def _hosterror(self, url: str):
    if HostError in self.errors:
      self.errors[HostError]()
    else:
      print(bcolors.fail + f"Cannot [GET] URL: {url}" + bcolors.end)

  def start(self, seconds: float=0, forever: bool=False) -> None:
    """Start the routine."""
    done = False
    if forever:
      if not self.routes and not self.URLfunc:
        print(bcolors.warning + f"WARNING: You are now starting an infinite loop with NO TASKS. You will not be able to use the console unless you thread this program." + bcolors.end)
    def runner():
      while not done:
        now = 0
        for func in self.URLfunc:
          try:
            r = requests.get(self.urls[now])
            r.raise_for_status()
          except:
            return self._hosterror(self.urls[now])
          func(r)
          now += 1
          time.sleep(seconds)
    Thread(target=runner).start()
          
    while not done:
      for func in self.routes:
        func()
        time.sleep(seconds)
      if not forever:
        done = True

  def get(self, url: str):
      """GET URL
      For discord bots hosting.
      """
      def decorator(func):
          self.urls.append(url)
          self.URLfunc.append(func)
          return func
      return decorator
    
# undefined
