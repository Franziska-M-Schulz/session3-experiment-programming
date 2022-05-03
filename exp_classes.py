from psychopy import core, sound, visual, event

class  Experiment:
    def __init__(self, window_size, text_color, background_color, keys=['c']):
        self.text_color = text_color
        self.window = visual.Window(window_size, color = background_color)
        self.fixation = visual.TextStim(self.window, '+', color = text_color)
        self.instructions = visual.TextStim(self.window, "You will first see a word and then a picture. \n \n Press 'y' if the word and the picture match. \n \n Press 'n' if the word and picture do not match. \n \n Start the experiment with 'c'. " )
        self.clock = core.Clock()
        self.keys = keys
    
    def show_fixation(self, time=0.5):
        self.fixation.draw()
        self.window.flip()
        core.wait(time)

    def show_instructions(self):
        self.instructions.draw()
        self.window.flip()
        self.keys = event.waitKeys(keyList=self.keys, clearEvents =True)