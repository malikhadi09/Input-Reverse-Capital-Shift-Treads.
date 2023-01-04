#NAME:MALIK ABDUL HADI
#REG NO: 200901053
#COURSE : OPERATING SYSTEM
#SECTION: B
import threading

class InputingThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.string = ""
        self.event = threading.Event()

    def run(self):
        try:
            # Taking input from the user
            self.string = input("Please, enter any string : ")
        except:
            # Handling exceptions if error occurs while providing input
            print("An error occurred while taking input.")
        finally:
            # Set the event to indicate that the input has been taken
            self.event.set()

class CapitalizeThread(threading.Thread):
    def __init__(self, input_thread):
        super().__init__()
        self.input_thread = input_thread

    def run(self):
        # Wait for the input thread to finish
        self.input_thread.event.wait()

        # Capitalizing the string and printing.

        print("Capitalized string is:", self.input_thread.string.upper())

class ReverseThread(threading.Thread):
    def __init__(self, input_thread):
        super().__init__()
        self.input_thread = input_thread

    def run(self):
        # Wait for the input thread to finish
        self.input_thread.event.wait()

        # Reverse the string and print it

        print("The Reversed string is:", self.input_thread.string[::-1])





class ShiftThread(threading.Thread):
    def __init__(self, input_thread):
        super().__init__()
        self.input_thread = input_thread

    def run(self):
        # Wait for the input thread to finish
        self.input_thread.event.wait()

        # Shifting the characters in the string and printing it
        shifted_string = ""
        for c in self.input_thread.string:
            shifted_string += chr((ord(c) - 97 + 2) % 26 + 97)
        print("Shifted string is:", shifted_string)

# Create the input thread
input_thread = InputingThread()


print("\n")
print("INPUTING, SHIFTING , REVERSING AND CAPITALIZING STRINGS,")
print("\n")
# Create the other threads and pass the input thread as an argument
reverse_thread = ReverseThread(input_thread)
capitalize_thread = CapitalizeThread(input_thread)
shift_thread = ShiftThread(input_thread)

# Starting the threads
input_thread.start()
reverse_thread.start()
capitalize_thread.start()
shift_thread.start()

# Waiting for the threads to finish
input_thread.join()
reverse_thread.join()
capitalize_thread.join()
shift_thread.join()
