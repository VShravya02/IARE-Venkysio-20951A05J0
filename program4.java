import threading
def revstring(input_str):
    revstring = input_str[::-1]
    print("Reversed string:", revstring)
input_str = input("Enter a string: ")
thread = threading.Thread(target=revstring, args=(input_str,))
thread.start()
# Wait for the thread to complete before exiting the program
thread.join()
