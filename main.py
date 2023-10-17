import json
import os

datapools = {}
command = []

def JSONThings():
  if command[1] == 'makefile':
    try:
      with open(f'{command[2]}.json', "w") as f:
        f.close()
    except IndexError:
      print('The operation could not be completed due to lack of arguments')
      print('Command should look like: json makefile <filename>')
    else:
      print('Done')
  
  if command[1] == 'remfile':
    try:
      os.remove(f'{command[2]}.json')
    except FileNotFoundError:
      print('The operation could not be completed due to lack of arguments')
      print('Command should look like: json remfile <filename>')
    else:
      print("Done")

  if command[1] == 'writefile':
    try:
      with open(f'{command[2]}.json', 'w') as jsonfile:
        try:
          json_object = json.loads(command[3])
          json.dump(json_object, jsonfile, indent=4, separators=(',',': '))
        except:
          print("The operation could not be completed due to lack of arguments: jsonformattedcontent")
          print("Command should look like: json writefile <filename> <jsonformattedcontent>")
        else:
          print("Done")
    except IndexError:
      print("The operation could not be completed due to lack of arguments: filename, jsonformattedcontent")
      print("Command should look like: json writefile <filename> <jsonformattedcontent>")
    else:
      print("Done")

def AddData():
  try:
    json_object = json.loads(command[2])
    datapools.update(json_object)
  except IndexError:
    print("The operation could not be completed due to lack of arguments: jsonformattedcontent")
    print("Command should look like: add data <jsonformattedcontent>")
  except json.decoder.JSONDecodeError:
    print("The operation could not be completed due to lack of arguments: jsonformattedcontent")
    print("Command should look like: add data <jsonformattedcontent>")

def RemoveData():
  try:
    datapools.pop(command[2])
  except IndexError:
    print("The operation could not be completed due to lack of arguments: tag")
    print("Command should look like: rem data <tag>")

def SaveData():
  with open("data.json", "w") as datafile:
    json.dump(datapools, datafile, indent=4, separators=(',',': '))
  print("Done")

def TakeInput():
    input_user = input()
    input_temp = ""

    str_index = 0
    inside_quotes = False
    inside_curly_brackets = False

    for i in input_user:
        str_index += 1

        if i == '"':
            inside_quotes = not inside_quotes
        
        if i == "{":
            inside_curly_brackets = True

        if not inside_curly_brackets:
            if not inside_quotes:
                if i != " " and i != '"':
                    input_temp += i
                elif i == " " and input_temp != "":
                    command.append(input_temp)
                    input_temp = ""
                
                if str_index == len(input_user) and input_temp != "":
                    command.append(input_temp)
                    input_temp = ""
            else:
                if i != '"':
                    input_temp += i
                if str_index == len(input_user):
                    command.append(input_temp)
                    input_temp = ""
        else:
            input_temp += i
            if str_index == len(input_user):
                command.append(input_temp)
                input_temp = ""

def CommandAct():
  if command[0] == 'rem' and command[1] == 'data':
    print("Command recognized")
    RemoveData()
  if command[0] == 'add' and command[1] == 'data':
    print("Command recognized")
    AddData()
  if command[0] == 'save' and command[1] == 'data':
    print("Command recognized")
    SaveData()
  if command[0] == 'print' and command[1] == 'data':
    print("Command recognized")
    print(datapools)
    print("Done")
  if command[0] == 'json':
    JSONThings()
  if command[0] == 'help':
     print("List of commands:")
     print("add data <jsonformattedtext> | Replaces the datapools list with a json formatted text")
     print("rem data <tag> | Removes the specified tag from the datapools list (Only works with top tags)")
     print("save data | Saves the datapools list into a json formatted file called 'data.json'")
     print("print data | Prints the current state of datapools list in the terminal")
     print("json makefile <filename> | Creates a .json file of the specified filename")
     print("json remfile <filename> | Deletes the .json file specified")
     print("json writefile <filename> <jsonformattedtext> | Creates a .json file of the specified name and writes the specified json formatted text")
     print("exit | Closes the program")
     print("help | Shows this list\n")
  if command[0] == 'exit':
    exit()

print("Type 'help' to see a list of commands")
while(True):
  command = []
  TakeInput()
  CommandAct()