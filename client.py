import requests


def name_request():
    r = requests.get("vcm-3583.vm.duke.edu:5000/name")
    print(r.json())


def hello_there_request():
    r = requests.get("vcm-3583.vm.duke.edu:5000/hello")
    print(r.json())


def find_distance_request():
    r = requests.get("vcm-3583.vm.duke.edu:5000/distance")
    print(r.json())
