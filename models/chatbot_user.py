from odoo import models, fields

class ChatbotUser(models.Model):
    _name = 'chatbot.user'
    _description = 'Chatbot User Information'

    name = fields.Char('User Name')
    company = fields.Many2one('res.company', string='Company')
    profession = fields.Selection([('trainee', 'Trainee'), ('experienced', 'Experienced')], string='Profession')
    skills = fields.Char('Skills')
    quiz_score = fields.Float('Quiz Score')
    eligible_to_apply = fields.Boolean('Eligible to Apply')

    def calculate_score(self, answers):
        score = 0
        for answer in answers:
            if answer.is_correct:
                score += 10
        self.quiz_score = score
        if score > 70:
            self.eligible_to_apply = True
        else:
            self.eligible_to_apply = False
