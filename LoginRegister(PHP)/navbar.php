<nav>
    <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="#">About us</a></li>
        <li><a href="#">Department</a></li>
        <li><a href="#">Contact us</a></li>
        <li id="myid"><a href="login.php">Login</a></li>
    </ul>
</nav>

<style>
    nav{
        background-color: black;
        border-radius: 30px;
    }
    nav li{
        list-style: none;
        float: left;
        margin: 13px 25px;
        color: white;
    }
    nav ul{
        overflow: auto;
    }
    nav li a{
        color: white;
        text-decoration: none;
        padding: 13px 25px;
    }
    nav li a:hover{
        background-color: aliceblue;
        color: black;
    }
    #myid{
        float: right;
    }
</style>
