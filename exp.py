import pandas as pd
from psychopy import core, sound, visual, event
import numpy as np
from random import shuffle
from exp_classes import Experiment

subject_id = input('Enter participant id: ')

experiment = Experiment((800, 600), (1, 1, 1), (-1, -1, -1))
experiment.show_fixation(1)
experiment.show_instructions()

stimuli = pd.read_csv("picture_verification_stimuli.csv")

images = []
texts= []

for item_path in stimuli['image_file']:
    image_stim = visual.ImageStim(experiment.window, image = item_path)
    images.append(image_stim)

for name_path in stimuli['item']:
    text_stim = visual.TextStim(experiment.window, text = name_path)
    texts.append(text_stim)

results = []

matches = list(zip(texts, images))
matches = np.random.permutation(matches)
texts_random = np.concatenate((texts[1:],texts[:1]))
non_matches = list(zip(texts_random, images))
non_matches = np.random.permutation(non_matches)

joined_stimuli = [*matches, *non_matches]
joined_stimuli = np.random.permutation(joined_stimuli)

for name, image in joined_stimuli:
    name.draw()
    experiment.window.flip()
    core.wait(0.5)
    experiment.show_fixation(0.5)
    image.draw()
    experiment.window.flip()

    start_time = experiment.clock.getTime()
    keys = event.waitKeys(maxWait=5, keyList=['y','n'], timeStamped=experiment.clock, clearEvents =True)

    if keys is not None:
        key, end_time = keys[0]
    else:
        key = None
        end_time = experiment.clock.getTime()
    
    results.append({
            'id': subject_id,
            'name': name.text,
            'image': image.image,
            'start_time': start_time,
            'end_time': end_time,
            'key': key
        })
        
results = pd.DataFrame(results)
results['reaction_time'] = results['end_time'] - results['start_time']
results.to_csv(f'output_{subject_id}.csv')