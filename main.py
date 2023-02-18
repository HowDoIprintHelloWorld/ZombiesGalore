import pygameGUI.pgmain as pgmain
import webGUI.webmain as webmain

from backend.backend import Backend


MODE = "web" # pygame / web




if __name__ == "__main__":
    backend = Backend()
    print("Selected mode: ", MODE)
    if MODE == "pygame":
        pgmain.main(backend)
    elif MODE == "web":
        webmain.main()
    else:
        print("No valid MODE selected")
