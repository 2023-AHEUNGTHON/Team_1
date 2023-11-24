from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def chatgpt_api(request):
    question = request.GET.get('user_input')

    # ChatGPT API 호출
    chatgpt_api_key = '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'
    api_url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {chatgpt_api_key}',
    }
    payload = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'},
                    {'role': 'user', 'content': question}],
    }
    response = requests.post(api_url, headers=headers, json=payload)

    # API 응답을 파싱하여 필요한 정보 추출
    result = response.json()
    assistant_response = result['choices'][0]['message']['content']
    print(assistant_response)

    data={
        'type' : 'FBV',
        'result' : assistant_response,
        }

    # 문자열로 응답 생성
    return Response(data)
