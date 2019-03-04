#**Spartan Messenger**

Spartan Messenger using GRPC in Python3


Implementation of the following are supported:

- One-on-one conversations between users

- Implementation of LRU cache is supported for storing latest messages. Size of the LRU can be modified

- End to end message encryption is using AES algorithm

- Groups chats with other users is supported

---

## File Structure

- chat.proto (Contains Protbuf services)
- server.py (Contains server side implementation)
- client.py (Contains client side implementation)
- spartan_crypto.py (Contains methods to encrypt and decrypt messages)
- chatlog.py (Contains logging related methods and levels)

---

## File configurations:

**Settings in config.yaml file**

Add users and groups with respective users in the group in the _config.yaml_ file

**Settings in chatlog.py file**

For debugging purpose, enable the following option in _chatlog.py_ file:

**DEBUG = False**
to 
**DEBUG = True**

---

## How to use 1 to 1 chat

##NOTE: To get a response from another client please press _**ENTER**_ key, this is used to avoid uneven display of messages using threading.

_To launch server:_

**$ python3 server.py**

Spartan server started on port 50051.


_To launch alice as a client:_

**$ python3 client.py alice**

[Spartan] Connected to Spartan Server at port 50051.

[Spartan] User list: bob,charlie,foo,bar,cab

[Spartan] Enter a user whom you want to chat with: bob

[Spartan] You are now ready to chat with bob.

[alice] > hey bob, I'm alice

[alice] > hey how are you

[bob] hey alice, I'm bob

[alice] >

_To launch bob as a client:_

**$ python3 client.py bob**

[[Spartan] Connected to Spartan Server at port 50051.

[Spartan] User list: alice,charlie,foo,bar,cab

[Spartan] alice is requesting to chat with you. Enter 'yes' to accept or enter different user: yes

[Spartan] You are now ready to chat with alice.

[alice] hey bob, I'm alice

[bob] > hey alice, I'm bob

[bob] > 

[alice] hey how are you

---

## How to use group chat

_To chat with 'cab' group of members alice, bob, charlie and **alice** as a client:_

**$ python3 client.py alice**

[[Spartan] Connected to Spartan Server at port 50051. 

[Spartan] User list: bob,charlie,foo,bar,cab

[Spartan] Enter a user whom you want to chat with: cab

[Spartan] You are now ready to chat with cab.

[alice] > hey bob and charlie, I'm alice

[alice] > 

[bob] hey alice and charlie, I'm bob

[charlie] hey alice and bob, I'm charlie


_To chat with 'cab' group of members alice, bob, charlie and **bob** as a client:_

**$ python3 client.py bob**

[[Spartan] Connected to Spartan Server at port 50051. 

[Spartan] User list: bob,charlie,foo,bar,cab

[Spartan] Enter a user whom you want to chat with: cab

[Spartan] You are now ready to chat with cab.

[alice] > hey bob and charlie, I'm alice

[alice] > 

[bob] hey alice and charlie, I'm bob

[charlie] hey alice and bob, I'm charlie


_To chat with 'cab' group of members alice, bob, charlie and **charlie** as a client:_

**$ python3 client.py charlie**

[Spartan] Connected to Spartan Server at port 50051.

[Spartan] User list: alice,bob,foo,bar,cab

[Spartan] cab is requesting to chat with you. Enter 'yes' to accept or enter different user: yes

[Spartan] You are now ready to chat with cab.

[alice] hey bob and charlie, I'm alice

[charlie] > hey alice and bob, I'm charlie

[bob] hey alice and charlie, I'm bob

[charlie] >

---
