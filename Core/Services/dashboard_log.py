import json
import random
from time import sleep

import requests
from sympy import Q
import threading


def get_planta():
    output = (json.loads((requests.get("http://localhost:8002/biodiesel_planta")).content))
    print (json.dumps(output, sort_keys=True, indent=4))

def get_valores():
    threading.Timer(0.1, get_valores).start()
    get_planta()

get_valores()


