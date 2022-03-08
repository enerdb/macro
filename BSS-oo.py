
#####################################
# Imports
#####################################

from pynput import mouse
from pynput import keyboard
import threading

#####################################
# Helper functions
#####################################

def single_click():
    my_mouse.click(mouse.Button.left)

#####################################
# Routine Classes
#####################################

class Routine(threading.Thread):

#""" The Thread class represents an activity that is run in a separate thread of control.
#There are two ways to specify the activity: by passing a callable object to the constructor,
#or by overriding the run() method in a subclass.
#No other methods (except for the constructor) should be overridden in a subclass.
#In other words, only override the __init__() and run() methods of this class.
#Parece que estou fazendo override no start()
#"""

    def __init__(self):
        super(Routine, self).__init__()  # Chama o construtor de threading.Thread
        self.running = False
        self.program_running = True # maybe should be a class attribute, not a object attribute
        
    def turn_on(self):
        self.running = True
        
    def turn_off(self):
        self.running = False
         

#### ClickMouse - AutoClick ####
         
class ClickMouse(Routine):
    def __init__(self, delay = 1, button = mouse.Button.left):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
 
    def run(self):
        while self.program_running:
            while self.running:
                my_mouse.click(self.button)
                event.wait(self.delay)
            event.wait(0.1)

#### Farm ####

class Farm(Routine):
    def __init__(self):
        super(Farm, self).__init__()
        
    def run(self):
        orientation = ['w', 'a', 's', 'd']
        while self.program_running:
            while self.running:
                ncircles = 3
                while(ncircles > 0):
                    sleep_time = 0.1 + ncircles*0.3
                    for side in orientation:
                        if not self.running:
                            return
                        my_mouse.click(mouse.Button.left)
                        my_keyboard.press(side)
                        event.wait(sleep_time)
                        my_keyboard.release(side)
                    ncircles -= 1
                event.wait(0.1)
 
    
#####################################
# On press functions
#####################################    

def stop_all():
    ac_thread.turn_off()
    farmer.turn_off()


def program_quit():
    stop_all()
    ac_thread.program_running = False # maybe should be a class attribute, not a object attribute
    farmer.program_running = False # maybe should be a class attribute, not a object attribute
    listener.stop()
    return False



#####################################
# Test Functions
#####################################    

def print_test():
    print('Entrada de teclado funcionando')

def quit_test():
    print('Saindo')
    listener.stop()


#####################################
# Main 
#####################################

if __name__ == "__main__":

    event = threading.Event()

    my_mouse = mouse.Controller()
    my_keyboard = keyboard.Controller()
    ac_thread = ClickMouse(1, mouse.Button.left)
    ac_thread.start()
    farmer = Farm()
    farmer.start()



    with keyboard.GlobalHotKeys({
            '<ctrl>+h': print_test,
            '<ctrl>+q': quit_test,
            '<ctrl>+f': farmer.turn_on,
            '<ctrl>+t': ac_thread.turn_on,
            '<ctrl>+g': stop_all,
            '<ctrl>+x': program_quit
            }) as listener:
        listener.join()

#######################################################
# Problemas encontrados:
# (Resolvido) - Não estou conseguindo fazer multithreading e o programa só libera o main quando a função intermediária termina
# (Resolvido) - return False não está funcionando para sair do programa com GlobalHotKeys. Funcionava com Listener 






########################################################

# from pynput import keyboard

# def on_activate():
    # print('Global hotkey activated!')

# def for_canonical(f):
    # return lambda k: f(l.canonical(k))

# hotkey = keyboard.HotKey(
    # keyboard.HotKey.parse('<ctrl>+<alt>+h'),
    # on_activate)
# with keyboard.Listener(
        # on_press=for_canonical(hotkey.press),
        # on_release=for_canonical(hotkey.release)) as l:
    # l.join()