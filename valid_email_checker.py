import csv
from validate_email import validate_email
from ipaddress import IPv4Address, IPv6Address

def check_validity(email):
    is_valid = validate_email(
        email_address=email,
        check_format=True,
        check_blacklist=True,
        check_dns=True,
        dns_timeout=10,
        check_smtp=True,
        smtp_timeout=10,
        smtp_helo_host='my.host.name',
        smtp_from_address='my@from.addr.ess',
        smtp_skip_tls=False,
        smtp_tls_context=None,
        smtp_debug=False,
        address_types=frozenset([IPv4Address, IPv6Address]))
    return is_valid


def check_email_valid():

    csv_file = input("Enter the path to the CSV file: ")

    valid_emails = []
    invalid_emails = []

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row      

        for row in reader:
            email = row[0]
            if check_validity(email):
                valid_emails.append(email)
            else:
                invalid_emails.append(email)
    # field names
    fields = ['Email', 'Validity']
    # name of csv file
    filename = "email_validity_test_result.csv"
    # writing to csv file 
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        for email in valid_emails:
            csvwriter.writerow([email, 'valid'])
        for email in invalid_emails:
            csvwriter.writerow([email, 'not valid'])

    print(f"process complete, csv file {filename} genarated")

if __name__ == "__main__":
    check_email_valid()