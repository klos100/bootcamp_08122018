import sys

f_name = None

if len(sys.argv) > 1:
    f_name = sys.argv[1]


def prepare_line(text):
    text = text.strip().lower()
    return text

if f_name:
    list_email = [] #mozna dac zbior to bedzie z glowy usuwanie duplikatow
    with open(f_name) as f:
        for line in f:
            if line.count("@") == 1:
                email = prepare_line(line)
                if email not in list_email:
                    list_email.append(email)

    list_email.sort()
    with open("cleaned_emails.txt",'w') as f:
        for email in list_email:
            f.write(f"{email} \n")



print(list_email)