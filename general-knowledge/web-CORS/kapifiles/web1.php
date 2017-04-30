<!DOCTYPE html>
<html>
	<title>web1</title>
<body>
<?php
error_reporting (1);

header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");
header('X-Frame-Options: DENY');

session_start(); 
$username = $password = $userError = $passError = '';

if(isset($_POST['sub'])){
  $username = $_POST['username']; $password = $_POST['password'];
  if($username === 'admin' && $password === 'password'){
    $_SESSION['login'] = true; 
  }
  if($username !== 'admin')$userError = 'Invalid Username';
  if($password !== 'password')$passError = 'Invalid Password';
}

if (isset($_POST['Logout'])) {
	$_SESSION['login'] = false;
	session_destroy();
	sleep(1);
	header('web1.php');

}

if(isset($_SESSION['login']) && $_SESSION['login'] == true){
	    echo "<h1>Hi Admin</h1>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod?
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, ?
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.?
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu ?
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in?
culpa qui officia deserunt mollit anim id est laborum.</p> 
<form name='input' action='' method='post'>
    <input type='submit' value='Logout' name='Logout' />
</form>";
} else {
	echo "<form name='input' action='' method='post'>
    <label for='username'></label><input type='text' value='' id='username' name='username' />

    <label for='password'></label><input type='password' value='' id='password' name='password' />

    <input type='submit' value='Login' name='sub' />
  </form>";
}


function cors($enable=false) {
	if ($enable == true) {
		if (isset($_SERVER['HTTP_ORIGIN'])) {
		    header("Access-Control-Allow-Origin: {$_SERVER['HTTP_ORIGIN']}"); // allow all origin
		    // header("Access-Control-Allow-Origin: kapi.net.only"); // allow only origin is kapi.net.only
		    // header('Access-Control-Allow-Credentials: false'); // do not allow access to credential e.g.cookie
		    header('Access-Control-Allow-Credentials: true'); // allow access to credential e.g. cookie
		    header('Access-Control-Max-Age: 1'); // secs
		}

		if ($_SERVER['REQUEST_METHOD'] == 'OPTIONS') {
		    if (isset($_SERVER['HTTP_ACCESS_CONTROL_REQUEST_METHOD']))
		        header("Access-Control-Allow-Methods: GET, POST, OPTIONS"); 

		    if (isset($_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']))
		        header("Access-Control-Allow-Headers: {$_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']}");

		    exit(0);
		}
	}
}
cors(true);
?>
</div>
</body>
</html> 