#!/usr/bin/env python3

def frame(text, frame):
    line1 = frame * (len(text)+4)
    line2 = frame + ' ' + text + ' ' + frame
    return line1 + '\n' + line2 + '\n' + line1

    

print(frame('Szia, láttalak már valahol?', '*'))
print(frame('Heló', '+'))
print(frame('Hogy vagy?', '-'))
print(frame('Jól', '#'))
