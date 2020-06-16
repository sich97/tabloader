import time
import keyboard

RUN_HOTKEY = "ctrl+e"


def main():
    """
    Pre-condition: Firefox web browser in foreground
    When the RUN_HOTKEY is pressed, the program will loop through tabs and reload each of them until
    the RUN_HOTKEY is pressed again.
    :return: None
    """
    # Initialization
    run_signal = initialize()

    # Program loop
    while True:
        # If the run signal is True
        if run_signal.get_state():
            # Go to first tab
            keyboard.press_and_release("alt+1")

            # While the run signal is still True
            while run_signal.get_state():
                # Reload current tab
                keyboard.press_and_release("ctrl+r")

                # Wait for 5 seconds to allow the tab to fully load
                time.sleep(5)

                # Go to next tab
                keyboard.press_and_release("ctrl+pagedown")
        else:
            # Wait for 0.1 seconds
            time.sleep(0.1)


def initialize():
    """
    Instantiates the run_signal and registers the RUN_HOTKEY to change the run_signal when pressed.
    :return: run_signal (Signal)
    """
    # Register key_combinations
    run_signal = Signal("run_signal", False)
    keyboard.add_hotkey(RUN_HOTKEY, run_signal.change_state)

    return run_signal


class Signal:
    """
    Mainly used to control and break loops
    """
    def __init__(self, name, initial_state):
        """
        Sets the signal to the desired initial state.
        Also stores the name of the object used to create the instance.
        :param name: The name of the object used when instantiating.
        :type name: string
        :param initial_state: The initial signal
        :type initial_state: bool
        """
        self.state = initial_state
        self.name = name

    def get_state(self):
        """
        Returns the current state of the signal
        :return: self.state (bool)
        """
        return self.state

    def set_state(self, new_state):
        """
        Sets the signal state to a desired truth value
        :param new_state: The new truth value
        :type new_state: bool
        :return: old_state (bool)
        """
        old_state = self.state
        self.state = new_state

        return old_state

    def change_state(self):
        """
        Changes the signal state to the opposite of what it currently is
        :return: self.state (bool)
        """
        if self.state:
            self.set_state(False)

        else:
            self.set_state(True)

        return self.state


if __name__ == '__main__':
    main()
