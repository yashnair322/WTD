<?php
include 'config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = mysqli_real_escape_string($conn, $_POST['username']);
    $password = md5($_POST['password']);
    $email = mysqli_real_escape_string($conn, $_POST['email']);

    $query = "INSERT INTO users (username, password, email) VALUES ('$username', '$password', '$email')";
    if (mysqli_query($conn, $query)) {
        header('Location: login.php');
    } else {
        $error = "Username or Email already exists";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>

    <?php include('navbar.php'); ?>

    <div class="container">
        <h2>Register</h2>
        <?php if (!empty($error)) echo "<p style='color:red;'>$error</p>"; ?>
        <form method="post">
            Username: <input type="text" name="username" placeholder="Username" required><br><br>
            <p>Email: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="email" name="email" placeholder="Email" required><br><br></p>
            Password: <input type="password" name="password" placeholder="Password" required><br><br>
            <input type="submit" value="Register">
        </form>
    </div>

    <style>
        <?php include 'styles.css'; ?>
    </style>

</body>
</html>
