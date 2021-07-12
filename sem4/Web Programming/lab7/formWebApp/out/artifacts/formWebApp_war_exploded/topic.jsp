<%@ page import="forumWebApp.domain.Topic" %>

<%
     if (session.getAttribute("user") == null) {
         return;
     }

    Topic topic = (Topic) request.getAttribute("topic");
%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <html>
    <head>
        <title><% out.println(topic.getTitle()); %></title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
        <script src="js/jquery-3.5.0.min.js" type="text/javascript"></script>
        <script src="js/ajax-utils/comments.js" charset="utf-8"></script>
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
    <div class="card">
        <div class="card-header">
            <h4 class="card-title">Topic: <% out.println(topic.getTitle()); %></h4>
            <h6 class="card-subtitle">started by <% out.println(topic.getAuthor()); %></h6>
        </div>
        <div class="card-body">
            <p class="card-text"> <% out.println(topic.getText()); %></p>
        </div>
    </div>

    <div class="d-flex mt-5 flex-column">
        <div class="form-group">
            <textarea class="form-control" id="text" cols="30" rows="3" placeholder="Write your comment..."></textarea>
        </div>
        <button class="btn btn-primary" onclick="addComment()">Comment</button>
    </div>

    <div class="comments">
    </div>


</div>

</body>
</html>
</title>
</head>
<body>

</body>
</html>