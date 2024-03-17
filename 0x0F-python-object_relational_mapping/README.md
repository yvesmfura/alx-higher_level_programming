# ALX Higher Level Programming - Python Object Relational Mapping

This repository contains a collection of Python scripts developed as part of the ALX Higher Level Programming curriculum, specifically focusing on Object Relational Mapping (ORM) using Python.

## Project Overview

This project is aimed at providing solutions to various tasks involving database operations using Python and SQL, with an emphasis on ORM concepts. The tasks cover a range of topics including querying databases, creating and manipulating tables, performing CRUD operations, and handling SQL injections.

## Task List

### Task 0: Get all states
- **File:** `0-select_states.py`
- **Description:** Script to list all states from a database.

### Task 1: Filter states
- **File:** `1-filter_states.py`
- **Description:** Script to list states with names starting with 'N'.

### Task 2: Filter states by user input
- **File:** `2-my_filter_states.py`
- **Description:** Script to filter states based on user input.

### Task 3: SQL Injection...
- **File:** `3-my_safe_filter_states.py`
- **Description:** Script to filter states safely from SQL injections.

### Task 4: Cities by states
- **File:** `4-cities_by_state.py`
- **Description:** Script to list all cities grouped by states.

### Task 5: All cities by state
- **File:** `5-filter_cities.py`
- **Description:** Script to list all cities of a specific state.

### Task 6: First state model
- **File:** `model_state.py`
- **Description:** Definition of the State class and Base instance.

### Task 7: All states via SQLAlchemy
- **File:** `7-model_state_fetch_all.py`
- **Description:** Script to list all State objects using SQLAlchemy.

### Task 8: First state
- **File:** `8-model_state_fetch_first.py`
- **Description:** Script to print the first State object from the database.

### Task 9: Contains 'a'
- **File:** `9-model_state_filter_a.py`
- **Description:** Script to list states containing the letter 'a'.

### Task 10: Get a state
- **File:** `10-model_state_my_get.py`
- **Description:** Script to print the State object with a specified name.

### Task 11: Add a new state
- **File:** `11-model_state_insert.py`
- **Description:** Script to add a new State object to the database.

### Task 12: Update a state
- **File:** `12-model_state_update_id_2.py`
- **Description:** Script to update the name of a State object.

### Task 13: Delete states
- **File:** `13-model_state_delete_a.py`
- **Description:** Script to delete State objects based on certain criteria.

### Task 14: Cities in state
- **Files:** `model_city.py`, `14-model_city_fetch_by_state.py`
- **Description:** Definition of the City class and script to fetch cities by state.

### Task 15: City relationship
- **Files:** `relationship_city.py`, `relationship_state.py`, `100-relationship_states_cities.py`
- **Description:** Enhanced definitions of City and State classes with relationship mapping.

### Task 16: List relationship
- **File:** `101-relationship_states_cities_list.py`
- **Description:** Script to list all states and corresponding cities using relationship mapping.

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the appropriate directory for the task you wish to run.
3. Execute the Python script with appropriate arguments as specified in the task description.

## Notes

- Ensure you have the required dependencies installed, especially `MySQLdb` and `SQLAlchemy`.
- Make sure to use correct MySQL credentials and database names while executing the scripts.
