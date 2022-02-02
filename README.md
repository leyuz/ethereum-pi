# ethereum-pi

Instructions to user:
1. Prepare Raspberry PI 4 with fresh Raspbian OS Legacy (Not tested on Bullseye, which you may need to run `sudo raspi-config` to enable legacy camera support)
2. Install Docker and docker-compose
3. Enable container's access to Pi Camera
    - One time setup `echo "SUBSYSTEM==\"vchiq\",MODE=\"0666\"" | sudo tee /etc/udev/rules.d/99-camera.rules`
    - Every reboot `xhost +local:`
4. Clone this repo
5. `cd ethereum-pi`

6. run 'docker-compose run backend'
7. It will pull the image and run.
8. Depends on where you issued the `docker-compose`, i.e. from SSH terminal, or a terminal in Desktop mode, a full graphical preivew or text preview (quite laggy) may appear.
9. Aim the Pi Camera at a QR code, representing a valid Etherum (ERC20) address
10. Adjust the Camera and QR code, the QR code will be captured and decoded.
11. Follow the instruction on the screen, but the gist is:
    - it will scan a ETH wallet's QR code
    - it will ask you whether you want to send some ether to that wallet (from testnet, not real ones ^_^)
    - the amount is based on current UTC time (not Singapore time)
    - e.g. if time is 16:29, then the amount is 0.00001629
    - in the output of the app, it will generate a link for you to check the status of the transaction online.


Below is a sample of the text mode preview
```
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BBB%WB@@&bpdddbkkhaoo*##MW&%@$$$$$$$$$$$$$$$
@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$@@@@@@@@@@@@@@@@@@@@@BBBBBBBBBBBB8#pCn(_lIUB@&mOmwwwqpdbkkhao#M&8B@$$$$$$$$$$$$$$
@@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$@@@@@@@@@@BBBBBBBBBBBBBB%%WhmUr)+I"",i](I`~a@@a0QOZZmwqqpqpba*M&8@$$$$$$$$$$$$$$$
@@@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$@@@@@@BBBBBBBBB%%%%8WhOXf[>,``"i]/cUCYunor^^j%@B*ZQQOZZZmwqpbh*W%@$$$$$$$$$$$$$$$$
@@@@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$@@@@@BB%%%%%8*dQv/[i,`.'iI.:JwXr)_I"";``xai'!bB@B8#hpwZZmqba#8B$$$$$$$$$$$$$$$$$$$
BB@@@$$$$$$$$$$$$$$$$$$$$$$$$$$$@@@@@@@@B%%8oqCn)_I^'."i`....`uO:'jkl.;n0bW&)'ldv^`fB@@B@$$$BBB@@$$$$$$$$$$$$$$$$$$$$$$$
%BBB@@@$$$$$$$$$$$$$$$$$$$$$@@@@@@@B8*qJn)+;^'':;.....!\!t-'..lk/';wn`"0B@@@d;`\a>'!h@@@@$$$@@@@@@$$$$$$$$$$$$$$$$$$$$$$
&88%BBB@@$$$$$$$$$$$$$@@@@@@%Mb0zt}<,`^:<:....']?if,.`<,':"'."{_;'']a<'-dOzf},'ldz"^t%@@@@$B%%%BBB@@@$$$$$$$$$$$$$$$$$$$
*#W&&W&%B@$$$$$$$$@@@8#pCn(_I"^"!-,..^z8%qvf^.,~`'"`^i(!.`nu``~;tu``JC"'";+(xXUUz\,'Iw@@B@@%&&88%BBB@@@@$$$$$$$$$$$$$$$$
pba*Moa#&88@$$$#ZYj1+I""i?{,^/a&B%z""z&%q?I"';-}^.;ZMM]'.'<x,...ih?'>aQzcx(-l,"''_("`{8@@@8##MW&88%%BBB@@@$$$$$$$$$$$$$$
qqph#8#*W&&&@$@QI^ifYv;;0B%x^Icck%W{^-MB8OO-'-k~.'^}rzaCYOb)|nr,,Yp:.^^,>[tuzXrl}-I`',O@@Boka*#MWW&&88%%BB@$$$$$$$$$$$$$
88&8%@@%888&B$$Bc,:~_L)^I}{d(`.'_o(,?uX&BBau"'\bUYw0)x*X,idBBJ":ZBBx`,xXom~,`'l?-!(/^`1%@8qqbho*###MMWW&&8B@$$$$$$$$$$$$
8%%BB@@$@BBBB$@@%t":cx_~`'`?b\{tvqmQq\joBk|I-`^z(;{M%M)`lfja),`._M\I+rl]]>~x;'[#CQ)!I':Z@%qZqdbhaoo***##MW8B@$$$$$$$$$$$
88%%%%BB@@@@@@@@BW{"~vf?"`'`{*t>:"^^c%8aq{![-^'`'I{\k_"^..."^[(!(<:fL_]-I\v^.>(!;nUj-''[&@MmZmqpdbkhaaoo*#W8B$$$$$$$$$$$
8%%%%%%%%B@$$$$@@@*]":\zv!`,(bZI^(-':Lc^..!q['!0!..'``}-''[}'.~v8kddnjo0uYcl[]I^,,.^t{'"Y@@WpZZmwqpddbkha*M8@$$$$$$$$$$$
88%%BB%B%%%B@@$$@@@a~"{d<`'"x%%C<?(xUdLI..'-w~>[i'`)[''?zO('..+oa%0(`'1J;!](<:{cmp:`xol'<#@@BMhqwwwqpdkhoM%@$$$$$$$$$$$$
W&88%%%%%%%8%%B$$@@BZI"jOI'',CMJnbzl[h(]I'~cq&8ZuvO)'..>qpa((rul:|+...`:<(]i;t+'lawzJC-'^X@$@@@@8W##M&8B@$$$$$$$$$$$$$$$
WW&&8%%%%%8888%B@$@@BJ;,1<{f"If!{[:~bQ\vbX}`"[[w\`~bujvL-?wd~!Z&&t''`+aL}l/;.^?|uaW]<](I'<#$$@@$$$$$$$$$$$$$$$$$$$$$$$$$
W&&88%%%%%%%8888%@@@@Bz:"(bZ+`''",^`|m;^j}'.."voa~'(ZlIUqdU;:fzMu!<nCMx<]z!;'`~~Uw*@@d<^.`xB$@$$$$$$$$$$$$$$$$$$$$$$$$$$
o#W&8%%%B%%%88888%@@@@%j"lni`''''_[``;";!`..:CM&xi.''"?,!,``..'I:-}I?]:'lcr(,..`"'l}/p<...ld@$@@$$@$$$$$$$$$$$$$$$$$$$$$
dh*W&8%%%%%%%%88&8%@@@@W{^``;f!I,...';0w{^..'1M8U,`'...'`';-'._[''>rM['!/I1fj,'?[~jXY>!^''`)%$$$$$$$$$$$$$$$$$$$$$$$$$$$
qdho#W8%%%%%B%%%888B@@@@o-`!z+"?>''':Q8*?'';+}+~mdj,..'~{'.+vL('..?aok-+1/i"";'`{);<*p\ij}`:m@$$$$$@$$$$$$$$$$$$$$$$$$$$
qqpba*MW8%%BBB%%%%%%%@$$Bd>^1CI''"nx{Xobpi`jO<:cWWunvjUU"..iLLbf\rz<+kh[]Q-l?}^')o<`\aunQn"'[%$$$$$@@@$$$$$$$$$$$$$$$$$$
ZmwqddhoM&%BBBB%%%888%@$$%0I">;`'';[)0>^|J"`"'.~#8Bk/l|#Qxum)1wOl!d%%zlltl_Oouxxxr+'`;:I<[]^,L@$$$$$@@@$$$$$$$$$$$$$$$$$
kmZZmda*MW&8%BBB%%%8888@$$8z;,rx"'``'^~,^crl>]i',,nc^">_vI_ZB#x^")fb):`''`XZI`l-)/fjrjf\{x#-`+#$$$$$@@@$$$$$$$$$$$$$$$$$
@WpZwqdka*MW&8%BBB%%88&%@$BMn,lQJxr("`>,^~o&&#dl..,OYU~..'!>X}ll'..^I)-_{`IXi'?W),"!_1fj:,Lm;"r@$$$$$@@@$$$$$$$$$$$$$$$$
@@%hmmqdbao#M&8%%%%%%88%@$@&*)^<w{+I'':\xb&W{lXX^..^:xd\}^`'`~}>+v"^CCjUO>!:'.^vQ",Z@$$@j^+*(^!k$$$$$@@@@$$$$$$$$$$$$$$$
@@@B#pwqpba*#M&8888%%%%%B$$BMd_"}aac;i|l`I!)u/(?!(i<{(JY!-d]`)hvrxi[O8{`'`nX,^'Ip)`-qZJu(,"xdl"/@$$$$$@@@$@$$$$$$$$$$$$$
@BB@B&dwwqbho#M&&88888%%B@$@8#m<"I:";1;`^:i?|1"IQ\)pwx]I](?l[bBn^''+QX1<{^`:<\:'1h+;i-)fxnncc~"lp$$$$$@@@@@$$$$$$$$$$$$$
B@@@BB8bmwpbha*#WW&&&8%BB@@@%&#Ql^l)/fjjf/1_-w(^)&@O;``l<`"^,(1~l(,'l["^,`i{}^''"jx\{->lI!+}\xX0#$$$$$$@@@@$$$$$$$$$$$$$
@BBBBB@BomZwpbao#MW&88BB@@$@B8M*c,IQf,,}fzQr"-d+"jCu>}>^^"{>`:\I```_)I^```<!^^,l~}\nUOd*8@$$$$$$$$$$$$$@@@@@$$$$$$$$$$$$
@@@BBBBBB#wQOqba*MM&8%BB@$$@@B8Mo\,_w],u8%%&{"\0;^`;r]:/Y,``itI```^,;I>]|xY0po&B$$$$$$$$$$$$$$$$$$$$$$$$@@@@@@@$$$$$$$$$
BBBBBBBBBB8k00wbo*#MW&8@@@@@@@B%Wh{:)w~Iff1?>!?dn,ljY(":+,,I<]|rzCQmhbpppUO@$$$$$$$$$$$$$$$$$$$$$$$$$$$$@@@@@@@$$$$$$$$$
BBBBBBBBBBB%aO0wbho#W%@@@@@@@@@B%&h-:jZtjnnxr/{+l:l+}/uJmkbdqQZJurunwZwqpoM$$$$$$$$$$$$$$$@@@@@@Bmujrw@$$@@@@@@@$$$$$$$$
BBBBBBBBBBBBB8WMW8%@@@@@@@@@@@@@BB8wi;+<>~[(rzLqaM%@@@@@@@pLOqhoW&%@@$$$$$$$$$$@@@@@@@BB%8*hhdqUq_]u_1W$$@@@@@@@@@$$$$$$
BBBBBBBBBBBBBBB$@@@@@@@@@@@@@@@@BBB8dZd*&BB@@@@B@@@@@@@@@@$$$$$$$$$@@@@@@@@BBB%8&&WW#***#M0mwmaa%MwZd8$$$$@@@@@@@@@$@$$$
BBBBBBBBBBBBBBBB@@@@@@@$$$$$$@B@@BBB%88BB@@@BBBBB@@@@@@@@@@@@@B@@@BBB@@@BBBB@@%MMW&8%B@@$$$$$$$$$$$$$$$$$$@@@@@@@@@@@@$@
BBBBBBBBBBBBBBBBBBBBB@@@@@@@@BBBB%BBBBBBBBBBBBBB%%%8%%%%BBBBBBB@@@@@@@@@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$@@@@@@@@@@@@@
```