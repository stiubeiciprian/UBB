function filterDocuments(column) {
    var input, filter, table, tr, td, i;

    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    table = document.getElementById("documentTable");
    tr = table.getElementsByTagName("tr");


    for (i = 1; i < tr.length; i++) {
        tr[i].style.display = "none";

        td = tr[i].getElementsByTagName("td");
        cell = tr[i].getElementsByTagName("td")[column];
        if (cell) {
            if (cell.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            }
        }
    }
}

selectedIndex = 0;
colNames = {
    1: "Title",
    2: "Author",
    4: "Type",
    5: "Format"
};

$(document).ready(function () {
    $("#searchDocumentButton").click(function () {
        var lastUsedFilter = colNames[document.getElementsByTagName("option")[selectedIndex].value];
        $("b").html(lastUsedFilter);
        selectedIndex = document.getElementById("format").selectedIndex;
        filterDocuments(document.getElementsByTagName("option")[selectedIndex].value);
    });
});
