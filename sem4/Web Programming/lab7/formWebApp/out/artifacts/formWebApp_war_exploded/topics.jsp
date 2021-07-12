<%
    if (session.getAttribute("user") == null) {
        return;
    }
%>

<html>
<head>
    <title>Topics</title>
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

    <h1>Topics</h1>
    <hr>
    <div class="topics">
    </div>

    <h1 class="mt-5">Add new topic</h1>
    <hr>
    <div class="d-flex flex-column">
        <div class="form-group">
            <input type="text" class="form-control" id="title" placeholder="Topic title">
        </div>
        <div class="form-group">
            <textarea class="form-control" id="text" cols="30" rows="3" placeholder="Topic description..."></textarea>
        </div>
        <button class="btn btn-primary" onclick="addTopic()">Add Topic</button>
    </div>

</div>

</body>
</html>
