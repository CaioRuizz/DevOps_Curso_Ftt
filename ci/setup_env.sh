mkdir certs

echo "$CA_PEM"

echo "$CA_PEM" > certs/ca.pem
echo "$CERT_PEM" > certs/cert.pem
echo "$CONFIG_JSON" > certs/config.json
echo "$ID_RSA" > certs/id_rsa
echo "$ID_RSA_PUB" > certs/id_rsa.pub
echo "$SERVER_KEY_PEM" > certs/server-key.pem
echo "$SERVER_PEM" > certs/server.pem

chmod 400 certs/*