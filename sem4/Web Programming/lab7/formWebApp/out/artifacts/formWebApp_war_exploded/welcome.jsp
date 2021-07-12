<%@ page import="forumWebApp.domain.User" %>
<%
    if (session.getAttribute("user") == null) {
        return;
    }
%>
<html>
<head>
    <title>Welcome</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <script src="js/jquery-3.5.0.min.js" type="text/javascript"></script>
    <script src="js/ajax-utils/topics.js" charset="utf-8"></script>
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="/">ForumApp</a>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
            <li class="nav-item active">
                <a class="nav-link" href="/welcome.jsp">Home</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="/topics.jsp">Topics</a>
            </li>
        </ul>
    </div>
</nav>

<div class="container mt-5">

    <h1>
    <%
        User user = (User) session.getAttribute("user");
        out.print("Welcome, " + user.getUsername());
    %>
    </h1>

</div>

</body>
</html>

