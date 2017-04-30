# Cross-origin resource sharing (CORS)
## Origin determination rules
The origin is the triple {protocol, host, port}. Two resources are considered to be of the same origin if and only if all these values are exactly the same ([see](https://en.wikipedia.org/wiki/Same-origin_policy#Origin_determination_rules)).

## Same origin policy
For security reasons, browsers restrict cross-origin HTTP requests initiated from within scripts. For example, [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) and [Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) follow the same-origin policy. So, a web application using XMLHttpRequest or Fetch could only make HTTP requests to its own domain. To improve web applications, developers asked browser vendors to allow cross-domain requests.

## Cross-origin resource sharing
is a mechanism that allows restricted resources (e.g. fonts) on a web page to be requested from another domain outside the domain from which the first resource was served. A web page may freely embed cross-origin images, stylesheets, scripts, iframes, and videos. Certain "cross-domain" requests, notably Ajax requests, however are forbidden by default by the same-origin security policy.

## Example #1
1. Alice access to a web page a.html in somedomain.a
2. Alice access to a web page b.html in somedomain.b. The page b.html contains JavaScript which try to pull some resources from a.html (the resource might be text, image, or any objects). This is generally prohibit by the browser (regardless of whether a.html was set HTTP header X-Fram-Option or not).
3. a.html was enabled CORS for any domain. So b.html could now pull some resources from a.html(regardless of whether a.html was set HTTP header X-Fram-Option or not) 
4. Moreover if a.html allow a web page from other domains to pull resources with credential by setting HTTP header "Access-Control-Allow-Credentials" to "true" the other web page from other domains will be able to make a request to a.html with credential e.g. cookie stored in user's browser.

## Real world example
The following steps demonstrate how CORS works.
1. Client access web1.php on originA and authenticate to the web
![step1](kapifiles/step1.png)
2. originA accept the authentication of the client and create session cookie
![step2](kapifiles/step2.png)
3. Client access malicious web2.php on originB
![step3](kapifiles/step3.png)
This is the Javascript code in web2.php
```javascript
function createCORSRequest(method, url) {
  var xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {
    // Chrome/Firefox/Opera/Safari.
    xhr.open(method, url, true);
    xhr.withCredentials = true;
    xhr.setRequestHeader("kapiheader","kapiheadervalue")
  } else if (typeof XDomainRequest != "undefined") {
    // for IE.
    xhr = new XDomainRequest();
    xhr.open(method, url);
  } else {
    xhr = null;
  }
  return xhr;
}

function makeCorsRequest(url,objID) {
  var obj = document.getElementById(objID);
  var xhr = createCORSRequest('GET', url);
  if (!xhr) {
    alert('CORS not supported');
    return;
  }

  xhr.onload = function() {
    var text = xhr.responseText;
    obj.innerHTML = obj.innerHTML + text;
  };

  xhr.onerror = function() {
    alert('Error');
  };

  xhr.send();
}
```
4. Client clicks the button "Click me to retrieve content from web1" on the web2.php which will send HTTP GET request to web1.php by follow the Cross-origin resource sharing protocols
Script on web2.php try to send HTTP GET to web1.php but the browser knows that web2.php try to do somthing cross the origin then the browser performs [preflight request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Preflighted_requests) by sending HTTP OPTIONS to web1.php like this
```
OPTIONS /CORS/web1.php HTTP/1.1
Host: 127.0.0.1:88
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Access-Control-Request-Method: GET
Access-Control-Request-Headers: kapiheader
Origin: http://localhost:90
Connection: close
```
web1.php answer by setting response headers like this
```
HTTP/1.1 200 OK
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Access-Control-Allow-Origin: http://localhost:90
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 1
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Allow-Headers: kapiheader
... snipped ...
```
From the response web1.php allow HTTP GET, POST, and OPTIONS and allow all custom HTTP headers including allow request with credential. Allowing request with credential means web2.php could request to web1.php by using session cookie authenticated by user previously in the 1st step. Script on web2.php now can perform HTTP request to web1.php and attach authenticated session in the request.
```
GET /CORS/web1.php HTTP/1.1
Host: 127.0.0.1:88
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
kapiheader: kapiheadervalue
Referer: http://localhost:90/CORS/web2.php
Origin: http://localhost:90
Cookie: PHPSESSID=04a5ovi6djtd5kc42coj6c79s2
Connection: close
```

response from web1.php
```
HTTP/1.1 200 OK
Date: Sun, 30 Apr 2017 05:15:06 GMT
Server: Apache/2.4.23 (Win32) OpenSSL/1.0.2h PHP/5.6.28
X-Powered-By: PHP/5.6.28
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
X-Frame-Options: DENY
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Access-Control-Allow-Origin: http://localhost:90
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 1
Content-Length: 677
Connection: close
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html>
	<title>web1</title>
<body>
<h1>Hi Admin</h1>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod?
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, ?
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.?
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu ?
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in?
culpa qui officia deserunt mollit anim id est laborum.</p> 
<form name='input' action='' method='post'>
    <input type='submit' value='Logout' name='Logout' />
</form></div>
</body>
</html> 
```

The result. ![step4](kapifiles/step4.png)

# Ref:
* https://en.wikipedia.org/wiki/Cross-origin_resource_sharing
* https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS
* https://en.wikipedia.org/wiki/Same-origin_policy
* https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Preflighted_requests