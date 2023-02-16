import pygameGUI.pgmain as pgmain

from backend.backend import Backend


MODE = "pygame" # pygame / web




if __name__ == "__main__":
    backend = Backend()
    print("Selected mode: ", MODE)
    if MODE == "pygame":
        pgmain.main(backend)
    else:
        print("No valid MODE selected")