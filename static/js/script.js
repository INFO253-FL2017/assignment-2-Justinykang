var f = document.getElementById("contact");
f.addEventListener("submit", function(event) {
    var n = f.elements.namedItem("name").value;
    var s = f.elements.namedItem("subject").value;
    var m = f.elements.namedItem("message").value;

    var e = document.getElementById("error");
    e.innerHTML = ""

    if (n == "") {
        e.innerHTML += 'Name<br>';
    }
    if (s == "") {
        e.innerHTML += 'Subject<br>';
    }
    if (m == "") {
        e.innerHTML += 'Message<br>';
    }

    if (e.innerHTML != "") {
        e.innerHTML = 'The following fields are missing:<br>' + e.innerHTML;
    } else {
        var mailgun = require("mailgun-js");
        var api_key = os.environ['INFO253_MAILGUN_PASSWORD'];
        var mailgun = require('mailgun-js')({apiKey: INFO253_MAILGUN_PASSWORD, domain: DOMAIN});

        var data = {
          from: os.environ['INFO253_MAILGUN_FROM_EMAIL'],
          to: os.environ['INFO253_MAILGUN_TO_EMAIL'],
          subject: s,
          text: m
        };

        mailgun.messages().send(data, function (error, body) {
          console.log(body);
        });
        // e.innerHTML = 'Hi ' + n + ', your message has been sent!';
    }
    event.preventDefault();
});





