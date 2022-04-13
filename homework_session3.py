# These are some homework exercises to practice working 
#  with pandas and psychopy.

## Exercise A
# 1. Load pandas and psychopy

import pandas as pd
from psychopy import visual, sound, core  # We import 3 components from the psychopy package

# 2. Load the picture verification simuli file
#    (look up the .read_csv method of pandas)

pic_stimuli = pd.read_csv('picture_verification_stimuli.csv')
print(pic_stimuli)

# 3. Loop over the item names, and print them on the screen
#    (you can loop over a single column just like a list!)


for column in pic_stimuli:
    if column == 'item':
        print(pic_stimuli[column])

# 4. Now, change your code to show a text stimulus with each item name,
#     with a 1 second pause in between, instead of using print().

window = visual.Window(size=(400, 400))
message = visual.TextStim(window)

for item in pic_stimuli['item']:
    message.text = item
    message.draw()
    window.flip()
    core.wait(1.0)
    window.flip()
    core.wait(1.0)
    


# 5. Loop over the item paths, and use them to create image stimuli;
#     display each image for 1 second.

for column in pic_stimuli:
    if column == 'image_file':
        print(pic_stimuli[column])

for pic in pic_stimuli['image_file']:
    image = visual.ImageStim(window, image= pic) 
    image.draw()
    window.flip()
    core.wait(1.0)


## Exercise B
# 1. Load the lexical decision stimuli file
lex_stimuli = pd.read_csv('lexical_decision_stimuli.csv')
print(lex_stimuli)


# 2. Select all the high frequency words (HF)
#    (you can do this using masks, just like how we selected a single row)

mask = lex_stimuli['freq_category'] == "HF"
#print(lex_stimuli.loc[mask, 'word'])

words = lex_stimuli.loc[mask, 'word']
#print(words)

# 3. Loop over the words, and create a sound stimulus for each
#    (you can specify the relative path as f'sounds/HF/{sound_name}.wav')

for audio in words:
    f'sounds/HF/{audio}.wav'
    #print(f'sounds/HF/{sound}.wav')

# 4. Play the sounds one-by-one, making sure there is some time between them

audio = sound.Sound('sounds/HF/baby.wav')

for audio in words:
    audio_path = f'sounds/HF/{audio}.wav'
    message.text = audio                    #I added text to the audio files, it was nice for me to see something on the screen while listening
    message.draw()
    mutli_sound = sound.Sound(audio_path)
    window.flip()
    mutli_sound.play()
    core.wait(2.0)


## Bonus exercise
# 1. Try to load in the image and/or sound stimuli first, 
#     before showing/playing them. You can use a list, and the .append()
#     method, to build a list of stimuli, and then use another for loop
#     to show/play them one by one.

#make a list with stimuli
#and then use this list to show/play them





# 2. Before showing/playing, try to randomise the order of stimuli; 
#     Google how to randomise the order of a list!
