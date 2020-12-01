# Shared
![Shared](https://user-images.githubusercontent.com/62826765/100805523-1546c980-342f-11eb-8b18-ac5a59338dc4.png)

Its **RSA** challenge, we were given two pairs *(n,e1)*, *(n,e2)* and two ciphers. It seems that the message encrypted two times with the same modulus but with different exponents.

With some researchs, this leads us to [Common Modulus Attack](https://crypto.stackexchange.com/questions/16283/how-to-use-common-modulus-attack)

## Attack :
**Bezout’s Theorem** says that if there are two integers a and b (not zero) then there are integers x and y such that :

![1_2ZwuBoulcRBPTxptxzh4qg](https://user-images.githubusercontent.com/62826765/100805816-a5850e80-342f-11eb-919d-c7f6504b09a5.png)

Back in our context, we have *gcd(e₁, e₂) = gcd(15,13) = 1*, then we have integers x and y such that :

![1_azXxHzA4EuE_5ZQVk6x-GQ](https://user-images.githubusercontent.com/62826765/100806192-525f8b80-3430-11eb-9500-ca5f2fa5da75.png)

Now, by using **the Extended Euclidean algorithm** we can find x and y and then the plaintext can be recovered as follows :

![1_AfVkYZVMT_5qzGtgr82DDA](https://user-images.githubusercontent.com/62826765/100806318-88047480-3430-11eb-92c8-3803333bac0d.png)
