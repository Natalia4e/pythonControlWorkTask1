
import uuid
import datetime
import json

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

def save_data_to_json():
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file, indent=4, default=str)

def add_new_note():
    title = input("Введите заголовок Вашей новой заметки \n")
    body = input(" Введите тело новой заметки \n")
    note = create_new_note(title,body)
    data.append(note)
    print(note)
    save_data_to_json()

def create_new_note(title,body):
    return {
        "id": str(uuid.uuid4()),
        "title": title,
        "body": body,
        "datetime": str(datetime.datetime.now())
    }
def change_note():
    id = input("Введите id заметки, которую хотите изменить \n")
    for i, item in enumerate(data):
        if item['id'] == id:
            title = input("Введите заголовок Вашей новой заметки \n")
            body = input(" Введите тело новой заметки \n")

            item['title'] = title
            item['body'] = body
            item['datetime'] = str(datetime.datetime.now())
            print(item)
            data[i] = item
            break

    print("Заметка изменена")
    save_data_to_json()

def delete_note():
    id = input("Введите id заметки, которую хотите удалить \n")
    for i, item in enumerate(data):
        if item['id'] == id:
            data.pop(i)
            print("Заметка удалена")
    save_data_to_json()

def search_note():
    id = input("Введите id заметки, которую хотите изменить \n")
    for i, item in enumerate(data):
        if item['id'] == id:
            print(data[i])

def show_all_notes():
    print(data)


