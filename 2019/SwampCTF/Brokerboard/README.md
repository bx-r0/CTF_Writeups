
# Brokerboard
![](./brief.png)

The important part of the brief is the mentioning of the ```https://localhost/key``` endpoint. This is where the flag will most likely be returned from.


The challenge provided a web interface that fetches links.

![](./images/website.png)

As you can see from the image the url ```http://www.google.com``` has been parsed successfully. However, any attempts with localhost as the main host causes this error to be returned:

```
Ruh roh, we don't allow you to fetch internal URLs!
```

The second most important part of the brief is the hint towards the use of ```parse_url``` in the system. This will be our vulnerable entry point.

The bug used was ![#73192](https://bugs.php.net/bug.php?id=73192) of the PHP bug page. This states that the host in incorrectly parsed when the use of ```#``` after the port number of the original domain.

The payload used is below:
```
http://example.com:80#@localhost/key
```

NOTE: even though the website states that ```?``` and ```//``` can work in place of the ```#```. These were unable to work in this context.

By placing the playload into the link fetcher it circumvents the initial check for ```localhost``` while ```parse_url``` takes ```localhost/key``` as the main url.

The flag is provided like so:

![](./images/website_flag.png)

```
FLAG: flag{y0u_cANn0t_TRU5t_php}
```