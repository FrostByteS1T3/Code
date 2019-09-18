from appjar import gui
from Hangman import play_hangman_gui
ascii_hangman_phase_1 = '''  
                               -------
                              |       |
                              |
                              |
                              |
                              |
                        ______|_______ '''
ascii_hangman_phase_2 = '''    
                               -------
                              |       |
                              |       O
                              |
                              |
                              |
                        ______|_______ '''
ascii_hangman_phase_3 = '''   
                               -------
                              |       |
                              |       O
                              |       |
                              |
                              |
                        ______|_______ '''
ascii_hangman_phase_4 = '''    
                               -------
                              |       |
                              |       O
                              |       |/
                              |
                              |
                        ______|_______ '''
ascii_hangman_phase_5 = '''    
                               -------
                              |       |
                              |       O
                              |      \|/
                              |
                              |
                        ______|_______ '''
ascii_hangman_phase_6 = '''   
                               -------
                              |       |
                              |       O
                              |      \|/
                              |      / 
                              |
                        ______|_______ '''
ascii_hangman_phase_7 = '''   
                               -------
                              |       |
                              |       O
                              |      \|/
                              |      / \
                              |
                        ______|_______ '''
print(ascii_hangman_phase_6)
app = gui()
play_hangman_gui(app)
