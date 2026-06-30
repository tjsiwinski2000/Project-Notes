import json

def convert_c_to_f(temp):
    # convert celsius to fahrenheit
    converted_temp = int(temp) * 9/5 +32
    return round(converted_temp)

def convert_f_to_c(temp):
    # convert celsius to fahrenheit
    converted_temp = (int(temp) -32) * 5/9
    return round(converted_temp)

def lambda_handler(event, context):
    output = 99
    if event['operation'] == 'c2f':
        output = convert_c_to_f(int(event['temp']))
    if event['operation'] == 'f2c':
        output = convert_f_to_c(int(event['temp']))
    return {
        'statusCode': 200,
        'body': json.dumps(output)
    } 
