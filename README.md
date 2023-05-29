# Inventory App

The Inventory App is a command-line application developed in Python for managing a list of shoes in an inventory. It provides various functionalities for interacting with the inventory, such as reading the data from a file, capturing new shoe details, viewing all the shoes in a tabular format, restocking shoes, searching for a shoe by its product code, calculating the value of each item, and identifying the item with the highest quantity.

## Running with Docker

To run the application using Docker, follow these steps:

1. Make sure Docker is installed on your system.
2. Clone this repository: `git clone https://github.com/moeketsisegalo/inventory_app.git`
3. Navigate to the project directory: `cd inventory_app`
4. Build the Docker image: `docker build -t inventory_app .`
5. Run the Docker container: `docker run -it inventory_app`

The application will be executed inside the Docker container, and you should see the output on your console.

## Running with an IDE

To run the application using an IDE, follow these steps:

1. Make sure you have Python installed on your system .
2. Clone this repository: `git clone https://github.com/moeketsisegalo/inventory_app.git`
3. Open the project in your favorite IDE.
4. Install the dependencies listed in the `requirements.txt` file. You can do this by running: `pip install -r requirements.txt`
5. Locate the `inventory.py` file and open it.
6. Run the `inventory.py` file from your IDE.

The application will be executed, and you should see the output on your console.


## Usage

1. Run the `inventory.py` file to start the application.
2. Select an option from the menu to perform the desired operation.
3. Follow the on-screen prompts to enter the required information.
4. The application will perform the selected operation and provide the appropriate output.

Make sure to install the `prettytable` module before running the application. You can install it using the following command:
```
python -m pip install -U prettytable
```

Note: This application uses a file named `inventory.txt` to store the inventory data. Make sure the file exists in the same directory as the `inventory.py` file.

## Credits

This Inventory App was developed as part of an educational project by Moeketsi Segalo under the guidance of HyperionDev.

Feel free to explore the functionalities of the Inventory App and manage your shoe inventory efficiently!

