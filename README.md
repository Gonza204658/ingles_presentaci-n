# 🚗 Parking System - Python

## Description

This project is a simple parking lot management system developed in Python.
The program allows users to register cars or motorcycles entering the parking lot and assigns them a position based on the available capacity.

The system also validates the vehicle plate length and checks if the parking lot is full before allowing entry.

## How the Program Works

The program starts by displaying a welcome message and a menu where the user can select their type of transportation.

The user has three options:

1. Register a **car**
2. Register a **motorcycle**
3. **Exit** the program

When a user selects a vehicle type, the program:

* Checks if the parking area is already full (maximum capacity is 10 vehicles).
* Requests the vehicle plate.
* Validates that the plate contains **exactly 6 characters**.
* Registers the vehicle and assigns a parking position.

The program keeps running using a **while loop** until the user selects the option to exit.

## Technologies Used

* Python 3

## Concepts Used in the Code

This program uses several basic programming concepts such as:

* Variables
* Conditional statements (`if`, `elif`, `else`)
* Loops (`while`)
* Counters
* User input (`input`)
* String validation (`len()`)

## Example of Code Logic

```
Carros_adentro = 5
Carros_ingresan = 0
motos_adentro = 5
motos_ingresan = 0
activador = 1
```

These variables store the number of vehicles already in the parking lot and the number that enter during the program execution.

## Author

Diego Fernando González Henríquez
