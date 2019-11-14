# AirBnB clone - The console

## Description

A command interpreter for initilization, serialization and deserialization of instances. <br />
Uses an abstracted storage engine.

## Requirements

Python3 <br />

## Installing

```bash
git clone https://github.com/dannyhollman/AirBnB_clone.git
```

## Usage

Interactive Mode
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) quit
$
```

Using commands
```bash
$ ./console.py
(hbnb) create User
eed21641-e8df-4fff-b98b-7798e5644a2b
(hbnb) show User eed21641-e8df-4fff-b98b-7798e5644a2b
[User] (eed21641-e8df-4fff-b98b-7798e5644a2b) {'updated_at': datetime.datetime(2019, 11, 12, 15, 24, 34, 299778), 'created_at': datetime.datetime(2019, 11, 12, 15, 24, 34, 299686), 'id': 'eed21641-e8df-4fff-b98b-7798e5644a2b'}
(hbnb) User.show(eed21641-e8df-4fff-b98b-7798e5644a2b)
[User] (eed21641-e8df-4fff-b98b-7798e5644a2b) {'updated_at': datetime.datetime(2019, 11, 12, 15, 24, 34, 299778), 'created_at': datetime.datetime(2019, 11, 12, 15, 24, 34, 299686), 'id': 'eed21641-e8df-4fff-b98b-7798e5644a2b'}
(hbnb) quit
$
```

Other Commands

create <class> - Creates a new instance of BaseModel and saves to json. <br />
<br />
show <class> <id> - Prints string representation of an instance. <br />
<br />
destroy <class> <id> - Deletes an instance. <br />
<br />
all <class/optional> - Prints all string representation of all instances. <br />
<br />
update <class> <id> <attribute> - Updates an instance based on class name.

Non-Interactive Mode
```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
$
```

## File Structure

 * [AirBnB_clone](AirBnB_clone)
     * [README.md](README.md)
     * [console.py](console.py)
     * [tests](/tests)
       * [test_models](/tests/test_models)
         * [test_review.py](/tests/test_models/test_review.py)
         * [test_city.py](/tests/test_models/test_city.py)
         * [test_amenity.py](/tests/test_models/test_amenity.py)
         * [test_place.py](/tests/test_models/test_place.py)
         * [__init__.py](/tests/test_models/__init__.py)
         * [test_base_model.py](/tests/test_models/test_base_model.py)
         * [test_state.py](/tests/test_models/test_state.py)
         * [test_user.py](/tests/test_models/test_user.py)
       * [test_console.py](/tests/test_console.py)
     * [models](/models)
         * [amenity.py](/models/amenity.py)
         * [base_model.py](/models/base_model.py)
         * [city.py](/models/city.py)
         * [engine](/models/engine)
           * [file_storage.py](/models/engine/file_storage.py)
           * [__init__.py](/models/engine/__init__.py)
         * [__init__.py](/models/__init__.py)
         * [place.py](/models/place.py)
         * [review.py](/models/review.py)
         * [state.py](/models/state.py)
         * [user.py](/models/user.py)

## Authors

* Danny Hollman
* Stephen Ranciato
