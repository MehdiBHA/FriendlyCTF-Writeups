# Corrupt

![2020-12-03 11_39_57-FriendlyCTF](https://user-images.githubusercontent.com/62826765/100998963-791ae080-355c-11eb-95c9-22d920977abc.png)

Using _file_ we make sure that we are dealing with a PNG file.



By looking at the hexadecimal dump of the file, we see that the file header has been modified :



What a **File Header** means ? The File Header is a short sequence of bytes placed at the beginning of the file and used to identify its Format. See [List of file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)

For PNG files, the first 8 bytes always contain the following hexadecimal values : ```89 50 4E 47 0D 0A 1A 0A```


