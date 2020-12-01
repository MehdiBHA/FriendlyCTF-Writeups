# Shared
![Flipper](https://user-images.githubusercontent.com/62826765/100805482-0233f980-342f-11eb-83db-fb9da44e1e34.png)

Its **RSA** challenge, we were given two pairs *(n,e1)*, *(n,e2)* and two ciphers. It seems that the message encrypted two times with the same modulus but with different exponents.

With some researchs, this leads us to [Common Modulus Attack](https://crypto.stackexchange.com/questions/16283/how-to-use-common-modulus-attack)

### Let's start attacking :
**Bezout’s Theorem** says that if there are two integers a and b (not zero) then there are integers x and y such that :

![1_2ZwuBoulcRBPTxptxzh4qg](https://user-images.githubusercontent.com/62826765/100805816-a5850e80-342f-11eb-919d-c7f6504b09a5.png)
