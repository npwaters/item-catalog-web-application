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
});