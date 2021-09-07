import json, requests


class Pagination:

    def __init__(self, items=[]):
        self.items = items
        self.cursor = 0

    def get_visible_items(self):
        run = self.cursor+3
        return self.items[self.cursor:run]
        a = self.items.pop(self.cursor)
        self.items.append(a)
        if self.cursor >= len(self.items)-1:
            self.cursor = 0


def lambda_handler(event, context):
    response = requests("GET", "https://api.airtable.com/v0/appBULZ298jKOcjoN/MainTable?view=Grid%20view",
                            headers={"Authorization": "Bearer keyW5hCXiZZ7WEJmf"})
    jsonik = json.loads(response.content)
    print(jsonik)
    zdarov = []
    for i in jsonik['records']:
        zdarov.append(i['fields']['title'])
    pig = Pagination(zdarov)
    aim = []
    for i in range(1):
        return pig.get_visible_items()
