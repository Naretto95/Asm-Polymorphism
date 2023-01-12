# Asm-Polymorphism

This project is a Python script for generating a new file from a given assembly file, with a new signature that does not exist in the payload.txt file. The goal of this project is to demonstrate the concept of polymorphism in assembly code.

## Features
- Generates a new assembly file from a user-specified input file
- The new file has a different signature from the original file, as well as from the payload.txt file
- Demonstrates the concept of polymorphism in assembly code

## Getting Started
To run this project on your local machine, you will need Python 3 installed.

1. Clone the repository to your local machine:
```
git clone https://github.com/Naretto95/Asm-Polymorphism.git
```
2. Run the script:
```
python generator.py
```
3. The program will prompt you for the location of the assembly file to modify, and the location to save the new file.

## Usage
The script will prompt the user for the location of the assembly file to modify and the location to save the new file. Once the input file is selected and read, the script will generate a new signature, and create a new file with the modified code and the new signature.

## Contribution
We are open to contributions and suggestions. If you would like to contribute, please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
This project uses Python libraries for working with assembly code.
