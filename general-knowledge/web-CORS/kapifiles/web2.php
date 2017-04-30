<!DOCTYPE html>
<html>
<head>
    <title>web2</title>
</head>
<body>
<script type="text/javascript">

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

</script>
<div align="center">
<h1>Sample</h1>
<div id="content1"></div>
<button onclick="makeCorsRequest('http://127.0.0.1:88/CORS/web1.php','content2')">Click me to retrieve content from web1</button>
<div id="content2"></div>
</div>
</body>
</html>