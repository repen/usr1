

try:
    with open("movies.text") as file:
        data = file.read()
    print( data )
except (FileNotFoundError, IOError):
    print("No such file")



# try:
#     with open("movies.txt", mode='r', encoding='UTF-8') as file:
#     print(file.read())
# except IOError:
#     print('Die Datei ist nicht vorhanden')