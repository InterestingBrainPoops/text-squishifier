# text-squishifier
My file compressor.
## How does it work?  
It uses arithemtic coding, and the symbols it uses are the bits of the message. 
As of now all it does is compress strings into a json format.  
resources.txt is a great place to find all the stuff you would need. 
  
## Can I use it in a project?
Yes. For python, all you need to do is add the squish_py folder to your project. 
and then 
```
from squish_py import encode, decode
```
decode takes the compressed string, and encode takes a string.
Once i get this working with files, then ill update this.