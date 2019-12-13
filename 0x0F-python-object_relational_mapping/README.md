# 0x0F. Python - Object-relational mapping

### Background Context

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (**ORM**). 


| File | Description |
|:----:|-------------|
| [Select States](0-select_states.py)| Get all states, using the package MySQLdb |
| [Filter States](1-filter_states.py)| Get all states, get all states with a name starting with N (upper N) from the database hbtn_0e_0_usa |
| [Select by user input](2-my_filter_states.py)| Get the states, takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. |
| [SQL Injection](3-my_safe_filter_states.py)| take the arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections! |
| [Select cities by state](4-cities_by_state.py)| Get all cities by state |
| [All cities by state](5-filter_cities.py)| takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa |
| [First state model](model_state.py)| file that contains the class definition of a State and an instance Base = declarative_base() |
| [All states via SQLAlchemy](7-model_state_fetch_all.py)| lists all State objects from the database hbtn_0e_6_usa |
| [First state](8-model_state_fetch_first.py)| prints the first State object from the database hbtn_0e_6_usa |
| [Contains \`a\`](9-model_state_filter_a.py)| lists all State objects that contain the letter a from the database hbtn_0e_6_usa |
| [Get a state](10-model_state_my_get.py)| prints the State object with the name passed as argument from the database hbtn_0e_6_usa |
| [Add a new state](11-model_state_insert.py)| that adds the State object “Louisiana” to the database hbtn_0e_6_usa |
| [Update a state](12-model_state_update_id_2.py)| changes the name of a State object from the database hbtn_0e_6_usa |
| [Delete states](13-model_state_delete_a.py)| deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa |
| [Select cities by state](14-model_city_fetch_by_state.py)| that prints all City objects from the database hbtn_0e_14_usa using the file [model_state.py](model_state.py) |



