# flask-crypto

      
      
      A flask extension which provide interface(API) to cryptography library of python.  
      
      
      


**Prerequisites**
------------------

know how to use flask extensions
pip3 install -r requirements.txt



**using** 
--------  

 Currently under developement <br>
 Welcoming you all to contribute in any possible way.
 Please have a look at the todo.  
 
 <br>
 For now
 ```
 from flask import Flask
 app=Flask(__name__)
 
 crpt=Crypto(app)
 #api to calculate key using PKCS7
 key=crpt.key_derive(b'data')
 #api to verify the key 
 crpt.key_verify(b'data', key)
 
 ```
 
    
**TODO**
---------

- [ ] write configuration parameter for the extension.
- [ ] file encryption and decryption support using asymmetric key encryption
- [ ] API for PGP(preety good privacy)
- [ ] coming up with the use case for API support to use asymmetric key encryptio

**Contributing**
----------------
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


