import sys, os

N = '\x1b[0m'    # WARNA MATI
B = '\x1b[1;94m' # BIRU
M = '\x1b[1;91m' # MERAH

if __name__ == '__main__':
    os.system("git pull")
    os.system("pip install rich")
    os.system("clear")
    os.system("python eliteprib.cython-38.so")

