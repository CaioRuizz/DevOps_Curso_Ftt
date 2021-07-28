mkdir certs

echo $CA | base64 -d > certs/ca.pem
echo $CERT | base64 -d > certs/cert.pem
echo $KEY | base64 -d > certs/key.pem