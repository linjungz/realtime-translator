
console.log('Initialize Cognito')
$('#cognito_status').text("Waiting for Cognito...")

// Initialize the Amazon Cognito credentials provider
AWS.config.region = 'us-east-1'; // Region
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: 'us-east-1:7f216796-f5a2-4e0a-a9b3-8eea01acbe0b',
});

get_credential();

function get_credential() {
    AWS.config.credentials.get(function(err, cred) {
        if (!err) {
            console.log(AWS.config.credentials);
            console.log('retrieved identity: ' + AWS.config.credentials.identityId);
            console.log('retrieved identity: ' + AWS.config.credentials.accessKeyId);
            console.log('retrieved identity: ' + AWS.config.credentials.secretAccessKey);
            console.log('retrieved identity: ' + AWS.config.credentials.sessionToken);

            $('#access_id').val(AWS.config.credentials.accessKeyId)
            $('#secret_key').val(AWS.config.credentials.secretAccessKey)
            $('#session_token').val(AWS.config.credentials.sessionToken)

            $('#cognito_status').text("Ready")
            $('#transcribe_status').text("Ready")
            $('#translate_status').text("Ready")
            $('#polly_status').text("Ready")
        
        } else {
            self.logger.error('error retrieving identity:' + err);
            alert('error retrieving identity: ' + err);
            $('#cognito_status').text("Error. Please refresh the page to retry")

        }
    });
}

