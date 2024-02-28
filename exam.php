<?php
$conn = new mysqli("localhost", "root", "");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "Connected successfully";

mysqli_select_db($conn, "hzdata");
$q = "CREATE TABLE  person
(
    FirstName varchar(15),
    LastName varchar(15),
    Pass varchar(15)
)";
$mq = mysqli_query($conn, $q);
if (!$mq) {
    echo "could not create table";
} else {
    echo "Table created successfully";
}
?>