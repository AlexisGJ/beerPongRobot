import httplib2

resp, content = httplib2.Http().request("http://beerpongrobot.herokuapp.com/web/shoot.php")
