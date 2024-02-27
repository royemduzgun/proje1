todos = []

def add_todo(todo):
    todos.append(todo)

def remove_todo(todo_index):
    if 0 <= todo_index < len(todos):
        del todos[todo_index]
    else:
        print("Geçersiz indeks!")

def print_todos():
    for i, todo in enumerate(todos):
        print(f"{i+1}. {todo}")

while True:
    print("\nYapılacaklar listesi :")
    print_todos()
    print("\n1.Yeni görev ekle")
    print("2.görev sil")
    print("3.çıkış")

    choice = input("Seçiminizi yapın:")

    if choice == "1":
        todo = input("Yeni görev: ")
        add_todo(todo)
    elif choice == "2":
        index = int(input("Silinecek görevin indeksi:")) - 1
        remove-todo(index)
    elif choice == "3":
        break
    else:
        print("Geçersiz seçenek!")
