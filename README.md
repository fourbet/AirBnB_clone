# AirBnb clone

## Description of the project
This is a project of Holberton School and we had 7 days to do it. 
<br /><br />This is the first step towards building our first full web application: an AirBnB clone. 

## Step 1: The Console

* Create your data model
* Manage (create, update, destroy, etc) objects via a console / command interpreter
* Store and persist objects to a file (JSON file)

The first step is to manipulate a powerful storage system. This storage engine will give an abstraction between objects and how they are stored and persisted.

![AirBnB_Clone](https://github.com/huy75/huy75.github.io/blob/main/img/airbnb-clone.png)

It consists of **writing a command interpreter to manage AirBnB objects**.
It specifies classes for **User, City, State, Amenity, Place** and **Review** that inherits from the **BaseModel** class.
<br /><br />
The **BaseModel** take care of the initialization of all the instances.
<br /><br />
Additionnaly, we have created the first abstracted storage engine of the project: the **FileStorage** class. Instances are **serialized** to a JSON file and are **deserialized** from a JSON file to instances.

## Description of the command interpreter
To manage the objects of our project we are using a command interpreter that can:
<br />
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Usage
Like the Unix shell, the console(the command interpreter) works in both interactive and non-interactive mode.
<br />
### Interactive mode:
To run the console in interactive mode type:
<br /><br />
```$ ./console.py ``` 
<br /><br />
Then it will prints a prompt and waits for input from the user:
<br /><br />
``` (hbnb) ```
<br />

### Supported Commands

|COMMAND | DESCRIPTION|
|----|--------
|```quit``` | Quits console|
|```EOF``` | Quits console via EOF|
|```help <command>``` | Display help for ```<command>```|
|```create <class>``` | Creates a new instance of ```<class>``` and prints the id|
|```show <class> <id>``` | Prints the string representation of an instance based on its ```<class>``` and ```<id>```|
|```destroy <class> <id>``` | Deletes an instance based on its ```<class>``` and ```<id>```|
|```all``` | Prints all string representation of all instances of all classes|
|```all <class>``` | Prints all string representation of all instances of the ```<class>```|
|```update <class> <id> <attribute name> <attribute value>``` | Creates or updates the attribute of an instance based on its ```<class>``` and ```<id>``` |```<class name>.all()``` | Retrieve all instances of a class|
|```<class name>.count()```| Retrieve the number of instances of a class |
|```<class name>.show(<id>)``` | Retrieve an instance based on its id|
|```<class name>.destroy(<id>)``` | Destroy an instance based on his id|
|```<class name>.update(<id>, <attribute name>, <attribute value>)```| Update an instance based on its id|
|```<class name>.update(<id>, <dictionary representation>)```| Update an instance based on its id with a dictionary|

### Non-interactive mode:
The same commands can be used to run the console in non-interactive mode.
<br />
From a bash-like command line type echo ``` <command> ``` and pipe to  ``` ./console.py ```
<br />

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```
## Examples
```bash
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) 
```

```bash
(hbnb) User.count()
2
(hbnb) 
```

```bash
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 23, 'first_name': 'Bob', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb) 
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
(hbnb) 
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 17, 10, 788143), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb) 
```

This project was done by [Huy](https://github.com/huy75) && [Ophelie](https://github.com/fourbet)



