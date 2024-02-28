<?php
$conn = new mysqli("localhost", "root", "");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "Connected successfully";

mysqli_select_db($conn, "hzdata");

$q = "INSERT INTO person(FirstName, LastName, Pass)
VALUES ('$_POST[FirstName]', '$_POST[LastName]', '$_POST[Password]')";

$mq = mysqli_query($conn, $q);
?>