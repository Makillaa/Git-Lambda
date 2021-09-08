import json, requests

massif = []


class ListCircle:

    def __init__(self, items=[]):
        global massif
        massif = items
        self.cursor = 0
        self.run = self.cursor + 3

    def circle(self):
        a = massif.pop(self.cursor)
        massif.append(a)
        if self.cursor >= len(massif) - 1:
            self.cursor = 0
        return self

    def get_visible_items(self):
        display = massif[self.cursor:self.run]
        self.circle()
        return display


def lambda_handler(event=None, context=None):
    global massif, jsonik, temporary_list
    if not massif:
        response = requests.get("https://api.airtable.com/v0/appBULZ298jKOcjoN/MainTable?view=Grid%20view",
                                headers={"Authorization": "Bearer keyW5hCXiZZ7WEJmf"})
        jsonik = json.loads(response.content)
        temporary_list = [i['fields']['title'] for i in jsonik['records']]
        lc = ListCircle(temporary_list)
        return lc.get_visible_items()
    else:
        lc = ListCircle(massif)
        return lc.get_visible_items()
