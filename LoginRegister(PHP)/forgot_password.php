<?php
// Dummy forgot password handler for now (extend with real email reset flow)
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];
    $msg = "If your email is registered, you'll receive reset instructions soon.";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forgot Password</title>
</head>
<body>

    <?php include('navbar.php'); ?>

    <div class="container">
        <h2>Forgot Password</h2>
        <?php if (!empty($msg)) echo "<p style='color:green;'>$msg</p>"; ?>
        <form method="post">
            <input type="email" name="email" placeholder="Enter your email" required>
            <input type="submit" value="Reset Password">
        </form>
    </div>

    <style>
        <?php include 'styles.css'; ?>
    </style>

</body>
</html>
