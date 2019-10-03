from dwm1001 import DWM1001

# Example: Read from ttyS5 and print positions to console.
if __name__ == "__main__":
    def printer(dwm, id, pos):
        print(id, pos)
    DWM1001("/dev/ttyS5").listen(printer)
