import json
import requests
from .models import CountIssue, CountCommit, CountRepository


class CrawlingIssue:
    URL = 'https://api.github.com/search/issues?q=language:'
    
    def __init__(self):
        pass


    
    def CrawlingJavascript(self):
        params = 'javascript'

        response = requests.get(self.URL+params)
        issue = response.json().get('total_count')
        
        javascript = CountIssue(javascript=issue)
        javascript.save()




    #URL = 'https://api.github.com/search/issues?q=language:'
    #params = 'python'

    #response = requests.get(URL+params)
    #issues = response.json().get('total_count')

    #result = {}
    #language = ['JavaScript', 'Java', 'Python', 'C', 'C#', 'C++', 'Go', 'Ruby', 'TypeScript', 'PHP', 'Scala', 'Rust', 'Kotlin', 'Swift', 'Shell']

    #for lang in language:
    #    response = requests.get(URL+lang)
    #    issues = response.json().get('total_count')
    #    result[lang] = issues
        # print(result[lang])

    # print(result)    

