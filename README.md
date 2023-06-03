# EchoLink - Open Source
What Is "EchoLink"? Well, ignoring the AWESOME name. The EchoLink project is a server-client communication script developed in Python. It enables users to establish a chat session by connecting to a central server. The server acts as a host, facilitating communication between multiple clients. Upon launching the client-side script, users are prompted to enter a username. This username is then used for subsequent sessions. The clients can send and receive messages, which are transmitted through the server to all connected clients. The chat messages are displayed in a standard format, showing the username of the sender along with the message content. The server-side script logs all chat activity, including user joins, disconnects, and messages sent, with corresponding timestamps. This log is printed in the server's console, providing administrators with a record of the chat session. The project ensures security by requiring users to connect with a valid username. Clients are unable to access the chat session or send/receive messages without first being authenticated by the server.
## Language Information
EchoLink is implemented in Python using mainly the requests package. The choice of Python as the programming language empowers the project with a rich set of features.
## Setup & Installation
To set up and install EchoLink, please follow the steps below:
- Ensure that you have a fairly recent version of Python installed on your system.

- Download a stable release of EchoLink from this repository.

- Open the folder marked as "server", then open the Python file within the server folder. This file should be named "server.py", after opening the file near the top will be the "Server Configuration" section. Please edit this as deemed fit by you.

- After choosing your port and IP options, navigate out of the server folder and now enter the client folder. Open the client.py file and change the "Connection configuration" section to the same details as the server.

- Now, both server & client have the same connection information everything should just work. Opening the server.py file in Python will display a Python shell of the server's log. Opening the client.py file in Python will display the client's display.
## Usage
Before utilizing the provided code, please take note of the following guidelines and restrictions:

**Code Usage Intentions:** This code is intended for legitimate and ethical purposes only. It should not be used with malicious intent, such as engaging in hacking, unauthorized access, or any other illegal activities. By using this code, you agree to abide by ethical standards and applicable laws.

**Modification and Alteration:** Users are permitted to modify and customize the code according to their specific requirements. However, it is essential to respect the original author's work and intentions when making alterations.

**No Commercial Profit:** Users are not allowed to sell or distribute the modified code for profit without obtaining explicit permission from the original author. The code should be used for personal, educational, or non-commercial purposes only.

**Fair Credit:** If the modified code or any portion of it is re-uploaded or shared elsewhere by someone other than the original author, it is expected that proper credit is given to the original author. Acknowledging the original source demonstrates respect for the work and effort put into developing the code.

**Liability and Legal Responsibility:** The original author of the code is not responsible for any legal or online actions resulting from the usage of the code. Users assume full liability for their actions and must ensure compliance with all applicable laws and regulations.

By utilizing this code, you acknowledge and agree to these terms and conditions. It is important to exercise responsible and ethical behavior while using this code to maintain a positive and lawful online environment.
## Features
- Just a simple text-chat session.
## FAQ

#### Can I Use This With Others?

Yes! You would have to port-forward the same port in the "server.py" file and have it launched before any client can connect but yes you can, that is what this project was designed for. A multi-client chat session!

## Contributing / Feedback
If you would like to add feedback on this project or feel like helping us out by giving us code, you can find contact the owner multiple ways, however the best and most effective way would be via Discord. You can join the Discord server and contact "TCSMasked" via text channels about this project there. You can join using this link:
**https://discord.maskednet.org/**
