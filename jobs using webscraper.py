import requests
from bs4 import BeautifulSoup

url = input("Please enter the link of your Microsoft Forms: ")
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    job_boxes = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, head in enumerate(job_boxes):
        date_element = head.find('span', class_='sim-posted').span
        if date_element is not None:
            date = date_element.text
            cname = head.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = head.find('span', class_='srp-skills').text.replace(' ', '')
            more_element = head.find('header', class_='clearfix').h2.a
            more = more_element['href'] if more_element is not None else 'N/A'

            if "few" in date:
                file_name = f'pk.{index}.txt'
                with open(file_name, 'w') as f:
                    f.write(f'Company name: {cname.strip()}\n')
                    f.write(f'Required skills: {skills.strip()}\n')
                    f.write(f'More info: {more}\n')
                print(f'File created: {file_name}')
            else:
                print(f"Skipped file creation for index {index} - 'Few' not in date")
        else:
            print(f"Skipped file creation for index {index} - date_element is None")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

print("Thank-You. Have a Good Day")
