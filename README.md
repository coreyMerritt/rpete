# rPete

rPete is a command line tool created to measure the repeat rate and repeat delay of your keyboard over multiple operating systems. The goal of rPete is to help users synchronize keyboard settings across various machines and operating systems.
<br></br>
## Table of Contents

- [Running with Docker](#running-with-docker)
- [Running on Host](#running-on-host)
	- [Installation](#installation)
	- [Usage](#usage)
	- [Additional Tools](#additional-tools)
- [License](#license)
<br></br>
## Running with Docker

1. Ensure that you have Docker properly installed on your system.
	- https://docs.docker.com/get-docker/

2. Pull the image onto your machine.
	```bash
	docker pull coreyleemerritt/rpete:latest
	```

3. Run the image.
	```bash
	docker run -it coreyleemerritt/rpete:latest
	```
<br></br>
## Running on Host

### Installation

1. Clone this repository.
```bash
git clone git@github.com:coreyMerritt/rpete
```

2. Install necessary dependencies.

	- All users will need the Pendulum library:
  	
	```bash
  	pip install pendulum
  	```


	- Windows users will also need the "windows-curses" library:
  
 	```powershell  
  	pip install windows-curses
  	```
<br></br>
### Usage

1. Navigate to the directory that contains rpete.py and run the tool.

```bash
python3 rpete.py
```

	- (Linux users will be forced to run the tool with sudo due to dependencies requirements)

2. Follow the on-screen instructions.

<br></br>
### Additional Tools

This repository also includes the error_margin tool used to check if the error margin of the Pendulum and Time libraries would be sufficient for the rPete project, this tool wasn't designed to be used by users but was left in the repo for anyone curious that wishes to use it. This tool can be run exactly the same way as rPete and requires no additional dependencies that aren't already demanded from rPete.
<br></br>
## License

This project is licensed under the [MIT License](LICENSE).
