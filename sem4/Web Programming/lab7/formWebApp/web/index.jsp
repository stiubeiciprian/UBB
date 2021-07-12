<%--
  Created by IntelliJ IDEA.
  User: stiub
  Date: 19/05/2020
  Time: 17:32
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title>Home</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
  </head>
  <body>

  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="/">ForumApp</a>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/login.html">Log in</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/register.html">Register</a>
        </li>
      </ul>
    </div>
  </nav>


    <div class="card container mt-5">
      <div class="card-body">
        <h5 class="card-title">Welcome!</h5>
        <hr>
        <p class="card-text">Please log into your account or register if you dont have one.</p>
        <a href="/login.html" class="card-link">Log in</a>
        <a href="/register.html" class="card-link">Register</a>
      </div>
    </div>



  </body>
</html>
