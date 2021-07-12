$(document).ready(function() {
    loadTopics();
});

function  loadTopics() {
    $('.topics').empty();
    $.getJSON(
        "/topic",
        function (topics) {
            for (let topic of topics) {
                $('.topics').append(
                    "<a class=\"card w-100 mt-2 py-2 px-3\" href=\"/topic?id=" + topic.id + "\">" +
                    "<h5 class=\"card-title\">" + topic.title + "</h5>" +
                    "</a>"
                );
            }
        }
    );

}

function addTopic() {
    $.ajax({
        type : "POST",
        url : "/topic",
        data: {
            title : $('#title').val(),
            text: $('#text').val(),
        },
        success: function() {
            loadTopics();
        },
        error: function() {
            alert("An error has occured while trying to add your topic.");
        }
    });
}