# privy

`privy` is a simple tool for secured p2p chat which leveraged gcrypt for encryption.

## privy-daemon

`privy-daemon` is a server which needs to be running for messages to be sent or recieved. Ideally this process is always running to maximize the chances of receiving an incoming message.

A message in the send-queue is kept there until successfully received by the other peer. Successful reception of a message requires the following:

1. Sending party encrypts the message and randomly generated keyphrase using the public key of the receiving party

2. Receiving party decrypts the message body and keyphrase.

3. Receiving party hashes the message body and sends it back to the sender.

3. Sender checks that hash matches expectation, if so the send is a success.

## privy

`privy` is a simple tool to send, recieve, and check the status of the `privy-daemon`