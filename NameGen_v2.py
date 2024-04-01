import random
import keyboard

# Define the arrays globally

a = ['macchiavellian', 'mad', 'magic', 'magical', 'magisterial', 'magnanimous', 'magnetic', 'magnificent', 'majestic', 'major', 'managed', 'managerial', 'manic', 'manifested', 'manoeuvrable', 'marvelous', 'marxist', 'masterful', 'masturbatory', 'maternal', 'matriarchal', 'maximalist', 'meandering', 'meaningful', 'meditative', 'melancholic', 'mellow', 'melodic', 'melodious', 'membranous', 'memorable', 'menacing', 'mental', 'mercurial', 'merry', 'merrymaking', 'mesmerizing', 'messianic', 'metalogical', 'metamodernist', 'metamorphic', 'methodic', 'methodological', 'meticulous', 'metropolitan', 'microcircuit for', 'microclimate of', 'microcosm of', 'microgenerative', 'micromanaged', 'mighty', 'militant', 'mirthful', 'mischievous', 'modern', 'modernist', 'modernizing', 'modest', 'molenbeek', 'monstrous', 'moody', 'motivated', 'multidimensional', 'multimedial', 'multimodal', 'multimorphic', 'mycelial', 'mysterious', 'mystic']
b = ['abstract', 'academic', 'accidental', 'activist', 'administrative', 'administrators of', 'aesthetic', 'agents of', 'aggregated', 'alliance of', 'amazing', 'ambient', 'analytic', 'architects of', 'architectural', 'art', 'artistic', 'awesome']
c = ['axes','examination', 'excellence', 'excess', 'exchange', 'exclusives', 'exclusivity', 'excursion', 'executive', 'executives', 'exercise', 'exhibition', 'existence', 'expansion', 'expectation', 'expedition', 'experience', 'experiment', 'explosion', 'exploration', 'expression', 'extacy', 'extatics', 'extraction', 'extravagance', 'extravaganza', 'extraverts', 'exuberance', 'xenophiles', 'xylophone music', 'X-ident']

def print_random_string():
    global a, b, c  # Access the global variables
    
    print("Press spacebar for a new random string:")  # Print initial prompt

    while True:
        keyboard.wait('space')  # Wait for spacebar press
        if keyboard.is_pressed('q'):  # Check if 'q' is pressed
            break  # Break out of the loop if 'q' is pressed
        
        print(f"{random.choice(a)} {random.choice(b)} {random.choice(c)}")
        print() #print an empty line
        print("Press spacebar for a new random string:")  # Print prompt after random text
        print() #print an empty line

print_random_string()
