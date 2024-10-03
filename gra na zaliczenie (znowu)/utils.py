import time

def slow_text(text, delay=0.1, end='\n', flush=True):
    for char in text:
        print(char, end='', flush=flush)
        time.sleep(delay)
    print(end, end='')
