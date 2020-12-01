# Shared
![Shared](https://user-images.githubusercontent.com/62826765/100805523-1546c980-342f-11eb-8b18-ac5a59338dc4.png)

Its **RSA** challenge, we were given two pairs *(n,e1)*, *(n,e2)* and two ciphers. It seems that the message encrypted two times with the same modulus but with different exponents.

With some researchs, this leads us to [Common Modulus Attack](https://crypto.stackexchange.com/questions/16283/how-to-use-common-modulus-attack)

## Attack
**Bezout’s Theorem** says that if there are two integers a and b (not zero) then there are integers x and y such that :

![1_2ZwuBoulcRBPTxptxzh4qg](https://user-images.githubusercontent.com/62826765/100805816-a5850e80-342f-11eb-919d-c7f6504b09a5.png)

Back in our context, if we have *gcd(e₁, e₂) = 1*, then we have integers x and y such that :

![1_azXxHzA4EuE_5ZQVk6x-GQ](https://user-images.githubusercontent.com/62826765/100806192-525f8b80-3430-11eb-9500-ca5f2fa5da75.png)

Now, by using **the Extended Euclidean Algorithm** we can find x and y and then the plaintext can be recovered as follows :

![1_AfVkYZVMT_5qzGtgr82DDA](https://user-images.githubusercontent.com/62826765/100806318-88047480-3430-11eb-92c8-3803333bac0d.png)

## Exploit
```python
from Crypto.Util.number import long_to_bytes
from sympy import invert

def egcd(a, b): #Extended Euclidean Algorithm
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)


n = 56891607317613445737750783421867972775249572399868790441120633009929442237956426430872259524747190957003843589191818005172449569095010326902570697779311445080658255239480648637639774011002922525938326812054289272761548189515649720401657615661945821118048442804640057370308200873641231270154569615397630035523
e1 = 15
e2 = 13
c1 = 56469309419621722745072264207838652962328435946767997622044814783708364014641727623574445134141501637979157915357991990349560025038641029733835390776874211827838349081746055988558104358822972488360758486671776227087938906728676579783033437913622465886682124098078049146249446462955542454130870990925587760172
c2 = 32329112615946008400629911894435459433005895247408214608443373037890224605212549196731172020927876324933946521979508705874232456594545880155126627698928055303619040189497194414548410456513691315796957680520443150673697523600966755935741384614826849213578224143275544065415119993769274896134376873260076292691

gcd, x, y = egcd(e1, e2)
assert gcd == 1
assert invert(pow(c2,y,n),n)

m = (pow(c1,x,n) * pow(c2,y,n)) % n
print(long_to_bytes(m))
```


FLAG is **_Securinets{c0mmon_m0dulus}_**
