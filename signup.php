<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $username = $_POST['username'];
        $password = $_POST['password'];

        // You would typically insert this data into a database, but for simplicity, we'll just print it here
        echo "Username: $username<br>";
        echo "Password: $password<br>";
    }
?>