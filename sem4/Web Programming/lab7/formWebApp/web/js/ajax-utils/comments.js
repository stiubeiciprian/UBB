$(document).ready(function() {
    loadComments()
});

function loadComments() {

    $('.comments').empty();

    let searchParams = new URLSearchParams(window.location.search);
    $.ajax({
        type: 'GET',
        url: '/comment',
        data: {
            topicId: searchParams.get('id')
        },
        success: function(data, textStatus, request){

            for (let comment of data) {

                let deleteButton = "";
                if (request.getResponseHeader('user') == comment.userId) {
                    deleteButton = "<button class='btn btn-danger ml-auto' onclick='deleteComment(" + comment.id + ")'>Delete</button>";
                }

                $('.comments').append(
                    "    <div class=\"card mt-4\">\n" +
                    "        <div class=\"card-header d-flex\">\n" +
                    "            <h6 class=\"card-title\">" + comment.author +"</h6>\n" +
                                 deleteButton +
                    "        </div>\n" +
                    "        <div class=\"card-body\">\n" +
                    "            <p class=\"card-text\">" + comment.text + "</p>\n" +
                    "        </div>\n" +
                    "    </div>"
                );
            }
        },
        error: function () {
            alert("An error has occured while fetching comments!");
        }
    });
}

function deleteComment(id) {
    if(confirm("Are you sure you want to delete your comment?")) {
        $.ajax({
            type: 'DELETE',
            url: '/comment?id=' + id,
            success: function (data, textStatus, request) {
                loadComments();
            },
            error: function () {
                alert("An error has occured while deleting your comment!");
            }
        });
    }
}

function addComment() {
    let searchParams = new URLSearchParams(window.location.search);
    $.ajax({
        type : "POST",
        url : "/comment",
        data: {
            topicId : searchParams.get('id'),
            text: $('#text').val(),
        },
        success: function() {
            loadComments();
        },
        error: function() {
            alert("An error has occured while trying to add your comment.");
        }
    });
}