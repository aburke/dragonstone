import signal
import time

halt = False


def exit_process(*args):
    global halt
    print("Exiting...")
    halt = True


def wait():
    while not halt:
        print("Waiting....")
        time.sleep(1)


signal.signal(signal.SIGINT, exit_process)


if __name__ == '__main__':
    wait()