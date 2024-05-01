import base64
from Cryptodome.Hash import MD2, MD4, MD5, SHA1, SHA224, SHA256, SHA384, SHA3_224, SHA3_256, SHA3_384, SHA3_512, SHA512, SHAKE128, SHAKE256, SHA256
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

class Hash(object):
    def __init__(self, data = b"") -> None:
        self.data = data

    def md2(self):
        hashx = MD2.new()
        hashx.update(self.data)
        return hashx.hexdigest()
    
    def md4(self):
        hashx = MD4.new()
        hashx.update(self.data)
        return hashx.hexdigest()
    
    def md5(self):
        hashx = MD5.new()
        hashx.update(self.data)
        return hashx.hexdigest()
    
    def sha1(self):
        hashx = SHA1.new()
        hashx.update(self.data)
        return hashx.hexdigest()
    
    def sha224(self):
        hashx = SHA224.new()
        hashx.update(self.data)
        return hashx.hexdigest()
    
    def sha256(self):
        hashx = SHA256.new()
        hashx.update(self.data)
        return hashx.hexdigest()
    
    def sha384(self):
        hashx = SHA384.new()
        hashx.update(self.data)
        return hashx.hexdigest()

    def sha512(self):
        hashx = SHA512.new()
        hashx.update(self.data)
        return hashx.hexdigest()
    
    def sha3_224(self):
        hashx = SHA3_224.new()
        hashx.update(self.data)
        return hashx.hexdigest()
    
    def sha3_256(self):
        hashx = SHA3_256.new()
        hashx.update(self.data)
        return hashx.hexdigest()
    
    def sha3_384(self):
        hashx = SHA3_384.new()
        hashx.update(self.data)
        return hashx.hexdigest()
    
    def sha3_512(self):
        hashx = SHA3_512.new()
        hashx.update(self.data)
        return hashx.hexdigest()
    
    def shake128(self):
        hashx = SHAKE128.new()
        hashx.update(self.data)
        return hashx.hexdigest()
    
    def shake256(self):
        hashx = SHAKE256.new()
        hashx.update(self.data)
        return hashx.hexdigest()

class BaseFamily(object):
    class Encoder(object):
        def __init__(self, data: str = "") -> None:
            self.data = data

        def base16(self):
            return base64.b16encode(self.data.encode("ascii"))
        
        def base32(self):
            return base64.b32encode(self.data.encode("ascii"))
        
        def base64(self):
            return base64.b64encode(self.data.encode("ascii"))
        
        def base85(self):
            return base64.b85encode(self.data.encode("ascii"))
        
    class Decoder(object):
        def __init__(self, data: str = "") -> None:
            self.data = str(data).replace("b", "").replace('"', "").replace("'", "")

        def base16(self):
            return base64.b16decode(self.data.encode("utf-8"))
        
        def base32(self):
            return base64.b32decode(self.data.encode("utf-8"))
        
        def base64(self):
            return base64.b64decode(self.data.encode("utf-8"))
        
        def base85(self):
            return base64.b85decode(self.data.encode("utf-8"))

class Crypto(object):
    def Rsa(keysizeInit: int = 1024, publicExponent: int = 65537):
        private_key = rsa.generate_private_key(
            public_exponent=publicExponent,
            key_size=keysizeInit
        )

        public_key = private_key.public_key()

        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        return {"public": public_pem.decode('utf-8'), "private": private_pem.decode("utf-8")}
    
    class StringFog(object):
        def __init__(self, inputString: str = "") -> None:
            self.ins = inputString
        
        def encrypt(self):
            encrypted_string = ''.join(chr(ord(char) + 1) for char in self.ins)
            return encrypted_string

        def decrypt(self):
            decrypted_string = ''.join(chr(ord(char) - 1) for char in self.ins)
            return decrypted_string