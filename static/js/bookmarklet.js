const siteUrl   = "https://bigbyte.pythonanywhere.com/";
const styeleUrl = siteUrl + "/home/BigByte/bookmarks/static";
const minWidth  = 250;
const minHeight = 250;

//Load CSS

var head  = document.getElementsByTagName("head")[0];
var link  = document.createElement("link");
link.rel  = "stylesheet";
link.type = "text/css";
link.href = styleUrl + "?r" + Math.floor(Math.random()*9999999999999999);
head.appendChild(link);

//Load HTML
var body = document.getElementsByTagName("body")[0];

boxHtml = `
    <div id="bookmarklet">
    <a href="#" id="close">&times;</a>
    <h1>Select an Image to bookmark:</h1>
    <div class="images"></div>
    </div>`;

body.innerHTML += boxHtml;
