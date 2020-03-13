let searchBox = document.getElementById("searchBox"), searchButton = document.getElementById("getButton"),
    divElement = document.getElementById('removeElements'), h1 = document.getElementById('h1Class'),
    notLink = document.getElementById('notLink')
function createData() {
    searchButton.addEventListener("click", function () {
        if (!(searchBox.value == '') && searchBox.value.includes("http")) {
            eel.getLinkFromSite(searchBox.value)
            notLink.remove()
            //put the loader logo on the screen when the system is working
            divElement.innerHTML = "<div class='loader'></div>"
            updateMe(function (json) {
                // create a demo table to dispaly the data from the json
                document.getElementById('wrapper').style.display = 'flex'
                const [link, comments] = document.querySelectorAll('#wrapper div');
                link.innerHTML += `<p class="first"><strong>Links</strong></p>`
                comments.innerHTML += `<p class="first"><strong>Comments</strong></p>`
                Object.values(json).forEach((entry, index) => {
                    link.innerHTML += `<p>${(index + 1) + ') ' + entry['linkSite']}</p>`
                    comments.innerHTML += `<p>${(index + 1) + ') ' + String(entry['Comment']).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')}}</p>`
                })
                divElement.remove()

            })
            divElement.classList.toggle("newDisplay")
        }
        else {
            notLink.innerHTML = "<h3 class = 'notLink'>Insert a Link - Must include http://</h3>"
        }
    });
}
//function to call the json file and get the data from inside
function updateMe(callback) {
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', '../data.json', true);
    xobj.onreadystatechange = function () {
        if (xobj.readyState == 4 && xobj.status == "200") {
            callback(JSON.parse(xobj.responseText));
        }
    };
    xobj.send(null);
}
createData()