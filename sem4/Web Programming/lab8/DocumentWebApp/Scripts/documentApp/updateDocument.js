$(document).ready(function () {
    $("#updateDocumentButton").click(function () {


        $.ajax({
            type: "POST",
            url: "/Main/Update",
            data: {
                id: $('#id').val(),
                title: $('#title').val(),
                author: $('#author').val(),
                pages: $('#pages').val(),
                format: $('#format').val(),
                type: $('#type').val()
            },
            success: function () {
                reload();
               
            },
            error: function () {
                alert("An error has occured while trying to update your document.");
            }
        });
        reload();
    });
});
