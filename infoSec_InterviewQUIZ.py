#!/bin/bash

import click
from PyInquirer import prompt
#in Python Venv, you can get no modeule for PyInquirer, unfortunately.

class Quiz:
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer

#infosec_interviewQuestionsList
cryptography_questionsList =[
"Symmetric encryption uses the same key for both encryption and decryption - much faster but the key needs to be transferred over an unencrypted channel.\n(a)True,\n(b)False\n\n",
"Asymmetric encryption: uses different keys for encryption and decryption - more secure but slow.\n(a)True,\n(b)False\n\n",
"Using a hybrid approach should not be preferred. Setting up a channel using asymmetric encryption and then sending the data using symmetric process.\n(a)True,\n(b)False\n\n",
"Examples of Symmetric Encryption Algorithms: Diffie Hellman, RSA\n(a)True,\n(b)False\n\n",
"How does  Asymmetric (Public-Key Cryptography) encryption Works? >> Sender encrypts the message using receiver's public key, Receiver decrypts the message using his own private key.\n(a)True,\n(b)False\n\n"
"A public key infrastructure (PKI) is a set of roles, policies, and procedures needed to create, manage, distribute, use, store, and revoke digital certificates and manage public-key encryption.\n(a)True,\n(b)False\n\n"
]

cryptography_questions =[
Quiz(cryptography_questionsList[0],"a"),
Quiz(cryptography_questionsList[1],"a"),
Quiz(cryptography_questionsList[2],"b"),  # Hybrid approach should be prefered.
Quiz(cryptography_questionsList[3],"b"),  # Diffie Hellman, RSA are Asymmetric Encryption Algorithms
Quiz(cryptography_questionsList[4],"a"),
Quiz(cryptography_questionsList[4],"a")
]

network_questionsList =[
"What port does ping work over? >> ICMP is a layer 3 protocol (it doesn’t work over a port) -Also, TCP and UDP are layer 4 protocols and not related to ping.\n(a)True,\n(b)False\n\n",
"VPN runs through the computer servers of thousands of volunteers (over 4,500 at time of publishing) spread throughout the  world.\n(a)True,\n(b)False\n\n", 
"ARP spoofing is a type of attack in which a malicious actor sends falsified ARP (Address Resolution Protocol) messages over a local area network.\n(a)True,\n(b)False\n\n",
"Enable SNMP service to be safe.Disabling SNMP is very dangerous.\n(a)True,\n(b)False\n\n"
]

network_questions =[
Quiz(network_questionsList[0],"a"),
Quiz(network_questionsList[1],"b"),  # Not Vpn but TOR network
Quiz(network_questionsList[2],"a"),
Quiz(network_questionsList[3],"b")  # Disable SNMP if it is not required
]


web_questionsList =[
"What is CSRF? \n(a) a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database.\n(b) a web application vulnerability in which the server does not check whether the request came from a trusted client or not.\n\n",  # b
"Update/Patch the web server software, Minimize the server functionality disable extra modules, Delete default data/scripts, Increase logging verboseness, Update Permissions/Ownership of files\n(a)For Web Server Hardening \n(b)For brute forcing\n\n",  #a
"Response Code: 5xx - Server side error\n(a)True,\n(b)False\n\n", # a
"2xx - Informational responses\n(a)True,\n(b)False\n\n", #b
"Blind SQLi (Boolean-based, Time-based)\n(a)True,\n(b)False\n\n" # a
]


web_questions =[
Quiz(web_questionsList[0],"b"),
Quiz(web_questionsList[1],"a"),
Quiz(web_questionsList[2],"a"),
Quiz(web_questionsList[3],"b"),
Quiz(web_questionsList[4],"a")
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    click.secho("You have scored {} out of {}".format(score,len(questions)),fg='white',bg='blue')



@click.group()
@click.version_option(prog_name='InfoSec Quiz',version='0.0.1')
def main():
    """A simple CLI Quiz app based on InfoSec Interview Questions"""
    pass

@main.command()
def start():
    """Start Quiz
    python3 infosec_quiz.py start
    """
    click.secho("Starting infosec_quiz",fg='blue')
    quiz_type = [
    {'type':'list','name':'questiontype','message':'Question Type',
            'choices':["Cryptography","Network","Web"]
    }
    ]
    answer_quiz_type = prompt(quiz_type)

    if answer_quiz_type['questiontype'] == 'Cryptography':
        click.echo("Starting...Let's see if you have some basic knowledge about cryptography \n")
        run_quiz(cryptography_questions)
    elif answer_quiz_type['questiontype'] == 'Network':
        click.echo("Starting...Let's see if you have some basic knowledge about networks\n")
        run_quiz(network_questions)
    elif answer_quiz_type['questiontype'] == 'Web':
    	click.echo("Starting...Let's see if you have some basic knowledge about Web Foundations\n")
    	run_quiz(web_questions)


@main.command()
def info():
    """Info About App
    python3 infosec_quiz.py info
    """
    click.secho("Infosec_quiz CLI",fg='white',bg='blue')
    click.secho("EmreYbs",fg='blue')

if __name__ == '__main__':
    main()
