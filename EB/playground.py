import boto3
import json
import boto3
from botocore.exceptions import ClientError
import requests

email = 'lectus@aliquetsemut.com'
userInfo = requests.get('http://6156app-env.89pzhbvd2j.ca-central-1.elasticbeanstalk.com/api/user/' + email)
print(userInfo.json())
# client = boto3.client('sns')

# response = client.publish(
#     TopicArn='arn:aws:sns:ca-central-1:969112874411:E6156CustomerChange',
#     Subject='email',
#     Message='{"customers_email":"rkmcd93@gmail.com"}',
# )

# print(response)


SENDER = "COMS E6156 App <fakeemail@gmail.com>"
# RECIPIENT = "dff@cs.columbia.edu"
# CONFIGURATION_SET = "ConfigSet"
AWS_REGION = "us-east-1"
SUBJECT = "Email Verification Test"
BODY_TEXT = ("Amazon SES Test (Python)\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
             )

BODY_HTML = """<html>
<head></head>
<body>
  <h1>Amazon SES Test (SDK for Python)</h1>
  <p>This email was sent with
    <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
    <a href='https://aws.amazon.com/sdk-for-python/'>
      AWS SDK for Python (Boto)</a>.</p>
      <form action="http://google.com">
        <input type="submit" value="Go to Google" />
    </form>
    <p>A really cool verification link would look like:{}
</body>
</html>
            """

# The character encoding for the email.
CHARSET = "UTF-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses', region_name=AWS_REGION)


# Try to send the email.
def send_email(recipient):
    try:
        print("recipient = ", recipient)
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    recipient
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


def handle_sns_event():
    # sns_event = records[0]['Sns']
    # topic_arn = sns_event.get("TopicArn", None)
    # topic_subject = sns_event.get("Subject", None)
    # topic_msg = sns_event.get("Message", None)

    # if topic_msg:
    em = 'rkmcd93@gmail.com'
    send_email(em)

# handle_sns_event()