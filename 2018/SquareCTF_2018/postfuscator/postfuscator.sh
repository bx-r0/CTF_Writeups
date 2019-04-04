#!/bin/bash
echo "Enter key:"
read key
echo -ne "%!PS
/input 65 string def
/Courier
18 selectfont
currentfile input readline
%" > postfuscator.ps
echo $key | tr -Cd a-f0-9 >> postfuscator.ps
echo -ne "
pop
/input exch store
/encrypt_str {
  /buf1 65 string def
  /buf2 (4L0ksa1t) def
  /n 0 def
  {
    buf2 n 8 mod get
    xor
    /i exch def
    buf1 n i put
    /n n 1 add store
  } forall
  buf1 0 n getinterval
} def
/test_str {
  /buf_z (800C46E31190C06039198D86E38180DC64311C0D868361C0D47230880C8730F198D06B0F1AC52192188C121C381B8C07039940D86D04898E06638190DC693484C4E092A8B0CA452C9F4961F34958DC6A389A40A691E1A8C643368AC4269010>) def
  /buf 118 string def
  /fake_file buf_z /ASCIIHexDecode filter def
  /fake_file2 fake_file /LZWDecode filter def
  fake_file2 buf readstring
  pop
  pop
  /ok 0 def
  /n 0 def
  {
    /c exch (...) cvs def
    buf n c length getinterval
    c
    eq {/ok ok c length add store} if
    /n n c length add store
  } forall
  ok buf length eq
} def
input encrypt_str test_str
{100 420 moveto (yes, you got it! flag-" >> postfuscator.ps
echo ${key:2:20} | tr -Cd a-f0-9 >> postfuscator.ps
echo -ne ") show}
{230 420 moveto (Sorry, nope.) show}
ifelse
/m {
  1 dict begin
    /p2y exch def
    /p2x exch def
    /p1y exch def
    /p1x exch def
    p1y p2y add 2 div
    p1x p2x add 2 div
  end
} def
/b {
  1 dict begin
    /r exch def
    /p3y exch def
    /p3x exch def
    /p2y exch def
    /p2x exch def
    /p1y exch def
    /p1x exch def
    /p0y exch def
    /p0x exch def
    r 0 lt
    {
      newpath
      p0x p0y moveto
      p3x p3y lineto
      stroke
    }
    {
      /r r 1 sub store
      p0x p0y p1x p1y m /p4x exch def /p4y exch def
      p1x p1y p2x p2y m /p5x exch def /p5y exch def
      p2x p2y p3x p3y m /p6x exch def /p6y exch def
      p4x p4y p5x p5y m /p7x exch def /p7y exch def
      p5x p5y p6x p6y m /p8x exch def /p8y exch def
      p7x p7y p8x p8y m /p9x exch def /p9y exch def
      p0x p0y p4x p4y p7x p7y p9x p9y r b
      p9x p9y p8x p8y p6x p6y p3x p3y r b
    }
    ifelse
  end
} def
/sq {
  1 dict begin
    /s 3 def
    -70 -50 -70 -50 -70 50 -70 50 s b
    -70 50 -70 70 -70 70 -50 70 s b
    -50 70 -50 70 50 70 50 70 s b
    50 70 70 70 70 70 70 50 s b
    70 50 70 50 70 -50 70 -50 s b
    70 -50 70 -70 70 -70 50 -70 s b
    50 -70 50 -70 -50 -70 -50 -70 s b
    -50 -70 -70 -70 -70 -70 -70 -50 s b
  end
} def
300 200 translate
2 setlinewidth
20 {.99 .99 scale sq} repeat
.6 .6 scale
40 {.99 .99 scale sq} repeat
showpage" >> postfuscator.ps
open postfuscator.ps
