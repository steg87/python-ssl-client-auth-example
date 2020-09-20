openssl req -newkey rsa:2048 \
            -x509 \
            -sha256 \
            -days 3650 \
            -nodes \
            -out client.crt \
            -keyout client.key \
            -subj "/C=UK/ST=Scotland/L=Glasgow/O=Company A/OU=Testing/CN=MyName"