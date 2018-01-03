
## Overview
This is an IIIF server in flask using iiif.py. This was cribbed from the iiif example and tweaked to allow for caching and hardwired to .tifs. 

Later I plan to move to port this to chalice to see how it will run on a Lambda.

## To try it it out


```
virtualenv flaskiiif
$cd flaskiiif
$source bin/activate
$git clone https://github.com/davidschober/flaskiiif
$pip install -r flaskiiif/requirements.txt
$python flaskiiif/app.py
```

put some images in your images folder

http://localhost:5000/test/IMAGEID


## TODO

* Port it to chalice
* Add logging

