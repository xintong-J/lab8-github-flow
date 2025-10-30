from adventure.utils import read_events_from_file
import random
from rich import print
from rich.console import Console
from rich.text import Text

console = Console()
default_message = "You stand still, unsure what to do. The forest swallows you."

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return default_message

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event

def sstyle(text, style):
    console.print(text, style=style)
def cstyle():
    otext = Text()
    otext.append("Which direction do you choose?", style="bold blue")
    otext.append("(left/right/exit)", style = "italic magenta")
    otext.append(": ", style="italic black")
    console.print(otext)

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    sstyle("You wake up in a dark forest. You can go left or right.", "italic red")
    while True:
        cstyle()
        choice = input().strip().lower()
        if choice == 'exit':
            sstyle("Exit!!!", "italic green")
            break
        result = step(choice, events)
        if "left" in result.lower():
            sstyle(result, "yellow")
        elif "right" in result.lower():
            sstyle(result, "purple4")
        else:
            sstyle(result,"cyan")
        print(step(choice, events))
