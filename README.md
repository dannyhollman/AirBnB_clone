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
     * [README.md](AirBnB_clone/README.md)
     * [file.json](AirBnB_clone/file.json)
     * [console.py](AirBnB_clone/console.py)
     * [tests](AirBnB_clone/tests)
       * [test_models](AirBnB_clone/tests/test_models)
         * [test_review.py](AirBnB_clone/tests/test_models/test_review.py)
         * [test_city.py](AirBnB_clone/tests/test_models/test_city.py)
         * [test_amenity.py](AirBnB_clone/tests/test_models/test_amenity.py)
         * [test_place.py](AirBnB_clone/tests/test_models/test_place.py)
         * [__init__.py](AirBnB_clone/tests/test_models/__init__.py)
         * [test_base_model.py](AirBnB_clone/tests/test_models/test_base_model.py)
         * [test_state.py](AirBnB_clone/tests/test_models/test_state.py)
         * [test_user.py](AirBnB_clone/tests/test_models/test_user.py)
       * [test_console.py](AirBnB_clone/tests/test_console.py)
     * [models](AirBnB_clone/models)
         * [amenity.py](AirBnB_clone/models/amenity.py)
         * [base_model.py](AirBnB_clone/models/base_model.py)
         * [city.py](AirBnB_clone/models/city.py)
         * [engine](AirBnB_clone/models/engine)
           * [file_storage.py](AirBnB_clone/models/engine/file_storage.py)
           * [__init__.py](AirBnB_clone/models/engine/__init__.py)
         * [__init__.py](AirBnB_clone/models/__init__.py)
         * [place.py](AirBnB_clone/models/place.py)
         * [review.py](AirBnB_clone/models/review.py)
         * [state.py](AirBnB_clone/models/state.py)
         * [user.py](AirBnB_clone/models/user.py)

## Authors

* Danny Hollman
* Stephen Ranciato
