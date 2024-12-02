from json_db_class import JSONTool
JSONTool = JSONTool() # Импортируем и инициализируем json_tool

db = JSONTool.load_db('db.json') # Загружаем бд по названию

print(db["Users"]["0"]["name"]) # str
print(db["Users"]["0"]["channels_amount"]) #int
print(db["Users"]["1"]["nickname"]) 
print(db["Users"]["1"]["telegram_channel"])
print(db["Users"]["1"]["habr"])

# Ниже прописаны методы

# db["Users"]["pi"] = 3.141592
# db["Users"]["1"]["nickname"] = "nothing" # Задаем новое значение существующей переменной
# db["Users"]["1"]["second_name"] = None # Задаем новую переменную с новым значением. True/False/None конвертируется в формат JSON

# db["Users"]["2"] = {} # Открываем новую ветвь
# db["Users"]["2"]["name"] = "Jobs" # Создаем переменную в новой ветви

JSONTool.save_db('db.json', db) # Сохраняем файл указывая название и передавая внутрь измененную переменную db