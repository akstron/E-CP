import requests
from bs4 import BeautifulSoup

'''
    Find codeforces problem
'''
from ..Problem.problem import Problem, Test
# from requests.auth import HTTPProxyAuth
from requests.auth import HTTPDigestAuth, HTTPBasicAuth


proxies = {
    "http":"172.31.100.27:3128",
    "https":"172.31.100.27:3128"
}
auth = ("edcguest", "edcguest")

def get_problem(url):
    response = requests.get(url)
    # response = requests.get(url, proxies=proxies, auth=auth)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'lxml')
    problem = Problem(get_problem_name(soup), get_problem_tests(soup))
    return problem

def get_problem_name(soup: BeautifulSoup):
    name_tag = soup.find('div', class_='title')
    name = name_tag.text
    return name

def get_problem_tests(soup: BeautifulSoup):
    input_tags = soup.find_all('div', class_='input')
    output_tags = soup.find_all('div', class_='output')
    tests = []

    #CHECK if both lengths are same
    length = len(input_tags)

    for index in range(length):
        input = input_tags[index].find('pre').text.strip()
        output = output_tags[index].find('pre').text.strip()
        tests.append(Test(input, output))
    
    return tests