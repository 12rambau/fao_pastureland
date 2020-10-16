import time
from IPython.display import clear_output

def update_progress(progress, msg='Progress'):
    bar_length = 20
    progress = float(progress)
    block = int(round(bar_length * progress))

    clear_output(wait = True)
    text = "{2}: [{0}] {1:.1f}%".format( "#" * block + "-" * (bar_length - block), progress * 100, msg)
    
    print(text)