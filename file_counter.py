import os
import sys

def count_files_folders():
    
    path = input("Введите путь к папке: ")
    
    
    if not os.path.exists(path):
        print("❌ Такой папки не существует!")
        return
    
    
    files = 0
    folders = 0
    
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            files += 1
        elif os.path.isdir(item_path):
            folders += 1
    
 
    print(f"\n📊 Результат для папки: {path}")
    print(f"📁 Папок: {folders}")
    print(f"📄 Файлов: {files}")
    print(f"✅ Всего: {files + folders}")


if __name__ == "__main__":
    count_files_folders()