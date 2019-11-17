function start() {
  gapi.load('auth2', function() {
    auth2 = gapi.auth2.init({
      client_id: '718168208441-jg3grpu7dhho0hr8cu186orp542dcjj2.apps.googleusercontent.com',
      // Scopes to request in addition to 'profile' and 'email'
      //scope: 'additional_scope'
    });
  });
}

$(document).ready(function () {
    $('#signinButton').click(function () {
        auth2.grantOfflineAccess().then(signInCallback);
    });

    $('#signoutButton').click(function () {
        console.log("signing out user!")
        $.ajax({
            type: 'POST',
            url: '/google_logout',
            processData: false,
            contentType: 'application/octet-stream; charset=utf-8',
            success: function (result) {
                // Handle or verify the server response if necessary.
                if (result) {
                    $('#result').html('Logout Successful!</br>' + result);
                    // redirect to home page
                    setTimeout(function () {
                        window.location.pathname = "/";
                    }, 1000);
                } else {
                    $('#result').html('Failed to make a server-side call. Check your configuration and console.');
                }
            }
        });
    })
});