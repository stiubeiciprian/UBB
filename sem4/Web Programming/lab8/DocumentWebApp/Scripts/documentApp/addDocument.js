$(document).ready(function () {
    $("#addDocumentButton").click(function () {
        $.ajax({
            type: "POST",
            url: "/Main/Add",
            data: {
                title: $('#title').val(),
                author: $('#author').val(),
                pages: $('#pages').val(),
                type: $('#type').val(),
                format: $('#format').val()
            },
            success: function () {
                reload();
            },
            error: function () {
                alert("An error has occured while trying to add your document.");
            }
        });
    });
});
