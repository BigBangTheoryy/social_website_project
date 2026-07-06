(function()){
    if (!window.bookmarklet){
        bookmarklet_js = document.body.appendChild(document.createElement("script"));
        bookmarklet_js.src = "https://bigbyte.pythonanywhere.com/static/js/bookmarklet.js?r="+Math.floor(Math.random()*9999999999999999); #This line tells the browser "Download and execute bookmarklet.js from my server, and append a random query parameter so the browser always fetches the newest version instead of using a cached copy.
        window.bookmarklet = true;
    }
    else{
        bookmarkletLaunch();
    }
})();