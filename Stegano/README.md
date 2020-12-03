# Corrupt

![2020-12-03 11_39_57-FriendlyCTF](https://user-images.githubusercontent.com/62826765/100998963-791ae080-355c-11eb-95c9-22d920977abc.png)

Using ```file``` and ```exiftool``` doesn't show us a thing.

By looking at the hexadecimal dump of the file, we see that the PNG file header has been modified :

![2020-12-03 12_03_30-Kali - VMware Workstation](https://user-images.githubusercontent.com/62826765/101001636-a5842c00-355f-11eb-958e-854cbf9b6337.png)

What a **File Header** means ? The File Header is a short sequence of bytes placed at the beginning of the file and used to identify its Format. See [List of file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)

For PNG files, the first 8 bytes always contain the following hexadecimal values : ```89 50 4E 47 0D 0A 1A 0A```

We use ```hexedit``` to edit the hex values :

![2020-12-03 12_07_58-Kali - VMware Workstation](https://user-images.githubusercontent.com/62826765/101002404-48d54100-3560-11eb-9fca-c04d334b81bc.png)

And now we can open our picture and get the flag :

![corrupt](https://user-images.githubusercontent.com/62826765/101003164-7de19380-3560-11eb-844e-78193a22e6e6.png)

FLAG is **_Securinets{89-50-4E-47-0D-0A-1A-0A}_**
