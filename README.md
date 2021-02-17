# AirBnb clone

## Description of the project
This is a project of Holberton School and we had 7 days to do it. 
<br /><br />This is the first step towards building our first full web application: an AirBnB clone. It consists of **writing a command interpreter to manage AirBnB objects**.
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
|```update <class> <id> <attribute name> <attribute value>``` | Creates or updates the attribute of an instance based on its ```<class>``` and ```<id>``` |

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



This project was done by [Huy](https://github.com/huy75) && [Ophelie](https://github.com/fourbet)



