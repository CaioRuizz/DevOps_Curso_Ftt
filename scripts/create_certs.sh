mkdir certs
echo $CA | base64 -d > certs/ca.pem
cat certs/ca.pem
echo $CERT | base64 -d > certs/cert.pem
cat certs/cert.pem
echo $KEY | base64 -d > certs/key.pem
cat certs/key.pem