function refreshDocuments() {

	$('.table').empty();
	$('.table').html("<tr><th>Title</th><th>Author</th><th>No.Pages</th><th>Type</th><th>Format</th><th>Update</th><th>Delete</th></tr>");

	$.getJSON(
		"/Main/GetDocuments",
		function (documents) {
			for (let doc of documents) {
				$('.table tr:last').after("<tr><td>" +
					doc.Title + "</td><td>" +
					doc.Author + "</td><td>" +
					doc.NumberOfPages + "</td><td>" +
					doc.Type + "</td><td>" +
					doc.Format + "</td>" +
					'<td><button type="button" onClick="window.location.href=\'/Main/UpdateDocument?id=' + doc.Id + '\'">Update</button></td>' +
					'<td><button type="button" onClick="deleteDocument(\'' + doc.Id + '\')">Delete</button></td></tr>'
				);
			}
		}
	);

}




function deleteDocument(id) {
	if (confirm("Are you sure you want to delete the document?")) {
		$.ajax({
			type: "POST",
			url: "/Main/Delete",
			data: {
				id: id,
			},
			success: function () {
			
					alert("Document was deleted successfully!");
					refreshDocuments();

			},
			error: function () {
				alert("An error has occured while trying to delete your document.");
			}
		});
	}

}



$(document).ready(function () {

	$.getJSON(
		"/Main/GetDocuments",
		function (documents) {
			for (let doc of documents) {
				$('.table tr:last').after("<tr><td>" +
					doc.Title + "</td><td>" +
					doc.Author + "</td><td>" +
					doc.NumberOfPages + "</td><td>" +
					doc.Type + "</td><td>" +
					doc.Format + "</td>" +
					'<td><button type="button" onClick="window.location.href=\'/Main/UpdateDocument?id=' + doc.Id + '\'">Update</button></td>' +
					'<td><button type="button" onClick="deleteDocument(\'' + doc.Id + '\')">Delete</button></td></tr>'
				);
			}
		}
	);

});
