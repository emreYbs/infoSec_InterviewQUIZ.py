# infoSec_InterviewQUIZ.py
# *A simple CLI Quiz app based on InfoSec Interview Questions*

**Usage:** </br>
infoSec_InterviewQUIZ.py [OPTIONS] COMMAND [ARGS]...

 
![image](https://user-images.githubusercontent.com/59505246/137523167-4cc8d1ae-e9de-4f14-8c22-ad7856a6d6ae.png)


To run the app, go to the folder and **pyton3 infoSec_InterviewQUIZ.py start**</br>  Then, you'll see this selection part. You can choose these 3 areas. Later,I'll add new sections and more questions. Now, the number of questions is insufficient.

![image](https://user-images.githubusercontent.com/59505246/137523703-f2ee235f-9ad1-41e7-ae8d-24dc5a125ad0.png)


![image](https://user-images.githubusercontent.com/59505246/137524255-6dbb122c-9798-4f22-90dd-ef7175ebe0cf.png)

**You can see your result:)**

![image](https://user-images.githubusercontent.com/59505246/137524573-c37736d3-df7a-4ff5-86dd-ca6adb68521e.png)

**Options:**</br>
  --version  Show the version and exit.
  --help     Show this message and exit.

**Commands:**</br>
  info   Info About App python3 infosec_quiz.py info
  start  Start Quiz python3 infosec_quiz.py start
  


## To start:   *python3 infoSec_InterviewQUIZ.py start*  

## For help:   *python3 infoSec_InterviewQUIZ.py --help* 

### Notes: in Python Venv, you can get no module error for the library "PyInquirer" although you have installed it, unfortunately. However, Works normally when installed "pip3 install PyInquirer", instead of installing on a virtual python environment.

For now, there are **few** questions about **Cryptography, Network and Web Foundations**. I'll add more questions and make it useful for someone who is studying for some infoSec related certificate exams or infoSec job interviews.

# Example Question (out of cryptography_questionsList _and_ network_questionsList):

*"Symmetric encryption uses the same key for both encryption and decryption - much faster but the key needs to be transferred over an unencrypted channel.*  **(a)True,  (b)False** </br>

*"Asymmetric encryption: uses different keys for encryption and decryption - more secure but slow.*  **(a)True  (b)False**

*"VPN runs through the computer servers of thousands of volunteers (over 4,500 ) spread throughout the  world.*   **(a)True  (b)False**

*"ARP spoofing is a type of attack in which a malicious actor sends falsified ARP (Address Resolution Protocol) messages over a local area network.*   **(a)True  (b)False**

Thanks to Jesse(https://github.com/Jcharis), I got his Udemy Course "Building Command Line Tools" and in his video tutorial,which was great by the way, there was a quiz app which exams you about tech, history, Bible,etc. And I coded the version for my own needs. *Feel free to make it better for your own needs. With the help of Click Library, and with more questions, you can make various kinds of CLI quiz tools.*
