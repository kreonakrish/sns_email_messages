import boto3
from jinja2 import Template

# Create an SNS client
sns_client = boto3.client('sns')

# Create a new SNS topic
response = sns_client.create_topic(Name='MyTopic')
topic_arn = response['TopicArn']

# Subscribe an email endpoint to the topic
sns_client.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='email@example.com'
)

# Read the email template
with open('email_template.html', 'r') as file:
    template_content = file.read()

# Sample data to populate the template
summary = "This is a summary of the data presented in the table below. The table contains sample data with 6 columns and 10 rows."
table_data = [
    ['Data 1', 'Data 2', 'Data 3', 'Data 4', 'Data 5', 'Data 6'],
    ['Data 7', 'Data 8', 'Data 9', 'Data 10', 'Data 11', 'Data 12'],
    ['Data 13', 'Data 14', 'Data 15', 'Data 16', 'Data 17', 'Data 18'],
    ['Data 19', 'Data 20', 'Data 21', 'Data 22', 'Data 23', 'Data 24'],
    ['Data 25', 'Data 26', 'Data 27', 'Data 28', 'Data 29', 'Data 30'],
    ['Data 31', 'Data 32', 'Data 33', 'Data 34', 'Data 35', 'Data 36'],
    ['Data 37', 'Data 38', 'Data 39', 'Data 40', 'Data 41', 'Data 42'],
    ['Data 43', 'Data 44', 'Data 45', 'Data 46', 'Data 47', 'Data 48'],
    ['Data 49', 'Data 50', 'Data 51', 'Data 52', 'Data 53', 'Data 54'],
    ['Data 55', 'Data 56', 'Data 57', 'Data 58', 'Data 59', 'Data 60']
]

# Create a Jinja2 template from the content
template = Template(template_content)

# Render the template with data
message_body = template.render(summary=summary, table_data=table_data)

# Publish the message to the topic
response = sns_client.publish(
    TopicArn=topic_arn,
    Subject='Sample Data Email',
    Message=message_body,
    MessageStructure='raw'
)

print("Email sent! Message ID:", response['MessageId'])
