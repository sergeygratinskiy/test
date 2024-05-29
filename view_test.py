import sys
import time

def wave_hand():
    for _ in range(99):
        sys.stdout.write("\r(• )=(• )")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\r(• )=( •)")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\r( •)=( •)")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\r(• )=( •)")
        sys.stdout.flush()
        time.sleep(0.5)

if __name__ == "__main__":
    while True:
        print("включён на просмотр")
        wave_hand()