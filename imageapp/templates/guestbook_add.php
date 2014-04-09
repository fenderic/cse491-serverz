{% extends "base.html" %}

{% block content %}
<?php
$host="mysql-user"; // Host name
$username="austine5"; // Mysql username
$password="A43567692"; // Mysql password
$db_name="austine5"; // Database name
$tbl_name="491guestbook"; // Table name

// Connect to server and select database.
mysql_connect("$host", "$username", "$password")or die("cannot connect server ");
mysql_select_db("$db_name")or die("cannot select DB");

$datetime=date("y-m-d h:i:s"); //date time

$sql="INSERT INTO $tbl_name(name, email, comment, datetime)VALUES('$name', '$email', '$comment', '$datetime')";
$result=mysql_query($sql);

//check if query successful
if($result){
  echo "Successful";
  echo "<BR>";

  // link to view guestbook page
  echo "<a href='guestbook_view'>View guestbook</a>";
} else {
  echo "ERROR";
}

mysql_close();
?>


<a href="/">Back to Home</a>
{% endblock %}