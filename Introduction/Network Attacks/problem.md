Several of the challenges are dynamic and require you to talk to our challenge servers over the network. This allows you to perform man-in-the-middle attacks on people trying to communicate, or directly attack a vulnerable service. To keep things consistent, our interactive servers always send and receive JSON objects.

Python makes such network communication easy with the telnetlib module. Conveniently, it's part of Python's standard library, so let's use it for now.

For this challenge, connect to socket.cryptohack.org on port 11112. Send a JSON object with the key buy and value flag.

The example script below contains the beginnings of a solution for you to modify, and you can reuse it for later challenges.

Connect at nc socket.cryptohack.org 11112

telnetlib_example.py

You have solved this challenge!