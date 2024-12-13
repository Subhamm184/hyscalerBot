from odoo import http
from odoo.http import request
import openai

openai.api_key = 'your_api_key'

class ChatbotController(http.Controller):

    @http.route('/chatbot/ask_questions', auth='public', methods=['POST'], type='json')
    def ask_questions(self, company, profession, skills):
        prompt = f"User selected {company}, profession is {profession}, and their skills are {skills}. Please ask 10 relevant questions."
        response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=prompt,
            max_tokens=150
        )
        return {'questions': response.choices[0].text.strip().split('\n')}
