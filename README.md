# rpete

rpete is a command line tool created to measure the repeat rate and repeat delay of your keyboard over multiple operating systems. The goal of rpete is to help users synchronize keyboard settings across various machines and operating systems.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Additional Tools](#additional-tools)
- [License](#license)

## Installation

1. Clone this repository:
```bash
git clone git@github.com:coreyMerritt/rpete
```
2. Install necessary dependencies:
  - All users will need the libraries: Keyboard and Pendulum:
  ```bash
  pip install keyboard
  pip install pendulum
  ```

  - Windows users will also need the "windows-curses" library:
  ```powershell  
  pip install windows-curses
  ```

## Usage

1. Navigate to the directory that contains rpete.py and run the tool:
```bash
python3 rpete.py
```
(Please note that Linux users will be forced to run the tool with sudo due to dependencies requirements)

2. Follow the on-screen instructions.

## Additional Tools

This repository also includes the error_margin tool used to check if the error margin of the Pendulum and Time libraries would be sufficient for the rpete project, this tool wasn't designed to be used by users but was left in the repo for anyone curious that wishes to use it. This tool can be run exactly the same way as rpete and requires no additional dependencies that aren't already demanded from rpete.

## License

This project is licensed under the [MIT License](LICENSE).
