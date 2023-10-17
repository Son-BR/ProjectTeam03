function search(event) {
    event.preventDefault();
    var query = document.getElementById("search-input").value.trim();
    if (query.length == 0) {
        return false;
    }
    var url = "https://www.googleapis.com/customsearch/v1?key=YOUR_API_KEY&cx=YOUR_CX&q=" + encodeURIComponent(query);
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.items && response.items.length > 0) {
                document.getElementById("search-summary").innerHTML = "Showing " + response.items.length + " results for \"" + query + "\"";
                document.getElementById("search-results").style.display = "block";
                var list = document.getElementById("search-list");
                list.innerHTML = "";
                for (var i = 0; i < response.items.length; i++) {
                    var item = response.items[i];
                    var li = document.createElement("li");
                    li.innerHTML = "<a href=\"" + item.link + "\">" + item.title + "</a><p>" + item.snippet + "</p>";
                    list.appendChild(li);
                }
            }
        }
    };
    xhr.send();
}
