# Corrupt

![2020-12-03 11_39_57-FriendlyCTF](https://user-images.githubusercontent.com/62826765/100998963-791ae080-355c-11eb-95c9-22d920977abc.png)

First, we use ```file```, ```stings``` and ```exiftool``` but we got nothing.

By looking at the hexadecimal dump of the file, we see that the file header has been modified :

![2020-12-03 12_03_30-Kali - VMware Workstation](https://user-images.githubusercontent.com/62826765/101001636-a5842c00-355f-11eb-958e-854cbf9b6337.png)

What a **File Header** means ? The File Header is a short sequence of bytes placed at the beginning of the file and used to identify its Format. See [List of file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)

For PNG files, the first 8 bytes always contain the following hexadecimal values : ```89 50 4E 47 0D 0A 1A 0A```

We use ```Hexedit``` to edit the hex values :

And now we can open the picture :


FLAG is **_Securinets{89-50-4E-47-0D-0A-1A-0A}_**
