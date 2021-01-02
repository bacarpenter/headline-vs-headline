#  headline-vs-headline

Hello! This is a small project I am going to work on to keep my self busy over the holliday break. It is based off of an idea from [this](https://www.youtube.com/watch?v=JTOJsU3FSD8&ab_channel=Fireship) YouTube video.

**Goal:** My goal is to create a site that allows people to see how different media organizations view the world. As a learning oppertunity, I am getting to learn how to preform webscraraping, xPath, and furthering my knowladge on Python & Django.

## Status
Functionality is **done** 😌

##  Usage (Out dated)

To start your own server, please follow these steps:
1. Clone the repo onto your machine. `git clone https://www.github.com/bacarpenter/headline-vs-headline.git`

2. Install the required packages with `pip3 install requirements.txt`

3. Download google chrome (if you don't already have it) and chrome driver. Add the location of the chrome driver binary to PATH

4. Generate a django secret key with `ADD COMMAND` and place it in a new txt file, 	`headlineVsHeadline/headlineVsHeadline/SECRET_KEY.txt`

5. Create a new firebase project [here](https://firestore.google.com) and add a cloud firestore database to it. Genorate a new credential secret key, and put it in the root of the project. Name the .jason `headline-vs-headline-firebase-adminsdk.json`

6. Start the web server on local host port 8000 by running `python3 headlineVsHeadline/manage.py runserver`

7. Check it out on [local host](http://localhost:8000)!

*I will be hosting a web version soon, so you won't need to do all this :)*

##  Project todo list

-  [x] Install and quickstart selenium

- [x] Understand selecting elements with selenium
	- [x] By Class
	- [x] By Id
	- [x] By Xpath

- [x] Implament news sources
	- [x] Fox News
	- [x] MSNBC 
	- [x] New York Times
	- [x] Washington Post

- [x] Begin a Django project to visualize the collected data

- [x] Implament a data base.
	- [x] Choose a data base. SQL? **Firestore?** MongoDB? ect.
	*Firestore DB implamented‼️*

- [x] Write a citation generator. 

- [x] Implament citation generator
	- [x] Fox
	- [x] MSNBC
	- [x] Washington Post
	- [x] New York Times

- [x] Design web interface
- [x] Implament a web interface

- [ ] Create docker container
- [x] Write a usage file, requirments.txt, ect.
- [ ] Deploy to cloud. Heroku?

### Streach Goals:
- [ ] Add aditional news sites to get data from.
- [ ] Implament an automatic testing program

## License
Please see the included MIT license, and comments describing intentions within the code.


## Contact
Please feel free to contact me via [email](mailto:bacarpenter04@gmail.com)
