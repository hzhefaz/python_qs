<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $username = $_POST['username'];
        $password = $_POST['password'];

        // Here you would typically check the username and password against a database
        // For simplicity, let's assume the correct username is "admin" and the password is "password"
        if ($username === 'admin' && $password === 'password') {
            echo "Login successful!";
        } else {
            echo "Invalid username or password.";
        }
    }