# ssl

The instruction are for windows:

all that in help from https://gist.github.com/KeithYeh/bb07cadd23645a6a62509b1ec8986bbc

all the files are from that link and exectly from there.

key.pem file is the example.com.key file that I create using that command:

openssl rsa -in example.com.key -out key.pem 

cert.pem file is the example.com.crt file that I create using that command:

openssl x509 -in example.com.crt -out cert.pem -outform PEM

you can copy my server.py is just very simple server in flask.

after all that you need to take the example.com.crt file and add him to the mmc

you can do it like that:

winkey+r -> write mmc + enter -> file snap in -> certificate -> add -> coputer account + next -> finish -> ok.

certificate(local coputer) -> trusted root certificates authorities -> right click on certificate -> all tasks -> import -> next -> browse to the example.com.crt in yout computer -> next ->  trusted root certificates authorities -> next -> finish/ok.

now you can activate the server.py by this command on the terminal:

python server.py

you need to change your defualt browser to chrom before that.

now it is need to work and be secure https on chrom.




