#  headline-vs-headline
**Docker Branch**
---

All the code, packaged nicley in a docker container.

## Usage
To run the web server for yourself, follow these steps:
1. Download [docker](https://www.docker.com/) onto your machine
2. If you have Django installed, generate a SECRET_KEY by running `python3 newSecretKey.py` and put it in a new file SECRET_KEY.txt. If you don't you un comment the line in `headlineVsHeadline/headlineVsHeadline/settings.py`, however, this is very insecure.
3. Create a new [Firebase](https://firebase.google.com) project and add a cloud firestore data base. From there, [create a service account](https://firebase.google.com/docs/admin/setup#initialize-sdk) and download the accompanying Json file. Place it in the root of this project and name it `headline-vs-headline-firebase-adminsdk.json`.
4. Build the dockerfile by running `docker build -t headline-vs-headline .` (you can replace headline-vs-headline with anything)
5. Run the docker image locally with the command `docker run -p 80:8000 headline-vs-headline` to spin up a container.
6. **Finally**, visit [localhost](localhost:80) and check it out!

## License
Please see the included MIT license, and comments describing intentions within the code.

## Contact
Please feel free to contact me via [email](mailto:bacarpenter04@gmail.com)