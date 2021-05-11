
# Поиск в ширину
from collections import deque


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # array is used for identifying already checked persons
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:  # person is verifying in case when it is not exists in searched array
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)  # identify it as checked
    return False


def person_is_seller(name):
    return name[-1] == 'm'  # true if name ends on 'm'


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search("you")
