function send_event(userdata, category, action, eventdata, pagedata) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == XMLHttpRequest.DONE ) {
           if(xmlhttp.status == 200){
               console.log(xmlhttp.responseText);
           }
        }
    }

    var event = {
      userdata: userdata, 
      category: category,
      action: action,
      timestamp: Date.now(),
      eventdata: eventdata,
      pagedata: pagedata,
      referer: document.referrer
    };
    console.log(event);

    xmlhttp.open("POST", "/event", true);
    xmlhttp.setRequestHeader("Content-type", "application/json");
    xmlhttp.send(JSON.stringify(event));
}
